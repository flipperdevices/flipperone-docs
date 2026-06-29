---
title: Monitor mode
slug: testing/network/wifi/monitor
---

Tests for monitor (promiscuous) mode, where the Wi-Fi card captures all traffic on a given channel rather than associating with a network.

## Test sequence

:::::WorkflowBlock
:::WorkflowBlockItem
Switch the Wi-Fi card to monitor mode.
:::

:::WorkflowBlockItem
Dump traffic on each band.
:::

:::WorkflowBlockItem
Decode the captured traffic.
:::
:::::

## PMKID sniff

Perform an RSN PMKID sniff against a real access point.


## ✅ Test log: Monitor mode

> Tested and recorded using build `1350` at 23 Jun 2026.

Environment: Debian Trixie; made sure that `NetworkManager`, `iw` and `dnsmasq` are present in the system.

:::::WorkflowBlock
:::WorkflowBlockItem
Switch to superuser console:

```bash
sudo su
```
:::

:::WorkflowBlockItem
Run this to see your Wi-Fi card name:

```bash
nmcli device status | grep wifi
```

in our case it is named `wlxb06b11673af2`:

```console
DEVICE                   TYPE      STATE                   CONNECTION 
lo                       loopback  connected (externally)  lo         
wlxb06b11673af2          wifi      disconnected            --     
```
:::

:::WorkflowBlockItem
Save the Wi-Fi card name to a variable:

```bash
DEV=wlxb06b11673af2
```
:::

:::WorkflowBlockItem
Release the radio from NetworkManager and tear down:

```bash
nmcli dev set "$DEV" managed no
ip link set "$DEV" down
iw dev "$DEV" del
```
:::

:::WorkflowBlockItem
Stop anything that retunes the radio:

```bash
pkill -x wpa_supplicant 2>/dev/null
rfkill unblock wifi
```
:::

:::WorkflowBlockItem
Set regdomain BEFORE creating the vif, while the phy is idle:

```bash
iw reg set HK
```
:::

:::WorkflowBlockItem
Create monitor as the ONLY vif on `phy0`:

```bash
iw phy phy0 interface add mon0 type monitor
ip link set mon0 up
```
:::

:::WorkflowBlockItem
Tune to any channel:

```bash
iw dev mon0 set channel 36
```
:::

:::WorkflowBlockItem
Verify:

```bash
tcpdump -i mon0 -e -n -s 256 |grep -i beacon
```

You should be able to see SSID beacon packets:

```console
13:21:53.554963 22732764us tsft 6.0 Mb/s 5180 MHz 11a -66dBm signal [bit 22] BSSID:xx:xx:xx:xx:xx:xx DA:ff:ff:ff:ff:ff:ff SA:xx:xx:xx:xx:xx:xx Beacon (Chasing the 5G Nut) [6.0* 9.0 12.0* 18.0 24.0* 36.0 48.0 54.0 Mbit] ESS, PRIVACY [|802.11]
13:21:53.567951 22745773us tsft 6.0 Mb/s 5180 MHz 11a -40dBm signal [bit 22] BSSID:xx:xx:xx:xx:xx:xx DA:ff:ff:ff:ff:ff:ff SA:xx:xx:xx:xx:xx:xx Beacon (Sid the Sloth) [6.0* 9.0 12.0 18.0 24.0 36.0 48.0 54.0 Mbit] ESS, PRIVACY [|802.11]
13:21:53.657399 22835161us tsft 6.0 Mb/s 5180 MHz 11a -66dBm signal [bit 22] BSSID:xx:xx:xx:xx:xx:xx DA:ff:ff:ff:ff:ff:ff SA:xx:xx:xx:xx:xx:xx Beacon (Chasing the 5G Nut) [6.0* 9.0 12.0* 18.0 24.0* 36.0 48.0 54.0 Mbit] ESS, PRIVACY [|802.11]
13:21:53.670426 22848173us tsft 6.0 Mb/s 5180 MHz 11a -40dBm signal [bit 22] BSSID:xx:xx:xx:xx:xx:xx DA:ff:ff:ff:ff:ff:ff SA:xx:xx:xx:xx:xx:xx Beacon (Sid the Sloth) [6.0* 9.0 12.0 18.0 24.0 36.0 48.0 54.0 Mbit] ESS, PRIVACY [|802.11]
13:21:53.759809 22937572us tsft 6.0 Mb/s 5180 MHz 11a -66dBm signal [bit 22] BSSID:xx:xx:xx:xx:xx:xx DA:ff:ff:ff:ff:ff:ff SA:xx:xx:xx:xx:xx:xx Beacon (Chasing the 5G Nut) [6.0* 9.0 12.0* 18.0 24.0* 36.0 48.0 54.0 Mbit] ESS, PRIVACY [|802.11]
13:21:53.772734 22950573us tsft 6.0 Mb/s 5180 MHz 11a -41dBm signal [bit 22] BSSID:xx:xx:xx:xx:xx:xx DA:ff:ff:ff:ff:ff:ff SA:xx:xx:xx:xx:xx:xx Beacon (Sid the Sloth) [6.0* 9.0 12.0 18.0 24.0 36.0 48.0 54.0 Mbit] ESS, PRIVACY [|802.11]
```
:::
:::::
