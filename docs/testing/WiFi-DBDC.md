---
title: Dual-Band Dual-Concurrent
slug: testing/network/wifi/dbdc
---

Tests for **DBDC** — Dual-Band Dual-Concurrent operation: running two interfaces on two different bands at the same time (for example, an access point on 5 GHz while a client runs on 2.4 GHz).

## Test sequence

:::::WorkflowBlock
:::WorkflowBlockItem
Bring up two interfaces on two different bands simultaneously.
:::

:::WorkflowBlockItem
Confirm both operate independently without interference.
:::

:::WorkflowBlockItem
Measure throughput on each band with `iperf3`.
:::

:::WorkflowBlockItem
Test combinations: AP + STA, AP + AP, STA + STA across band pairs.
:::
:::::

## ❌ Test log: AP+STA dual-band

> Tested and recorded using build `1322` at 25 Jun 2026.
> 
> - 2.4 GHz AP
> - 5 GHz STA


Environment: Debian Trixie; made sure that `NetworkManager`, `iw` and `dnsmasq` are present in the system.

:::::WorkflowBlock
:::WorkflowBlockItem
Set Regulatory Domain if not set

```bash
sudo iw reg set HK
```
:::

:::WorkflowBlockItem
Run to **see your Wi-Fi card name**

```bash
nmcli device status | grep wifi
```

in our case it is called `wlxb06b11673af2`:

```console
DEVICE                   TYPE      STATE                   CONNECTION 
lo                       loopback  connected (externally)  lo         
wlxb06b11673af2          wifi      disconnected            --     
```
:::

:::WorkflowBlockItem
The AP will live on a second virtual interface named `ap0` on the same phy, because one netdev can't be STA and AP simultaneously. `udev` will try to rename a freshly created `ap0` to a wlx* predictable name, which breaks the NM profile binding. Pin the name with a `.link` file:

```bash
sudo tee /etc/systemd/network/10-ap0.link >/dev/null <<'EOF'
[Match]
OriginalName=ap0

[Link]
Name=ap0
EOF
```

Apply it:

```bash
sudo udevadm control --reload
```
:::

:::WorkflowBlockItem
Create a LAN bridge (NAT + DHCP)

Change `192.168.50.1/24` if it overlaps the upstream AP subnet. These two subnets must differ; otherwise, routing collapses.

```bash
sudo nmcli connection add type bridge con-name br-lan ifname br-lan \
  ipv4.method shared ipv4.addresses 192.168.50.1/24 \
  ipv6.method ignore \
  connection.autoconnect yes
```

Bring it up:

```bash
sudo nmcli connection up br-lan
```
:::

:::WorkflowBlockItem
Verify that the bridge is NM-owned (not "externally" managed):

```bash
nmcli -f GENERAL.STATE device show br-lan     # must NOT say 'externally'
ip addr show br-lan | grep inet               # expect 192.168.50.1/24
pgrep -a dnsmasq                              # expect one bound to br-lan
```

In our case:

```console
$ nmcli -f GENERAL.STATE device show br-lan
GENERAL.STATE:                          100 (connected)

$ ip addr show br-lan | grep inet
    inet 192.168.50.1/24 brd 192.168.50.255 scope global noprefixroute br-lan

$ pgrep -a dnsmasq
15291 /usr/sbin/dnsmasq --conf-file=/dev/null --no-hosts --keep-in-foreground --bind-interfaces --except-interface=lo --clear-on-reload --strict-order --listen-address=192.168.50.1 --dhcp-range=192.168.50.10,192.168.50.254,3600 --dhcp-leasefile=/var/lib/NetworkManager/dnsmasq-br-lan.leases --pid-file=/run/nm-dnsmasq-br-lan.pid --conf-dir=/etc/NetworkManager/dnsmasq-shared.d
```
:::

:::WorkflowBlockItem
Create an STA uplink

Replace **wlan0**, **YourHomeWiFi**, and **upstream-password** with your values:

```bash
sudo nmcli connection add type wifi con-name sta-uplink ifname wlan0 \
  ssid YourHomeWiFi \
  wifi-sec.key-mgmt wpa-psk wifi-sec.psk 'upstream-password' \
  ipv4.method auto ipv6.method ignore \
  connection.autoconnect yes
```

Bring it up:

```bash
sudo nmcli connection up sta-uplink
```

Verify (change **wlan0** here first):

```bash
iw dev wlan0 info
```

We got this output:

```console
Interface wlxb06b11673af2
	ifindex 5
	wdev 0x1
	addr b0:6b:11:67:3a:f2
	type managed
	wiphy 0
	channel 36 (5180 MHz), width: 80 MHz, center1: 5210 MHz
	txpower 3.00 dBm
	multicast TXQ:
		qsz-byt	qsz-pkt	flows	drops	marks	overlmt	hashcol	tx-bytes	tx-packets
		0	0	0	0	0	0	0	0		0

```
:::

:::WorkflowBlockItem
Create an AP profile

