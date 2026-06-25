---
title: AP+STA SCC testing
slug: testing/network/wifi/ap-sta-scc
---

Tests for Wi-Fi as Access Point + Station Single-Channel Concurrency (AP+STA SCC): running hotspot (AP) and client (STA) modes simultaneously on the **same band and channel**.

## Test description

Repeat on each band (2.4 GHz, 5 GHz, 6 GHz):

1.  Bring up an access point and connect to an external access point as a client, both on the same channel.
2.  Confirm both interfaces stay associated simultaneously.
3.  Measure throughput on each interface with `iperf3`.


## Test log: AP+STA (build 1350, 2026-06-23)

Environment: Debian Trixie; made sure that `NetworkManager`, `iw` and `dnsmasq` are present in the system.

1. Set Regulatory Domain if not set:

  ```bash
  sudo iw reg set HK
  ```

2. Run to **see your Wi-Fi card name**

   ```bash
   nmcli device status | grep wifi
   ```

   in our case it is called `wlxb06b11673af2`:

   ```console
   DEVICE                   TYPE      STATE                   CONNECTION 
   lo                       loopback  connected (externally)  lo         
   wlxb06b11673af2          wifi      disconnected            --     
   ```

3. The AP will live on a second virtual interface named `ap0` on the same phy, because one netdev can't be STA and AP simultaneously. `udev` will try to rename a freshly created `ap0` to a wlx* predictable name, which breaks the NM profile binding.
   Pin the name with a `.link` file:

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

4. Create a LAN bridge (NAT + DHCP)

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

5. Verify that the bridge is NM-owned (not "externally" managed):

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
   11182 /usr/sbin/dnsmasq --conf-file=/dev/null --no-hosts --keep-in-foreground --bind-interfaces --except-interface=lo --clear-on-reload --strict-order --listen-address=192.168.50.1 --dhcp-range=192.168.50.10,192.168.50.254,3600 --dhcp-leasefile=/var/lib/NetworkManager/dnsmasq-br-lan.leases --pid-file=/run/nm-dnsmasq-br-lan.pid --conf-dir=/etc/NetworkManager/dnsmasq-shared.d
   ```

6. Create an STA uplink

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
   iw dev "wlxb06b11673af2" info
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

7. Create an AP profile

  ```bash
  sudo nmcli connection add type wifi con-name ap-downlink ifname ap0 \
    ssid FlipperOne \
    wifi-sec.key-mgmt wpa-psk wifi-sec.psk 'flipperone' \
    802-11-wireless.mode ap \
    802-11-wireless.powersave 2 \
    master br-lan slave-type bridge \
    connection.autoconnect no
  ```

8. Bring-up helper.

   This is the piece that makes SCC work:

   - it brings the STA up first (so it owns the channel context),
   - reads the STA's channel/width,
   - creates `ap0` with a stable MAC set atomically at creation,
   - pins the AP chandef to the STA,
   - and activates the AP.


   First, write an `~/apsta-up` script:
   ```bash
   sudo tee ~/apsta-up >/dev/null <<'EOF'
   #!/bin/sh
   # Bring up an SCC AP on ap0 locked to the STA's current channel.
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

   # 5. pin AP chandef to the STA (SCC) and force the stable MAC (disables randomization)
   nmcli connection modify "$AP_CON" \
       802-11-wireless.band "$BAND" \
       802-11-wireless.channel "$CH" \
       802-11-wireless.cloned-mac-address "$APMAC"
   # channel-width only exists on NM >= 1.50; ignore failure on older releases
   nmcli connection modify "$AP_CON" 802-11-wireless.channel-width "${WMHZ:-20}" 2>/dev/null || true

   # 6. activate
   nmcli connection up "$AP_CON"
   echo "apsta: $AP_IF up  band=$BAND ch=$CH width=${WMHZ:-20} mac=$APMAC  (matched to $STA)"
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
   Connection successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/9)
   apsta: ap0 up  band=a ch=36 width=80 mac=xx:xx:xx:xx:xx:xx  (matched to wlxb06b11673af2)
   ```

9. Check network connectivity:

  ```bash
  ping flipper.net
  ```

10. Connect to your freshly created SSID `FlipperOne` with your phone/laptop and check the network connectivity.
