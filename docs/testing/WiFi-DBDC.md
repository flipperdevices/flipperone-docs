---
title: DBDC
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

## Test log: DBDC mode (build 1322, 2026-06-25)

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

## STA + AP on two bands with a one-line driver patch

The "driver does not support DBDC" result above refers to the mt7915-style dual-chain `dev->dbdc_support` flag, which mainline mt76 never wires up for `mt7921`. The practical goal (a station uplink on one band and an access point on another) is reachable through a different path: cfg80211's multi-channel concurrency (MCC) / channel-context mechanism. What blocked it was the driver's advertised interface-combination table, not the hardware (BIT(5) above) and not the firmware.

### Root cause

Mainline mt76 lists only `P2P_GO`, not a full AP, on the second channel of its multi-channel interface combination (`if_limits_chanctx_mcc` in `mt792x_core.c`). cfg80211 therefore rejects `STA + AP` on two channels before the firmware is ever asked. This is why the NetworkManager attempt above fails with "Hotspot network creation took too long" / `supplicant-timeout`: the `ap0` vif can never be granted a second channel context, so the hotspot never starts.

### The fix

Add `BIT(NL80211_IFTYPE_AP)` next to `P2P_GO` in the MCC combo:

```diff
 static const struct ieee80211_iface_limit if_limits_chanctx_mcc[] = {
 	{ .max = 2, .types = BIT(NL80211_IFTYPE_STATION) | BIT(NL80211_IFTYPE_P2P_CLIENT) },
 	{
 		.max = 1,
-		.types = BIT(NL80211_IFTYPE_P2P_GO)
+		.types = BIT(NL80211_IFTYPE_P2P_GO) |
+			 BIT(NL80211_IFTYPE_AP)
 	},
 	{ .max = 1, .types = BIT(NL80211_IFTYPE_P2P_DEVICE) },
 };
```

After patching, `iw phy` advertises the AP in the two-channel combo:

```console
* #{ managed, P2P-client } <= 2, #{ AP, P2P-GO } <= 1, #{ P2P-device } <= 1,
  total <= 3, #channels <= 2
```

The firmware then accepts the concurrent AP with no `MCU ... timeout`, confirming that the closed firmware already allows it and only the driver's advertised combo was the gate.

### Verified end-to-end

Tested on an ALFA AWUS036AXML (MT7921AU, USB `0e8d:7961`) running the same firmware (`____010000-20260224110949`) as the Flipper One's WXT2AM2101 module, so the firmware-determined result transfers directly.

- STA associated to an upstream AP on one band while `ap0` ran a hotspot on the other band, verified in both cross-band orders (STA-2.4 / AP-5 GHz and STA-5 / AP-2.4 GHz).
- Real clients (Android, iPhone, MacBook) associated to the AP, completed DHCP, and passed traffic while the STA simultaneously carried an uplink on the other band. Both interfaces' byte counters advanced in the same time intervals.

Throughput (`iperf3`):

| Mode | Link | Throughput |
|------|------|-----------|
| STA 2.4 GHz | HT20 | ~74 ↑ / 60 ↓ Mbit/s |
| STA 5 GHz | VHT80 | ~250 Mbit/s |
| AP 2.4 GHz | ch1 | ~67 / 59 Mbit/s |
| AP 5 GHz | ch36, VHT80 | ~352 ↓ / 112 ↑ Mbit/s |
| STA 2.4 + AP 5 GHz (concurrent) | DBDC | AP ~84 ↑ / 319 ↓ Mbit/s under simultaneous STA load |

This is multi-channel concurrency on a single radio: under heavy AP load the STA yields airtime (its throughput drops but it stays associated). That is the expected behavior of one radio time-slicing two channels. It is usable for a travel router (uplink + hotspot), but it is not the independent dual-chain (TX0/TX1) operation the Windows QA tool describes.

### Limits

Two configurations do not work:

- Two simultaneous APs on two different bands (AP + AP). The radio brings up two AP BSSes (both reach `AP-ENABLED`), but only the first-started one beacons; the second stays silent. Verified with distinct fixed BSSIDs and cache-flushed scans from a second radio: two APs on the same channel both beacon (one channel context, multi-SSID), but on different channels only the first does. Two AP channels need a STA or P2P-client to drive the channel-switch arbiter; two passive masters (AP + AP, and also AP + P2P-GO and GO + GO, tested) don't trigger it. The ceiling is one beaconing AP whenever two channels are in use; the other context must be the client that drives the time-share.
- A third BSS context, for example STA + 2 APs. The third interface comes up in `iw` but is never granted a channel and stays off air (0 beacons in cache-flushed scans). The hardware ceiling is two concurrent BSS contexts. An earlier `EBUSY` reported here was a wedged-device / `bssid=` config artifact; on a clean driver the third context simply gets no airtime rather than erroring.

### Firmware root cause

Disassembling the WM firmware (Tensilica Xtensa; `capstone 6` `CS_ARCH_XTENSA` decodes it despite the custom-TIE opcodes that make Ghidra and objdump fail) locates the mechanism in the firmware's own data model rather than the driver:

- The MCC time-share scheduler defines quota and absence roles for STA, P2P-GO and P2P-GC (`MccStaQuotaTimeInUs`, `MccP2pGoQuotaTimeInUs`, `CnmGOAbsenceMarginInUs`) but no AP/SAP role, so a second infrastructure-AP context is never granted a concurrent channel. This is why STA + AP works (the STA drives the absence schedule, the AP rides its presence windows) while AP + AP does not.
- The `DBDC band :%d not support in MT7961` string is an ID-based DBGLOG (rendered to text off-chip by the host log tool) with no pointers found anywhere in the image, so it appears to be a diagnostic print rather than a gate that can be flipped. The MT7961 "MOBILE" SKU shares the codebase with the larger MT7972 but runs a reduced profile; `RAM_BAND_NUM = 1` (single RF).
- The blob is plaintext, unsigned and CRC-only (trailer = `zlib.crc32(fw[:-4])`, recomputable; loaded via `FW_SCATTER` + `FW_START` with no signature check), so it is patchable in principle, but there is no single byte to flip for dual-AP: the limit is a missing scheduler role plus single-RF hardware. True simultaneous dual-band dual-AP would need a two-radio (MT7915-class) part.

The same MCC path extends to 6 GHz (Wi-Fi 6E; under ETSI/SK only the low 6 GHz sub-band `5945–6425 MHz` is enabled, indoor), so STA-5 GHz + AP-6 GHz should behave like the 2.4/5 GHz pairs. The capability is confirmed via `iw phy` (Band 4 channels enabled); a live 6 GHz STA+AP run has not yet been performed.

For the full concurrency matrix, see the [Concurrency support summary](./WiFi.md) on the Wi-Fi page.