```bash
sudo nmcli connection add type wifi con-name ap-downlink ifname ap0 \
  ssid FlipperOne \
  wifi-sec.key-mgmt wpa-psk wifi-sec.psk 'flipperone' \
  802-11-wireless.mode ap \
  802-11-wireless.powersave 2 \
  master br-lan slave-type bridge \
  connection.autoconnect no
```
:::

:::WorkflowBlockItem
Bring-up helper.

This is the piece that attempts DBDC:

- it brings the STA up first (so it owns the channel context),
- reads the STA's channel/width,
- creates `ap0` with a stable MAC set atomically at creation,
- pins the AP chandef to the other band,
- and activates the AP.

First, write an `~/apsta-up` script:

```bash
sudo tee ~/apsta-up >/dev/null <<'EOF'
#!/bin/sh
# Attempt a DBDC AP on ap0 on the other band from the STA.
set -eu

STA_CON=sta-uplink
AP_CON=ap-downlink
AP_IF=ap0

# 1. resolve the base wifi device (first real wifi; never p2p-dev, never ap0)
STA=$(nmcli -t -f DEVICE,TYPE device status \
      | awk -F: -v ap="$AP_IF" '$2=="wifi" && $1!=ap {print $1; exit}')
[ -n "$STA" ] || { echo "apsta: no wifi device found" >&2; exit 1; }

# 2. ensure uplink is up; wait for association (channel-context owner)
nmcli connection up "$STA_CON" >/dev/null 2>&1 || true
i=0
while :; do
    CH=$(iw dev "$STA" info 2>/dev/null | awk '/channel/{print $2}')
    [ -n "${CH:-}" ] && break
    i=$((i+1)); [ "$i" -ge 30 ] && { echo "apsta: STA not associated after 30s" >&2; exit 1; }
    sleep 1
done
WMHZ=$(iw dev "$STA" info | sed -n 's/.*width: \([0-9]*\).*/\1/p')
[ "$CH" -le 14 ] && BAND=bg || BAND=a

# 3. stable locally-administered MAC for the AP vif (distinct from STA on same phy)
PHY=$(iw dev "$STA" info | awk '/wiphy/{print "phy"$2}')
MAC=$(cat /sys/class/net/"$STA"/address)
APMAC="02:${MAC#*:}"

# 4. (re)create ap0 with the MAC set atomically at creation
iw dev "$AP_IF" del 2>/dev/null || true
iw phy "$PHY" interface add "$AP_IF" type __ap addr "$APMAC"

# 5. force AP onto the other band (DBDC) and force the stable MAC (disables randomization)
[ "$BAND" = a ] && { APBAND=bg; APCH=6; APW=20; } || { APBAND=a; APCH=36; APW=80; }
nmcli connection modify "$AP_CON" \
    802-11-wireless.band "$APBAND" \
    802-11-wireless.channel "$APCH" \
    802-11-wireless.cloned-mac-address "$APMAC"
# channel-width only exists on NM >= 1.50; ignore failure on older releases
nmcli connection modify "$AP_CON" 802-11-wireless.channel-width "$APW" 2>/dev/null || true

# 6. activate
nmcli connection up "$AP_CON"
echo "apsta: $AP_IF up  band=$APBAND ch=$APCH width=$APW mac=$APMAC  (STA on $STA)"
EOF
```

Set script permissions:

```bash
sudo chmod +x ~/apsta-up
```

Run the script:

```bash
sudo ~/apsta-up
```

Example output:

```console
$ sudo ./apsta-up 
<SKIPPED>
[  705.971837] wlxb06b11673af2: deauthenticating from xx:xx:xx:xx:xx:xx by local choice (Reason: 3=DEAUTH_LEAVING)
[  706.325902] wlxb06b11673af2: authenticate with xx:xx:xx:xx:xx:xx (local address=xx:xx:xx:xx:xx:xx)
[  706.335759] wlxb06b11673af2: send auth to xx:xx:xx:xx:xx:xx (try 1/3)
[  706.338224] wlxb06b11673af2: authenticated
[  706.341785] wlxb06b11673af2: associate with xx:xx:xx:xx:xx:xx (try 1/3)
[  706.346504] wlxb06b11673af2: RX AssocResp from xx:xx:xx:xx:xx:xx (capab=0x431 status=0 aid=3)
[  706.359261] wlxb06b11673af2: associated
Error: Connection activation failed: 802.1X supplicant took too long to authenticate
Hint: use 'journalctl -xe NM_CONNECTION=d63b4dd9-ea30-4b55-8931-55d12c8267f5 + NM_DEVICE=ap0' to get more details.
```

Let's see the journal:

```console
Jun 25 18:33:28 flipperone-a9438e-build-1322-router-target NetworkManager[542]: <warn>  [1782412408.0506] device (ap0): Activation: (wifi) Hotspot network creation took too long, failing activation
Jun 25 18:33:28 flipperone-a9438e-build-1322-router-target NetworkManager[542]: <info>  [1782412408.0507] device (ap0): state change: config -> failed (reason 'supplicant-timeout', managed-type: 'full')
```
:::
:::::

## ❌ Test log: AP+AP dual-band

> Tested and recorded using build `1393` at 26 Jun 2026.
> 
> - 2.4 GHz AP
> - 5 GHz AP

