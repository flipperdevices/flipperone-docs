---
title: RM520N-GL
slug: testing/network/cellular/rm520n-gl
---

::Image[]{src="/files/pics/rm520n-gl-cellular-modem.png" size="30" width="438" height="615" position="center" caption="Quectel RM520N-GL M.2 module"}

The Quectel RM520N-GL is a 5G Sub-6 GHz M.2 modem. Flipper One detects it over USB 3 with no extra setup: the in-kernel `option` and `qmi_wwan` drivers bind to it, and ModemManager uses the `quectel` plugin to talk to it over QMI.

## Datasheets

| Document | Contents |
|---|---|
| [RM520N Series 5G Module Specification V1.6](https://github.com/flipperdevices/flipperone-docs/blob/public-release/docs/files/datasheets/RM520N-GL/Quectel_RM520N_Series_5G_Module_Specification_V1.6.pdf) | Key features, bands, data rates, interfaces |
| [RM520N Series Reference Design V1.2](https://github.com/flipperdevices/flipperone-docs/blob/public-release/docs/files/datasheets/RM520N-GL/quectel_rm520n_series_reference_design_v1-2.pdf) | Quectel's reference design for the module |
| [RG520N, RG525F, RG5x0F, RM5x0N Series AT Commands Manual V1.1](https://github.com/flipperdevices/flipperone-docs/blob/public-release/docs/files/datasheets/RM520N-GL/quectel_rg520nrg525frg5x0frm5x0n_series_at_commands_manual_v1-1.pdf) | AT command reference for the RM520N and related Quectel 5G modules |
| [5G-M2 EVB User Guide V1.1](https://github.com/flipperdevices/flipperone-docs/blob/public-release/docs/files/datasheets/RM520N-GL/quectel_5g-m2_evb_user_guide_v1-1.pdf) | Quectel's evaluation board for 5G M.2 modules |
| [RM520N Series Hardware Design V1.3](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6382/Quectel_RM520N_Series_Hardware_Design_V1.3.pdf) | Pinout, antenna connectors and their bands, RF and electrical characteristics. Hosted by Digi-Key. |

## Status

| Check | Status | Notes |
|---|:---:|---|
| USB enumeration | ✅ | SuperSpeed (5 Gbps), `2c7c:0801` |
| Kernel drivers | ✅ | mainline `option` + `qmi_wwan`, no patches |
| ModemManager detection | ✅ | `quectel` plugin, QMI primary port |
| SIM detection | ✅ | slot 1, USIM, PIN disabled |
| Network registration | ✅ | Vodafone UK (234/15), home network |
| Data connection (NetworkManager) | ✅ | IPv4 over `raw-ip` QMI, MTU 1500 |
| Signal and cell info (ModemManager) | ✅ | serving and neighbour cells, LTE and 5G signal |
| LTE carrier aggregation | ✅ | B1 + B20 aggregated (B7 configured but not active) |
| 5G NR (NSA) | ⚠️ | cell advertises NSA, but no stable NR link during the test (weak signal) |
| 5G NR (SA) | ✅ | n78, 100 MHz, Vodafone UK. About 930 Mbit/s download with receive tuning, see [USB interface](#usb-interface) |
| AT command ports | ⚠️ | both ports are held by ModemManager. Use debug mode for tests, see [AT commands](#at-commands) |
| Per-antenna signal | ✅ | all four receive paths work on B1. Low bands such as B20 use only two, see [Per-antenna signal](#per-antenna-signal) |
| Module temperature | ✅ | 44–47 °C during the test, no heatsink |
| GNSS | ⚠️ | engine starts and outputs NMEA through `gps-unmanaged`; no satellites in 5 min indoors. ModemManager's QMI GNSS modes fail, see [GNSS](#gnss) |
| rfkill (W_DISABLE1# / W_DISABLE2#) | ⚠️ | W_DISABLE1 turns cellular off, W_DISABLE2 turns GNSS off, but NetworkManager treats both as cellular kill switches, see [rfkill switches](#rfkill-switches) |
| PCIe mode | ⚠️ | data works over PCIe Gen 2 ×1, but only with a runtime driver workaround, see [PCIe mode](#pcie-mode) |

## Module specifications

| Parameter | Value |
|---|---|
| Manufacturer | Quectel |
| Model | RM520N-GL, AA firmware variant (`RM520NGLAA…`) |
| Chipset | Qualcomm Snapdragon X62 |
| Form factor | M.2 Key B, 30.0 × 52.0 × 2.3 mm, about 8.7 g |
| 3GPP release | Release 16 |
| Radio technologies | 5G NR (SA and NSA, Sub-6 GHz only, no mmWave), LTE, WCDMA. No 2G (GSM). |
| Peak data rate, 5G SA | 2.4 Gbps down / 900 Mbps up |
| Peak data rate, 5G NSA | 3.4 Gbps down / 550 Mbps up |
| Peak data rate, LTE | 1.6 Gbps down / 200 Mbps up (DL Cat 19, UL Cat 18) |
| Peak data rate, WCDMA | 42 Mbps down / 5.76 Mbps up |
| Host interfaces | USB 2.0, USB 3.1, PCIe 3.0 ×1. Flipper One uses USB by default. |
| (U)SIM | 2 interfaces, (U)SIM card detection, eSIM optional |
| Antenna connectors | 4 (ANT0–ANT3), shared by Sub-6 GHz and GNSS |
| GNSS | Optional: GPS, GLONASS, BeiDou, Galileo, QZSS (Qualcomm IZat Gen9C Lite) |
| Supply voltage | 3.135–4.4 V, typical 3.7 V |
| Power consumption | 195 µA powered down, 4.7 mA sleep, 40 mA idle on USB 2.0, 60 mA idle on USB 3.0 |
| Operating temperature | −30 °C to +75 °C |
| Extended temperature range | −40 °C to +85 °C |
| Firmware tested | `RM520NGLAAR03A04M4G` (`AT+QGMR`: `RM520NGLAAR03A04M4G_A0.301.A0.301`) |
| Hardware revision | `20000` |
| Carrier config (MBN) | `UK-VoLTE-Vodafone`, revision `0A010426` (selected automatically from the SIM) |

Module data is from the [RM520N Series 5G Module Specification V1.6](https://github.com/flipperdevices/flipperone-docs/blob/public-release/docs/files/datasheets/RM520N-GL/Quectel_RM520N_Series_5G_Module_Specification_V1.6.pdf). Peak data rates are theoretical. Firmware, hardware revision and carrier config were read from the test unit.

### Supported bands

Bands reported by the module (`qmicli --dms-get-band-capabilities`), and the NSA list from the specification:

| Technology | Bands |
|---|---|
| 5G NR SA | n1, n2, n3, n5, n7, n8, n12, n13, n14, n18, n20, n25, n26, n28, n29, n30, n38, n40, n41, n48, n66, n70, n71, n75, n76, n77, n78, n79 |
| 5G NR NSA | n1, n2, n3, n5, n7, n8, n12, n14, n20, n25, n28, n30, n38, n40, n41, n48, n66, n71, n77, n78, n79 (from the specification; the module reports the SA list for both modes) |
| LTE | B1, B2, B3, B4, B5, B7, B8, B12, B13, B14, B17, B18, B19, B20, B25, B26, B28, B29, B30, B32, B34, B38, B39, B40, B41, B42, B43, B46, B48, B66, B71 |
| WCDMA | B1 (2100), B2 (1900), B4 (1700), B5 (850), B6 (800), B8 (900), B19 (850 Japan) |

All bands are enabled by default. The acquisition order is 5G NR → LTE → WCDMA.

ModemManager offers these mode combinations: 3G, 4G, 5G, and any pair or all three with one preferred. There is no 2G mode.

## Antennas

::Image[]{src="/files/pics/rm520n-gl-antenna-connectors.svg" size="60" width="640" height="720" position="center" caption="RM520N-GL antenna connectors, label side up"}

The RM520N-GL has four antenna connectors, ANT0–ANT3, along the edge opposite the M.2 contacts. The two square pads next to ANT3 are not antenna connectors. All four connectors carry cellular signals; ANT1 and ANT3 also carry GNSS.

### What each connector does

Each connector has a different role depending on the frequency band. From Table 32 of the [RM520N Series Hardware Design V1.3](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6382/Quectel_RM520N_Series_Hardware_Design_V1.3.pdf):

| Connector | Low band, 617–960 MHz | Mid/high band, 1452–2690 MHz | 5G n41 | 5G n77/n78/n79 and LTE 3.4–3.8 GHz | Other |
|---|---|---|---|---|---|
| ANT0 | TX + primary RX | TX + primary RX | TX + primary RX | Second TX + diversity RX | WCDMA TX + RX |
| ANT1 | — | MIMO RX (3rd path) | MIMO RX (3rd path) | MIMO RX (3rd path) | LTE LAA RX, GNSS L5 |
| ANT2 | — | MIMO RX (4th path), second TX for EN-DC | Second TX + MIMO RX (4th path) | TX + primary RX | — |
| ANT3 | Diversity RX, second TX for EN-DC | Diversity RX | Diversity RX | MIMO RX | LTE LAA RX, WCDMA RX, GNSS L1 |

Terms:

| Term | Meaning |
|---|---|
| TX | Transmit. ANT0 is the main transmit antenna on most bands. |
| Primary RX (PRX) | The main receive path. |
| Diversity RX (DRX) | The second receive path. Together with the primary path it gives 2×2 MIMO. |
| MIMO RX | The third and fourth receive paths, used for 4×4 MIMO. |
| Second TX | Used only for uplink MIMO or EN-DC (LTE and 5G transmitting at the same time). |
| Low band | LTE B5, B8, B12, B13, B14, B17, B18, B19, B20, B26, B28, B71 and 5G n5, n8, n12, n13, n14, n18, n20, n26, n28, n71 |
| Mid/high band | For example LTE B1, B2, B3, B4, B7, B25, B30, B66 and 5G n1, n2, n3, n7, n25, n30, n66 |

What this means in practice:

- **Low bands use only two antennas, ANT0 and ANT3.** ANT1 and ANT2 are not connected to the low-band receivers. On LTE B20 (800 MHz), a common band in Europe, the modem receives on two paths at most.
- **Mid and high bands and n41 use all four antennas** for 4×4 MIMO receive.
- **5G n77, n78, n79 and LTE B42, B43, B48 (3.3–5 GHz) transmit on ANT2,** not ANT0. ANT0 is their second transmitter and diversity receiver.
- **GNSS L1 is on ANT3, L5 on ANT1.** For GNSS, at least ANT3 must have an antenna that covers 1559–1609 MHz.

### Antenna requirements

From Table 41 of the hardware design guide:

| Type | Requirement |
|---|---|
| Cellular (WCDMA, LTE, 5G) | VSWR ≤ 2, efficiency > 30 %, 50 Ω |
| Cable loss, low band (< 1 GHz) | < 1 dB |
| Cable loss, mid band (1–2.3 GHz) | < 1.5 dB |
| Cable loss, high band (> 2.3 GHz) | < 2 dB |
| GNSS | L1 1559–1609 MHz, L5 1166–1187 MHz, RHCP or linear polarization, VSWR ≤ 2, passive antenna gain > 0 dBi |

The connectors are standard 2 × 2 mm RF receptacles, 50 Ω, rated DC–6 GHz, for Ø0.81 mm or Ø1.13 mm coaxial cable. Adapters and pigtails for them are commonly sold as MHF4 or IPEX4. Quectel recommends a passive GNSS antenna when LTE B13 or B14 is in use, because an active one can pick up harmonics.

### How to connect antennas

**Four antennas (recommended).** Connect a wideband antenna (617–6000 MHz) to each of ANT0–ANT3. This gives 4×4 MIMO on mid and high bands, 2×2 on low bands, and GNSS on ANT1 and ANT3.

**Fewer than four antennas.** Always connect ANT0, since it is the main transmit antenna on most bands. The second most important is ANT3, the diversity receiver on every band and the GNSS L1 input. With only ANT0 and ANT3 connected, the modem still works with 2×2 MIMO on all bands except 5G n77/n78/n79 and LTE B42/B43/B48 (3.3–5 GHz), which transmit on ANT2.

:::hint{type="warning"}
Do not leave a transmitting connector open. ANT0 transmits on most bands, ANT2 on 3.3–5 GHz bands, and ANT2 and ANT3 can transmit during EN-DC. If one of them has no antenna, terminate it with a 50 Ω load or connect a small antenna.
:::

### Using a 2×2 MIMO directional antenna

A 2×2 MIMO directional antenna, such as a Yagi or panel antenna, has two ports that point the same way, usually with cross polarization (±45° or horizontal/vertical). It works with the RM520N-GL as a two-path antenna. Which two connectors to use depends on the band you need:

| Bands you want to improve | Port 1 | Port 2 | Leave on small antennas |
|---|---|---|---|
| LTE and 5G on low and mid bands, n41 (most LTE networks) | ANT0 | ANT3 | ANT1, ANT2 |
| 5G n77/n78/n79, LTE B42/B43/B48 (3.3–5 GHz) | ANT2 | ANT0 | ANT1, ANT3 |

For example, for LTE B20 or B1 with a 2×2 Yagi:

1. Connect Yagi port 1 to ANT0 and port 2 to ANT3. On low bands such as B20 these are the only two receive antennas, so the Yagi gets all of the benefit.
2. Connect small wideband antennas to ANT1 and ANT2. On mid bands they add the third and fourth receive paths, and they keep ANT2 terminated.
3. Make sure the Yagi covers the band the network uses. Yagis are usually narrowband: an 800 MHz Yagi does nothing on B1 (2100 MHz). Check the band with `AT+QENG="servingcell"` or `sudo qmicli -d /dev/cdc-wdm0 --device-open-proxy --nas-get-rf-band-info`. If the modem moves to a band the Yagi does not cover, limit the modem to the Yagi's bands with `sudo mmcli -m any --set-current-bands`, for example `--set-current-bands=eutran-20` for B20 only.
4. Keep the coaxial cables short and low-loss. The limits above (under 1 dB on low band, 2 dB on high band) are easy to exceed with a few meters of thin cable.
5. Point the antenna at the cell. Compare the PRX and DRX values from `AT+QRSRP` and `AT+QSINR` while you turn it. Both ports should improve together.
6. GNSS L1 is also on ANT3. A Yagi pointing sideways is a poor GNSS antenna. If you need GNSS, put the Yagi on ANT0 and ANT1 instead and keep a wideband or GNSS antenna on ANT3. This loses the low-band diversity path, because ANT1 has no low-band receiver.

:::hint{type="info"}
The antenna requirements and connector roles come from Quectel's hardware design guide. The Yagi setup has not been tested on Flipper One yet.
:::

## USB interface

| Parameter | Value |
|---|---|
| VID:PID | `2c7c:0801` |
| Manufacturer string | `Quectel` |
| Product string | `RM520N-GL` |
| `bcdDevice` | `5.04` |
| USB version | `bcdUSB 3.20` |
| Negotiated speed | SuperSpeed, 5 Gbps |
| Configuration | 1 configuration, `DIAG_SER_RMNET` |
| Interfaces | 5 |
| Power | Bus powered, `MaxPower 896mA`, remote wakeup supported |

:::hint{type="info"}
The RM520N-GL and the [RM530N-GL](RM530N-GL.md) both use VID:PID `2c7c:0801` and the same interface layout. Use `lsusb` to see the product string, or `mmcli -L` to see the model, when you need to tell them apart. Any udev rule that matches `2c7c:0801` applies to both modems.
:::

On the test unit the modem was connected through the onboard USB 3.0 hub (Corechips `3431:6341`), at USB path `2-1.4`:

```text
$ lsusb -t
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci-hcd/1p, 5000M
    |__ Port 001: Dev 002, If 0, Class=Hub, Driver=hub/4p, 5000M
        |__ Port 004: Dev 003, If 0, Class=Vendor Specific Class, Driver=option, 5000M
        |__ Port 004: Dev 003, If 1, Class=Vendor Specific Class, Driver=option, 5000M
        |__ Port 004: Dev 003, If 2, Class=Vendor Specific Class, Driver=option, 5000M
        |__ Port 004: Dev 003, If 3, Class=Vendor Specific Class, Driver=option, 5000M
        |__ Port 004: Dev 003, If 4, Class=Vendor Specific Class, Driver=qmi_wwan, 5000M
```

:::hint{type="warning"}
**Stock Linux limits download speed to about 500 Mbit/s.**

All USB and network receive work for the modem runs on CPU0, a Cortex-A53 core. Under load CPU0 reaches 100% and drops about 10% of received packets, while the other cores stay almost idle.

Moving this work to the Cortex-A72 cores raised download speed from 495 Mbit/s to about 930 Mbit/s with no dropped packets. Both results come from the same 5G SA cell (n78, 100 MHz) and the same Ookla server:

```bash
sudo sysctl -w net.core.netdev_max_backlog=10000
echo 4 | sudo tee /proc/irq/32/smp_affinity_list
echo e0 | sudo tee /sys/class/net/wwu1u4i4/queues/rx-0/rps_cpus
```

These settings are lost on reboot. The IRQ number can differ: find the `xhci-hcd:usb1` line in `/proc/interrupts`. RPS must be set again if the modem re-enumerates on USB.
:::

### Interfaces and ports

All five interfaces are vendor-specific (class `ff`). The kernel driver creates one Linux device per interface:

| Interface | Class / Sub / Proto | Endpoints | Kernel driver | Linux device | Function | ModemManager role |
|:---:|---|---|---|---|---|---|
| 0 | `ff/ff/30` | 2 × bulk | `option` | `/dev/ttyUSB0` | DIAG (Qualcomm diagnostics) | ignored |
| 1 | `ff/00/40` | 2 × bulk + interrupt | `option` | `/dev/ttyUSB1` | GNSS NMEA output | `gps` |
| 2 | `ff/00/00` | 2 × bulk + interrupt | `option` | `/dev/ttyUSB2` | AT commands | `at` (primary) |
| 3 | `ff/00/00` | 2 × bulk + interrupt | `option` | `/dev/ttyUSB3` | AT commands | `at` (secondary) |
| 4 | `ff/ff/ff` (`RmNet`) | 2 × bulk + interrupt | `qmi_wwan` | `/dev/cdc-wdm0` + `wwu1u4i4` | QMI control + data network interface | `qmi` (primary), `net` |

The `ttyUSB` and `cdc-wdm` numbers depend on probe order. With two modems connected, the second modem gets `ttyUSB4`–`ttyUSB7` and `cdc-wdm1`. The network interface name follows the USB path: `wwu1u4i4` means root port 1 (the onboard hub), hub port 4, interface 4.

```text
$ mmcli -m 0
  System   |  device: /sys/devices/platform/soc/23400000.usb/xhci-hcd.0.auto/usb2/2-1/2-1.4
           | drivers: option, qmi_wwan
           |  plugin: quectel
           | primary port: cdc-wdm0
           |   ports: cdc-wdm0 (qmi), ttyUSB0 (ignored), ttyUSB1 (gps),
           |          ttyUSB2 (at), ttyUSB3 (at), wwu1u4i4 (net)
```

### Why ModemManager holds the serial ports

ModemManager's own udev rules decide the role of each port. For `2c7c:0801` they are in `/usr/lib/udev/rules.d/77-mm-quectel-port-types.rules`:

```text
ATTRS{idVendor}=="2c7c", ATTRS{idProduct}=="0801", ENV{.MM_USBIFNUM}=="00", SUBSYSTEM=="tty", ENV{ID_MM_PORT_TYPE_QCDM}="1"
ATTRS{idVendor}=="2c7c", ATTRS{idProduct}=="0801", ENV{.MM_USBIFNUM}=="01", SUBSYSTEM=="tty", ENV{ID_MM_PORT_TYPE_GPS}="1"
ATTRS{idVendor}=="2c7c", ATTRS{idProduct}=="0801", ENV{.MM_USBIFNUM}=="02", SUBSYSTEM=="tty", ENV{ID_MM_PORT_TYPE_AT_PRIMARY}="1"
ATTRS{idVendor}=="2c7c", ATTRS{idProduct}=="0801", ENV{.MM_USBIFNUM}=="03", SUBSYSTEM=="tty", ENV{ID_MM_PORT_TYPE_AT_SECONDARY}="1"
```

ModemManager opens both AT ports and keeps them open for as long as the modem is present:

- **The modem sends messages on its own.** Registration changes, incoming SMS, SIM insert or remove reports (`+QSIMSTAT`) and start-up messages (`+QUSIM`, `+QIND: PB DONE`) arrive on the AT ports at any time, so something has to read them all the time.
- **A serial port has no sharing.** Whichever process reads first gets the bytes. A second program on the same port, such as `minicom`, loses replies to ModemManager, and ModemManager loses replies to it.
- **Some features use AT only.** Most control goes over QMI, but the Quectel plugin still uses AT for SIM hot-swap detection, GNSS control and some vendor queries.

What happens if a port is taken away from ModemManager:

| Port removed | Effect |
|---|---|
| `ttyUSB3` (secondary AT) | Almost nothing. ModemManager keeps using `ttyUSB2` and QMI. |
| `ttyUSB2` and `ttyUSB3` (both AT) | Data, signal and SMS still work over QMI. SIM hot-swap detection and AT-based GNSS control stop working. Not recommended. |

### QMI

The data path uses QMI through `qmi_wwan` (USB composition `DIAG_SER_RMNET`). The module does not expose MBIM in this mode.

| Parameter | Value |
|---|---|
| Control device | `/dev/cdc-wdm0` (owner `root`, mode `0600`) |
| Network interface | `wwu1u4i4` |
| Link layer protocol | `raw-ip` (`/sys/class/net/wwu1u4i4/qmi/raw_ip` = `Y`) |
| Uplink / downlink aggregation (QMAP) | disabled |
| Multiplexing | not used (`multiplexed: no` on the bearer) |
| QMI services | `wds`, `dms`, `nas`, `qos`, `wms`, `voice`, `uim`, `pbm`, `loc`, `pdc`, `wda`, `dsd`, `sar`, and others |

Only one process can use the QMI control device at a time, and ModemManager already uses it. `qmi-proxy`, part of libqmi, shares the device between several programs. Add `--device-open-proxy` to `qmicli` so it goes through `qmi-proxy` and does not disrupt ModemManager:

```bash
sudo qmicli -d /dev/cdc-wdm0 --device-open-proxy --dms-get-revision
```

:::hint{type="warning"}
`qmi-proxy` accepts only root clients. As a normal user, `qmicli --device-open-proxy` fails with `couldn't open the QmiDevice: endpoint hangup`. Run `qmicli` with `sudo`.
:::

Per-chain receive info over standard QMI (`qmicli --nas-get-tx-rx-info=lte` or `=5gnr`) returns `NotSupported` on this firmware. Use the Quectel AT commands in [Per-antenna signal](#per-antenna-signal) instead.

### AT commands

While ModemManager is running, a terminal program on `ttyUSB2` or `ttyUSB3` gets no replies. There are three ways to send AT commands:

| Method | Data connection | Use it for |
|---|---|---|
| ModemManager in debug mode + `mmcli --command` | Drops for about 20 s each time ModemManager restarts (on and off), then stays up | QA measurements |
| Give `ttyUSB3` to another program with a udev rule | Drops once when ModemManager restarts. Not needed if the rule is in the image from boot. | Applications that need AT permanently |
| Stop ModemManager | Down until ModemManager is started again | One-off checks |

**ModemManager debug mode.** `mmcli --command` sends any AT command through ModemManager's own port queue, so it never collides with ModemManager's traffic. Without debug mode it fails with `Operation only allowed in debug mode`. Debug mode enables this for every program with root rights, so turn it off after testing.

```bash
sudo mkdir -p /etc/systemd/system/ModemManager.service.d
printf '[Service]\nExecStart=\nExecStart=/usr/sbin/ModemManager --debug\n' | sudo tee /etc/systemd/system/ModemManager.service.d/debug.conf
sudo systemctl daemon-reload
sudo systemctl restart ModemManager
sudo mmcli -m any --command='AT+QGMR'
```

To turn debug mode off:

```bash
sudo rm /etc/systemd/system/ModemManager.service.d/debug.conf
sudo systemctl daemon-reload
sudo systemctl restart ModemManager
```

**Dedicated AT port.** This rule tells ModemManager to ignore interface 3 (`ttyUSB3`) on every `2c7c:0801` modem. It matches the USB interface number, not the `ttyUSB` name, so it keeps working when several modems are connected:

```text
# /etc/udev/rules.d/78-quectel-at-ignore.rules
SUBSYSTEM=="tty", ATTRS{idVendor}=="2c7c", ATTRS{idProduct}=="0801", ATTRS{bInterfaceNumber}=="03", ENV{ID_MM_PORT_IGNORE}="1"
```

Apply it with `sudo udevadm control --reload && sudo udevadm trigger --subsystem-match=tty && sudo systemctl restart ModemManager`. Afterwards `mmcli -m any` lists the port as `ttyUSB3 (ignored)`, and any program in the `dialout` group can open it.

**Stop ModemManager.**

```bash
sudo systemctl stop ModemManager
sudo picocom -b 115200 /dev/ttyUSB2
sudo systemctl start ModemManager
```

:::hint{type="info"}
`AT+QTEMP`, `AT+QGMR`, `AT+QCFG="pcie_mbim"` and `AT+QGPSCFG` are not described in the [AT Commands Manual V1.1](https://github.com/flipperdevices/flipperone-docs/blob/public-release/docs/files/datasheets/RM520N-GL/quectel_rg520nrg525frg5x0frm5x0n_series_at_commands_manual_v1-1.pdf). Their use on this page is based on how the test unit responded.
:::

## Per-antenna signal

Software cannot test an antenna directly. The modem measures the signal on each of its four receive paths, and each path is wired to its own antenna connector. Comparing the paths shows whether an antenna is missing, damaged or badly placed.

| Command | Returns |
|---|---|
| `AT+QRSRP` | Signal strength (RSRP) on PRX, DRX, RX2, RX3, and the radio type (`LTE` or `NR5G`) |
| `AT+QRSRQ` | Signal quality (RSRQ) on each path |
| `AT+QSINR` | Signal-to-noise ratio (SINR) on each path |
| `AT+QENG="servingcell"` | Current radio type, band, channel and bandwidth |

Each reply lists the four paths in order: `+QRSRP: <PRX>,<DRX>,<RX2>,<RX3>,<sysmode>`, where `<sysmode>` is `LTE` or `NR5G`. PRX is the primary receive path. The commands work only on LTE and 5G.

Valid ranges, from the AT Commands Manual:

| Command | Range |
|---|---|
| `AT+QRSRP` | −140 to −44 dBm |
| `AT+QRSRQ` | −20 to −3 dB |
| `AT+QSINR` | −20 to 30 dB on LTE, −23 to 40 dB on 5G |

A value of `-32768` means the value is invalid for that path. Quectel describes these values as a reference only, not a receiver sensitivity test, and recommends reading them while data is being transferred, when they are more accurate.

To measure:

1. Enable AT access with one of the methods in [AT commands](#at-commands).
2. Note the band from `AT+QENG="servingcell"`.
3. Start a download, then read `AT+QRSRP`, `AT+QRSRQ` and `AT+QSINR` at least five times, a few seconds apart. Values move by a few dB between readings, so record the range, not a single number.

How to read the results:

| Result | Meaning |
|---|---|
| All paths within about 5–6 dB of each other | Antennas are connected and working. |
| One path at about −140 dBm, or `-32768`, while the others are normal | That antenna is missing, disconnected or damaged, unless the band uses fewer paths (see below). |
| Signal strength normal, SINR poor on every path | Radio environment: cell edge, interference or neighbouring cells. Not an antenna fault. |
| One path weaker and less stable than the others | Check that antenna's cable and placement. |

:::hint{type="warning"}
Check the band before you mark an antenna as faulty. Low bands (617–960 MHz, such as LTE B20 and B28) are received only on ANT0 and ANT3, so RX2 and RX3 show `-32768` there even with good antennas. Which connector each path uses depends on the band, see [What each connector does](#what-each-connector-does). Take the readings while data is flowing, as Quectel recommends.
:::

### Results on the test unit

Measured on 2026-10-20 with ModemManager in debug mode, Vodafone UK, indoors. Six readings, about 5 s apart, in each state. The B20 readings were taken while the modem was idle; the B1 readings during a download:

| Primary carrier | Path | RSRP | RSRQ | SINR |
|---|---|---|---|---|
| LTE B20 (800 MHz), EARFCN 6300, PCI 359, idle | PRX | −117 … −120 dBm | −9 … −14 dB | 0 … 5 dB |
| | DRX | −117 … −118 dBm | −9 … −13 dB | 2 … 6 dB |
| | RX2 | no value (`-32768`) | no value | no value |
| | RX3 | no value (`-32768`) | no value | no value |
| LTE B1 (2100 MHz), EARFCN 223, PCI 332, download | PRX | −120 … −122 dBm | −13 … −16 dB | −7 … 2 dB |
| | DRX | −119 … −120 dBm | −14 … −16 dB | −4 … 0 dB |
| | RX2 | −119 … −120 dBm | −13 … −16 dB | −2 … 0 dB |
| | RX3 | −118 … −120 dBm | −12 … −15 dB | 1 … 2 dB |

What this shows:

- **All four receive paths work.** On B1 all four paths are within 3 dB of each other.
- **On B20 the modem uses only two paths.** RX2 and RX3 reported no value on B20 and came back on B1. This matches the hardware: low bands are received only on ANT0 and ANT3 (see [What each connector does](#what-each-connector-does)), so it is not an antenna fault. The B20 readings were taken while idle; repeat them during a download for comparable SINR values.
- **The weak point is the signal itself.** RSRP around −120 dBm and SINR near 0 dB on every path point to the radio environment, not to one antenna. A 25 s download over this link averaged 0.38 MB/s.
- **PRX has the lowest SINR on B1** (down to −7 dB). It is still within range of the other paths, but check the main antenna cable and placement when you repeat the test.

Example replies:

```text
$ sudo mmcli -m any --command='AT+QENG="servingcell"'
response: '+QENG: "servingcell","NOCONN","LTE","FDD",234,15,2670A,359,6300,20,3,3,300B,-117,-9,-90,12,6,239,-'

$ sudo mmcli -m any --command='AT+QRSRP'
response: '+QRSRP: -121,-119,-119,-118,LTE'

$ sudo mmcli -m any --command='AT+QCAINFO'
response: '+QCAINFO: "PCC",223,75,"LTE BAND 1",1,332,-119,-15,-83,252
+QCAINFO: "SCC",6300,50,"LTE BAND 20",2,359,-117,-10,-88,3,0,-,-
+QCAINFO: "SCC",2850,100,"LTE BAND 7",1,85,-118,-12,-97,0,0,-,-'
```

How to read the `AT+QENG="servingcell"` reply for LTE:

| Field | Example | Meaning |
|---|---|---|
| state | `NOCONN` | `SEARCH`: looking for a cell. `LIMSRV`: camping, not registered. `NOCONN`: registered, idle. `CONNECT`: registered, connected. On the test unit it stayed `NOCONN` even during a download, so do not rely on it. |
| MCC, MNC | `234`, `15` | Operator (Vodafone UK) |
| cell ID | `2670A` | Cell identity, hexadecimal |
| PCI | `359` | Physical cell ID |
| EARFCN | `6300` | Channel number |
| band | `20` | LTE band |
| UL / DL bandwidth | `3`, `3` | `0` = 1.4 MHz, `1` = 3 MHz, `2` = 5 MHz, `3` = 10 MHz, `4` = 15 MHz, `5` = 20 MHz |
| TAC | `300B` | Tracking area code, hexadecimal |
| RSRP, RSRQ, RSSI | `-117`, `-9`, `-90` | Signal on the primary cell |
| SINR | `12` | Raw value. Convert with SINR = value × 2 − 20, so `12` is 4 dB. |
| CQI | `6` | Channel quality indicator, 1–30 |
| TX power | `239` | Transmit power in 0.1 dBm, so `239` is 23.9 dBm. Only meaningful while data is flowing. |
| srxlev | `-` | Cell reception level. `-` means not valid in the current state. |

When the modem has a 5G NSA link (EN-DC), the reply has three lines: `+QENG: "servingcell",<state>`, then an `"LTE"` line with the fields above, then an `"NR5G-NSA"` line with the 5G cell's PCI, RSRP, SINR, RSRQ, ARFCN, band and bandwidth.

In the `AT+QCAINFO` reply, the fields are `<freq>,<bandwidth>,<band>,<state>,<PCID>,<RSRP>,<RSRQ>,<RSSI>,<RSSNR>`. The bandwidth codes are 6 = 1.4 MHz, 15 = 3 MHz, 25 = 5 MHz, 50 = 10 MHz, 75 = 15 MHz and 100 = 20 MHz. For a secondary cell (`SCC`), the state is 0 = deconfigured, 1 = configured but deactivated, 2 = activated.

### Module temperature

`AT+QTEMP` lists the module's internal temperature sensors. During the test, with no heatsink, the module read 44–47 °C:

```text
+QTEMP:"modem-lte-sub6-pa1","44"
+QTEMP:"modem-lte-sub6-pa2","44"
+QTEMP:"cpuss-0-usr","47"
+QTEMP:"mdmss-0-usr","47"
+QTEMP:"modem-ambient-usr","46"
```

Sensors that read `0` (`modem-sdr*`) or `-273` (`modem-mmw0`, mmWave, which this module does not have) are not in use.

## Signal and cell info from ModemManager

ModemManager reads signal and cell details over QMI. These commands need `sudo`: as a normal user `--get-cell-info` is refused by ModemManager's D-Bus policy, and `--signal-setup` needs root.

**Signal.** ModemManager reads detailed signal values only after a refresh rate is set. Set it, read, and set it back to `0` when you are done:

```text
$ sudo mmcli -m any --signal-setup=5
$ sudo mmcli -m any --signal-get
  Signal |         refresh rate: 5 seconds
  LTE    |                 rssi: -87.00 dBm
         |                 rsrq: -15.00 dB
         |                 rsrp: -120.00 dBm
         |                  s/n: -5.80 dB
  5G     |                 rsrq: -20.00 dB
         |                 rsrp: -115.00 dBm
         |                  s/n: -3276.80 dB
$ sudo mmcli -m any --signal-setup=0
```

A value of `-3276.80` means "no value". ModemManager passes it through without filtering it.

**Cell info.** Lists the serving cell and the neighbour cells the modem can see:

```text
$ sudo mmcli -m any --get-cell-info
  Cell info | cells:
            |        cell type: lte, serving: no, physical ci: 55, earfcn: 2850, rsrp: -120.700000, rsrq: -13.600000
            |        cell type: lte, serving: no, physical ci: 32, earfcn: 223, rsrp: -122.600000, rsrq: -18.200000
            |        cell type: lte, serving: no, physical ci: 14C, earfcn: 223, rsrp: -119.000000, rsrq: -15.300000
            |        cell type: lte, serving: yes, operator id: 23415, tac: 300B, ci: 2670A, physical ci: 167, earfcn: 6300, rsrp: -117.600000, rsrq: -12.800000, timing advance: 5
```

`physical ci`, `tac` and `ci` are hexadecimal. For example, `physical ci: 167` is PCI 359.

## GNSS

The GNSS receiver sends NMEA sentences on `ttyUSB1` once GNSS is started. ModemManager can start it in three ways. Only one works with this firmware:

| ModemManager mode | Result |
|---|---|
| `--location-enable-gps-raw` | Fails: `Couldn't not register tracking events: QMI protocol error (48): 'InvalidArgument'` |
| `--location-enable-gps-nmea` | Fails with the same error |
| `--location-enable-gps-unmanaged` | Works. ModemManager starts GNSS and leaves `ttyUSB1` free for other programs. |

In `gps-unmanaged` mode ModemManager does not read the NMEA port, so read the sentences from `ttyUSB1` directly.

To test GNSS:

1. Start GNSS:
   ```bash
   sudo mmcli -m any --location-enable-gps-unmanaged
   ```
2. Put the port in raw mode and read it. Without `raw -echo` the terminal echoes data back to the modem and the output is garbled.
   ```bash
   sudo stty -F /dev/ttyUSB1 raw -echo
   sudo cat /dev/ttyUSB1
   ```
3. Stop GNSS when you are done:
   ```bash
   sudo mmcli -m any --location-disable-gps-unmanaged
   ```

What to look for in the output:

| Sentence | No fix | Fix |
|---|---|---|
| `$GPGGA` | 7th field `0` | 7th field `1` or higher, with latitude, longitude and the number of satellites |
| `$GPRMC` | 3rd field `V` | 3rd field `A`, with UTC time and date |
| `$GPGSA` | 3rd field `1` | 3rd field `2` (2D) or `3` (3D) |

### GNSS results on the test unit

Logged for 5 minutes on 2026-10-20, indoors, cold start:

- **The GNSS engine starts.** `ttyUSB1` sent 1205 sentences: `$GPGGA`, `$GPRMC`, `$GPVTG` and `$GPGSA` once per second. They stop as soon as GNSS is disabled.
- **No fix and no satellites.** Every sentence stayed empty (`$GPGGA,,,,,,0,,,,,,,,*66`, `$GPRMC,,V,…`), and the receiver never reported a UTC time either.
- **Only GPS sentences (`$GP`) are sent.** There are no satellites-in-view sentences (`GSV`), and none for GLONASS, BeiDou or Galileo. This depends on the module's NMEA output settings (`AT+QGPSCFG`), which were not checked.

GNSS L1 is received on ANT3 and L5 on ANT1 (see [What each connector does](#what-each-connector-does)). Not yet checked: whether the antenna on ANT3 covers 1559–1609 MHz, and a test outdoors with a clear view of the sky. Repeat the test outdoors before you mark GNSS as working or broken.

## rfkill switches

Flipper One has two rfkill switches for the M.2 slot. Each one drives one of the M.2 disable lines through a GPIO:

```text
$ rfkill -o ID,TYPE,DEVICE,SOFT,HARD
ID TYPE DEVICE                    SOFT      HARD
 0 wlan Onboard WiFi+BT        blocked unblocked
 1 wwan M.2 WWAN             unblocked unblocked
 2 wwan M.2 WWAN (WDISABLE2) unblocked unblocked
```

| rfkill device | M.2 signal | GPIO | What the RM520N-GL does when blocked |
|---|---|---|---|
| `M.2 WWAN` (ID 1) | `W_DISABLE1#`, pin 8 | `gpio2 PB4` | Airplane mode: cellular radio off |
| `M.2 WWAN (WDISABLE2)` (ID 2) | `W_DISABLE2#`, pin 26 | `gpio4 PA0` | GNSS off. Cellular keeps working. |

Blocking a switch drives its line LOW, unblocking drives it HIGH. Both lines are active LOW and pulled up inside the module (section 4.4 of the [hardware design guide](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6382/Quectel_RM520N_Series_Hardware_Design_V1.3.pdf)).

### Test results

Tested on 2026-10-21 with Ethernet as the default route, so the test did not cut off the SSH session.

**W_DISABLE1# (`sudo rfkill block 1`):**

1. NetworkManager reported `rfkill: WWAN now disabled by radio killswitch` and had ModemManager disable the modem. Within 1 s the modem was in low-power mode and detached, and the data link was down.
2. While the line was LOW, `sudo mmcli -m any --enable` failed with `Couldn't set operating mode: QMI protocol error (4): 'Aborted'`. The module itself keeps the radio off, as the hardware design guide describes.
3. After `sudo rfkill unblock 1`, the modem registered within 2 s and the data connection was back after 3 s, with a new IP address.

**W_DISABLE2# (`sudo rfkill block 2`), with GNSS running:**

1. NMEA output on `ttyUSB1` stopped.
2. NetworkManager also reported `WWAN now disabled by radio killswitch` and disabled cellular data, although this line only controls GNSS.
3. While the line was LOW, `sudo mmcli -m any --enable` worked and the modem registered on LTE and 5G NR, so the line does not affect the cellular radio. GNSS stayed silent even after it was started again.
4. After `sudo rfkill unblock 2`, cellular data was back within 7 s. GNSS did not restart by itself.

### rfkill known issues

- **The GNSS switch also turns off cellular data.** Both switches are registered with rfkill type `wwan`, so NetworkManager treats either one as a cellular kill switch. Registering the W_DISABLE2 switch as type `gps` (`radio-type = "gps"` in the device tree node `rfkill-m2-wdisable2`) should stop this. Not tested yet.
- **GNSS does not recover after W_DISABLE2# is released.** ModemManager still lists `gps-unmanaged` as enabled, but no NMEA arrives, and `--location-disable-gps-unmanaged` fails with `Unknown mobile equipment error: 505`. Restarting ModemManager fixes it: `sudo systemctl restart ModemManager`, then `sudo mmcli -m any --location-enable-gps-unmanaged`. Cellular drops for about 20 s during the restart.

### Ways to turn the cellular radio off

| Control | Command | What it does |
|---|---|---|
| NetworkManager WWAN radio | `nmcli radio wwan off` | NetworkManager tells ModemManager to disable the modem. |
| ModemManager | `sudo mmcli -m any --disable` | Puts the modem in low-power mode. The modem stays on USB. |
| rfkill | `sudo rfkill block 1` | Drives `W_DISABLE1#` LOW. The module cannot turn the radio on until the line is released. NetworkManager also disables WWAN. |

## Multiple modems

ModemManager numbers modems in the order it finds them (`Modem/0`, `Modem/1`, …). The number changes when a modem is reset, re-plugged or switches SIM slot. Scripts and apps should use a stable identifier instead:

| Identifier | Where to read it | Stays the same when |
|---|---|---|
| Device (UID) | `mmcli -m 0 -K` → `modem.generic.device` | The modem stays in the same M.2 slot |
| Custom UID | Set with the `ID_MM_PHYSDEV_UID` udev property | You name each slot yourself |
| Device identifier | `modem.generic.device-identifier` | The same modem and firmware are reconnected |
| IMEI | `modem.generic.equipment-identifier` | Always, it belongs to the module |
| Network interface | `ip link`, e.g. `wwu1u4i4` | The modem stays in the same M.2 slot |

`mmcli -m` accepts the UID as well as the index. For a NetworkManager connection that must always use the same modem, set `gsm.device-id` or `gsm.sim-id` on the connection.

## PCIe mode

By default the modem uses USB. It can also send data over PCIe: the M.2 slot carries one PCIe 2.1 lane. That lane uses the same pins as SATA, so PCIe is not available when the SATA overlay (`rk3576-flipper-one-sata.dtbo`) is enabled.

:::hint{type="warning"}
On the current kernel, data over PCIe works only after the runtime workaround below. Without it the modem registers on the network, but the data connection hangs in `connecting`.
:::

### Switch to PCIe

1. Enable [ModemManager debug mode](#at-commands) to send AT commands.
2. Move the data path to PCIe and enable MBIM over PCIe. Diagnostics stay on USB.
   ```bash
   sudo mmcli -m any --command='AT+QCFG="data_interface",1,0'
   sudo mmcli -m any --command='AT+QCFG="pcie_mbim",1'
   ```
3. Restart the modem:
   ```bash
   sudo mmcli -m any --command='AT+CFUN=1,1'
   ```
4. Reboot Flipper One. The PCIe controller only looks for devices at boot and cannot rescan later.

:::hint{type="warning"}
Quectel's AT Commands Manual does not recommend `AT+CFUN=1,1` while the modem uses PCIe, because it can break the PCIe start-up sequence. It recommends a hardware reset, with the host and the module restarted together. On the test unit `AT+CFUN=1,1` followed by a host reboot worked. Firmware updates are not supported over PCIe after an `AT+QCFG="data_interface"` switch: switch back to USB before updating.
:::

Both settings are saved automatically and take effect after the module restarts. With `data_interface 1,0`, AT commands are available on both USB and PCIe. The defaults on the test unit were `data_interface 0,0`, `pcie_mbim 0` and `pcie/mode 0` (PCIe endpoint mode, which is correct for Flipper One; `1` is root-complex mode).

To switch back to USB, use the same AT commands with ModemManager in debug mode. The USB AT ports are still available in PCIe mode.

1. Restore the defaults:
   ```bash
   sudo mmcli -m any --command='AT+QCFG="data_interface",0,0'
   sudo mmcli -m any --command='AT+QCFG="pcie_mbim",0'
   ```
2. Detach the PCIe device, so the driver does not hang on a link that is about to disappear:
   ```bash
   echo 1 | sudo tee /sys/bus/pci/devices/0000:01:00.0/remove
   ```
3. Restart the modem. If the command fails with `Resource temporarily unavailable`, wait a few seconds and run it again.
   ```bash
   sudo mmcli -m any --command='AT+CFUN=1,1'
   ```

No reboot is needed to go back: USB devices are detected at any time. On the test unit the modem came back on USB with `qmi_wwan` and reconnected about 50 s after the restart.

### What the system shows

```text
$ lspci -nn
01:00.0 Unassigned class [ff00]: Qualcomm Technologies, Inc SDX62 [Snapdragon X62 5G] [17cb:0308]

$ sudo dmesg | grep pcie
rockchip-dw-pcie 22000000.pcie: PCIe Gen.2 x1 link up
```

| Parameter | Value |
|---|---|
| PCI ID | `17cb:0308`, subsystem `17cb:5201` |
| Link | 5 GT/s (Gen 2) ×1, limited by Flipper One's single PCIe 2.1 lane. The specification lists PCIe 3.0 ×1; the module advertises 16 GT/s ×2 in its link capabilities. |
| Kernel driver | `mhi-pci-generic` (MHI bus) |

In PCIe mode the modem still shows up on USB, but only with four interfaces: DIAG, NMEA (`ttyUSB1`) and two AT ports. The USB data interface (`qmi_wwan`) is gone.

### Driver workaround

The kernel's `mhi-pci-generic` driver picks a channel layout by PCI ID. It knows the RM520N-GL only by Quectel's IDs (`1eac:1004`, `1eac:1007`). This module reports Qualcomm's generic ID, so the driver uses the generic `qcom-sdx65m` profile. That profile hands the data channel to the raw-IP driver (`mhi_net`), while the modem sends MBIM-framed data, which only `mhi_wwan_mbim` understands.

Until the kernel has this ID, add it to the Quectel profile at runtime and rebind the modem. This lasts until the next reboot:

```bash
D=/sys/bus/pci/drivers/mhi-pci-generic
A=$(sudo awk '$3=="mhi_quectel_rm5xx_info"{print $1}' /proc/kallsyms)
echo "17cb 0308 17cb 5201 0 0 $A" | sudo tee $D/new_id
echo 0000:01:00.0 | sudo tee $D/unbind
echo 0000:01:00.0 | sudo tee $D/bind
```

A kernel patch can add the same entry (`PCI_DEVICE_SUB(PCI_VENDOR_ID_QCOM, 0x0308, PCI_VENDOR_ID_QCOM, 0x5201)` with `mhi_quectel_rm5xx_info`) to `drivers/bus/mhi/host/pci_generic.c`. OpenWrt carries this patch for the RM520N-GL in the GL.iNet GL-X3000, and it was sent upstream in July 2025, but it is not in mainline. The subsystem vendor is Qualcomm's own ID, so other SDX62 modules may report the same ID; treat the patch as a local workaround until Quectel or the MHI maintainers confirm it.

### Interfaces with the Quectel profile

| Linux device | Function | ModemManager role |
|---|---|---|
| `/dev/wwan0mbim0` | MBIM control | `mbim` (primary) |
| `/dev/wwan0at0` | AT commands | `at` |
| `/dev/wwan0qcdm0` | Qualcomm diagnostics | ignored |
| `wwan0` | Data network interface (`mhi_wwan_mbim`) | `net` |

The NMEA channel fails to start (`mhi_wwan_ctrl mhi0_NMEA: probe with driver mhi_wwan_ctrl failed with error -95`). GNSS NMEA is still available on the USB port `ttyUSB1`.

### PCIe results on the test unit

Measured on 2026-10-20 with Vodafone UK, indoors, the same weak signal as the USB tests:

| Test | Result |
|---|---|
| Data connection | Connected, `wwan0` got an IPv4 address |
| Ping 1.1.1.1 | 4/4 replies, 30–44 ms |
| 25 s download | 0.42 MB/s (USB: 0.38 MB/s). Limited by the signal, not the bus. |
| Per-antenna AT commands | Work. `AT+QRSRP` reported an `NR5G` measurement. |

### Known issues

- **ModemManager lists the modem twice.** One entry uses PCIe (MBIM, `wwan0at0`), the other the leftover USB AT ports. Both control the same radio. Ignoring the USB ports in PCIe mode needs a udev rule, which has not been tested yet.
- **Check which interface is the default route.** On the test unit the cellular connection had `ipv4.route-metric 100`, lower than Ethernet's 101, so all traffic went over cellular, in USB and PCIe mode alike. Any cellular test then also cuts off the SSH session. Set the cellular route metric higher, for example `sudo nmcli connection modify cellular-vodafone-uk ipv4.route-metric 700 ipv6.route-metric 700`, then restart the connection with `nmcli connection down` and `up`. `nmcli device reapply` left the interface without an IP address on the test unit.

## Software stack

The test ran with the following versions:

| Component | Version |
|---|---|
| OS | Debian GNU/Linux 13 (trixie) |
| Kernel | `7.3.0-rc7` (Flipper One build 1243) |
| ModemManager | 1.24.0 |
| NetworkManager | 1.52.1 |
| libqmi (`qmicli`) | 1.36.0 |

## Connect to the network

Create a NetworkManager connection for your carrier's APN. This example uses Vodafone UK:

```bash
sudo nmcli connection add type gsm ifname '*' con-name cellular-vodafone-uk apn wap.vodafone.co.uk
sudo nmcli connection modify cellular-vodafone-uk connection.autoconnect yes
sudo nmcli connection up cellular-vodafone-uk
```

Check that the connection is up:

```text
$ nmcli device status
DEVICE    TYPE      STATE      CONNECTION
cdc-wdm0  gsm       connected  cellular-vodafone-uk

$ mmcli -b 0
  Status             |      connected: yes
                     |    multiplexed: no
                     |      interface: wwu1u4i4
  Properties         |            apn: wap.vodafone.co.uk
                     |        ip type: ipv4v6
  IPv4 configuration |         method: static
                     |        address: 10.206.200.114
                     |         prefix: 30
                     |            mtu: 1500
```

## Radio state during the test

Measured on 2026-10-20 with Vodafone UK, indoors:

| Parameter | Value |
|---|---|
| Registration | home, Vodafone UK (MCC 234, MNC 15) |
| Access technology | LTE (5G NSA available on the cell, no stable NR link) |
| Primary cell | LTE B1, EARFCN 223, 15 MHz |
| Secondary cell | LTE B20, EARFCN 6300, 10 MHz (activated) |
| Configured secondary cell | LTE B7, EARFCN 2850, 20 MHz (deactivated) |
| LTE RSSI | −75 dBm |
| LTE RSRP | −121 dBm |
| LTE RSRQ | −20 dB |
| LTE SNR | −10.0 dB |
| IMS voice support | yes (VoLTE carrier config loaded) |

:::hint{type="warning"}
The LTE signal was very weak during this test (RSRP −121 dBm, SNR −10 dB). This is probably why the modem stayed on LTE and did not keep a 5G NR link. Repeat the 5G test with better antenna placement or closer to a window.
:::

## Useful commands

`qmicli` and the `mmcli` signal and cell commands need `sudo`.

| Task | Command |
|---|---|
| List modems | `mmcli -L` |
| Modem summary | `mmcli -m any` |
| Signal (LTE and 5G) | `sudo mmcli -m any --signal-setup=5`, then `sudo mmcli -m any --signal-get` |
| Serving and neighbour cells | `sudo mmcli -m any --get-cell-info` |
| Firmware version | `sudo qmicli -d /dev/cdc-wdm0 --device-open-proxy --dms-get-revision` |
| Supported bands | `sudo qmicli -d /dev/cdc-wdm0 --device-open-proxy --dms-get-band-capabilities` |
| Active band | `sudo qmicli -d /dev/cdc-wdm0 --device-open-proxy --nas-get-rf-band-info` |
| Carrier aggregation | `sudo qmicli -d /dev/cdc-wdm0 --device-open-proxy --nas-get-lte-cphy-ca-info` |
| 5G NSA availability | `sudo qmicli -d /dev/cdc-wdm0 --device-open-proxy --nas-get-system-info` |
| SIM status | `sudo qmicli -d /dev/cdc-wdm0 --device-open-proxy --uim-get-card-status` |
| Data format | `sudo qmicli -d /dev/cdc-wdm0 --device-open-proxy --wda-get-data-format` |
| rfkill state | `rfkill` |