Environment: Debian Trixie; made sure that `NetworkManager`, `iw` and `dnsmasq` are present in the system.

:::::WorkflowBlock
:::WorkflowBlockItem
Set Regulatory Domain if not set:

```bash
sudo iw reg set HK
```
:::

:::WorkflowBlockItem
See your Wi-Fi card name and resolve its phy:

```bash
nmcli device status | grep wifi
iw dev wlxb06b11673af2 info | awk '/wiphy/{print "phy"$2}'
```

In our case the card is `wlxb06b11673af2` on `phy0`:

```console
DEVICE                   TYPE      STATE                   CONNECTION 
wlxb06b11673af2          wifi      disconnected            --     
phy0
```
:::

:::WorkflowBlockItem
**Ask the radio which interface combinations it allows.** This settles the question before any AP is brought up:

```bash
iw phy phy0 info | sed -n '/valid interface combinations/,/HT Capability/p'
```

On this build:

```console
	valid interface combinations:
	 * #{ managed, P2P-client } <= 2, #{ P2P-GO } <= 1, #{ P2P-device } <= 1,
	   total <= 3, #channels <= 2
	 * #{ managed, P2P-client } <= 2, #{ AP } <= 1, #{ P2P-device } <= 1,
	   total <= 3, #channels <= 1
	HT Capability overrides:
```

Reading it:

- Only the **second** combination contains `AP`, and it caps **`#{ AP } <= 1`**. There is no combination anywhere that permits two `AP` interfaces.
- That same AP combination is limited to **`#channels <= 1`** (so an AP can only coexist with a STA on the same channel — SCC — which is why the [AP+STA SCC guide](./WiFi-AP-STA-SCC.md) pins them together).
- The **first** combination is the only one allowing two channels (**`#channels <= 2`**, i.e. DBDC), covering `managed`/`P2P-client` + `P2P-GO` only — never a normal `AP`.

Conclusion: **two APs are impossible on any band combination** — the failure is at the AP-count limit, before channels are even considered.
:::

:::WorkflowBlockItem
**Empirical confirmation (raw `iw`, no NetworkManager).**

Clean slate — remove any leftover vifs:

```bash
for i in ap0 ap1; do sudo iw dev $i del 2>/dev/null; done
```

First AP vif — allowed (this is the one AP the radio permits):

```bash
sudo iw phy phy0 interface add ap0 type __ap addr 02:6b:11:67:3a:f2
sudo ip link set ap0 up
```

No errors, `ap0` is up.

Second AP vif — refused. The refusal lands either at `interface add` or at `ip link set ... up` depending on kernel; on this build it is at bring-up:

```bash
sudo iw phy phy0 interface add ap1 type __ap addr 06:6b:11:67:3a:f2
sudo ip link set ap1 up
```

```console
$ sudo ip link set ap1 up
RTNETLINK answers: Device or resource busy
```

The `Device or resource busy` (`-EBUSY`) is the combination check rejecting a second `AP` interface — confirmed before any channel or band is assigned, exactly as the table above predicts.

Tidy up:

```bash
for i in ap0 ap1; do sudo iw dev $i del 2>/dev/null; done
```
:::
:::::

**Conclusion:** `#{ AP } <= 1` — the radio exposes only one AP slot. Two APs on any band combination are impossible. Genuine dual-band AP requires a second radio or a DBDC AP-class chip (MT7915/7916/7986/7996) whose driver exposes an AP combination with `#channels <= 2`.

## Register readout

As of 25 June 2026 and Kernel 7.1.1, `mt7921` driver does not support DBDC.

Support for DBDC [has been added to mt7915](https://github.com/openwrt/mt76/commit/b436da4d9d925f6ff80310841d1fbeb25c93b667) and mt7925 (router SoCs) driver [by OpenWrt project](https://github.com/openwrt/mt76/issues/315), but not to other models.

The check for DBDC support from mt7915 is performed as follows:

```c
dev->dbdc_support = !!(mt7915_l1_rr(dev, MT_HW_BOUND) & BIT(5));
```

where `MT_HW_BOUND = 0x70010020`.

Attempt to read this value on FENVI AX1800 and EDUP AX3000 7921u modules results in follows:

```sh
/sys/kernel/debug/ieee80211/phy4/mt76# echo 0x70010020 > regidx 
/sys/kernel/debug/ieee80211/phy4/mt76# cat regval

0x00000020
```

Which means that BIT(5) == 1 and DBDC is **supported in hardware** on 7921u.

### Windows drivers

There's an evidence from [MT7921 QA-Tool User Guideline PDF](https://www.mouser.com/datasheet/2/1074/User_Manual_5321522-3304019.pdf) that Windows drivers support DBDC, and the hardware supports it in the following configuration:

>MT7921 support only below dual-band dual-concurrent (DBDC) mode operation:  
>* (Tab TX/RX) TX0/RX0 transceiver is operating in 5GHz (A-band)  
>* (Tab TX/RX Band 1) TX1/RX1 transceiver is operation in 2.4GHz (G-band)
