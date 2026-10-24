---
title: 5G Modem app
slug: cpu-software/flipctl/5g-modem-app
docTags: 
createdAt: Sat Oct 24 2026 00:00:00 GMT+0000 (Coordinated Universal Time)
updatedAt: Sat Oct 24 2026 00:00:00 GMT+0000 (Coordinated Universal Time)
---

The 5G Modem app is FlipCTL's built-in screen for cellular modems. It lives in **Network → 5G Modem** and shows everything the modem reports about the network, the signal and the connection, down to each antenna, and lets you turn the radio off and switch between the physical SIM and the Flipper eSIM.

It is built for two kinds of users: the QA team, who test modems and antennas and need real measurements, and owners, who need to see at a glance whether they have service and how good it is.

This page is the requirements and the plan for the app. Each chapter describes one screen: what it shows, how it behaves, and the technical background behind it.

:::hint{type="info"}
**Status.** A working prototype runs on a Flipper One with a [Quectel RM520N-GL](../../testing/RM520N-GL.md). Every screenshot on this page is a real frame from it, rendered from the device's own data. Identifiers (IMEI, ICCID, IMSI, phone number, IP addresses) are replaced with placeholders. What is not done yet is listed in [Plan](#plan).
:::

***

## Design principles

- **ModemManager owns the modem, NetworkManager owns the connection.** FlipCTL does not talk to the modem itself. It reads ModemManager (MM) over D-Bus and asks it to change things. No second modem manager, no QMI, no direct use of the modem's serial ports. The one exception is per-antenna signal, which MM can only pass through as AT commands, see [Per-antenna measurements](#per-antenna-measurements).
- **No processes.** FlipCTL starts no `mmcli`, `qmicli` or `nmcli` for this app. Everything comes from D-Bus, sysfs and kernel device files.
- **Told, not asked.** MM announces every change on D-Bus, and FlipCTL redraws when it does. Nothing is polled while nothing is on screen. Detailed signal and cell info, which MM only reads when asked, are asked for only while a screen shows them.
- **A modem is known by where it is plugged in.** MM numbers modems in the order it finds them, and the number changes on every reset, SIM switch and replug. FlipCTL names a modem by its port instead, so a screen keeps showing the same modem through a restart.
- **Only what the modem really reports.** No guessed values. When something is not available, the screen says so in words rather than showing an empty field.

***

## Network menu

::Image[]{src="/files/pics/cpu-software/5g-modem-network-menu.png" size="60" width="768" height="432" position="center" caption="Network menu with one modem: the entry shows the operator"}

The **5G Modem** entry in the Network menu shows the state of cellular on the right, like the Wi-Fi entry does, so you can see it without opening the app.

| Shown | When |
|---|---|
| `No modem` | No modem is installed |
| `Disabled` | The radio is switched off with the [radio switch](#radio-switch) |
| `No SIM` | The modem has no SIM card, or the selected card does not answer |
| `SIM locked` | The SIM needs a PIN |
| `Off` | MM has the modem disabled for another reason, for example NetworkManager's WWAN radio is off |
| `Connecting...` | The modem is starting, searching, registering or connecting |
| `No service` | The modem is on but not registered on any network |
| Operator name, e.g. `vodafone UK` | Connected. When the network sends no name: MCC/MNC, e.g. `234/15` |

The first row that matches wins, top to bottom. The status bar shows the same modem's network (`3G`, `4G`, `5G`, `5G+`) and signal bars, with the same strength as the app (see [Signal bars and percentage](#signal-bars-and-percentage)).

### Several modems

Flipper One can have more than one modem at a time: one in the M.2 slot and more on USB, for example for load balancing between operators.

- **With no modem or one modem** there is a single **5G Modem** entry, as in the screenshot.
- **With more than one**, every modem gets its own **5G Modem** entry, and only then does each entry show where its modem is plugged in:

```
Network
  5G Modem  M.2 ............ vodafone UK
  5G Modem  USB-A ................ No SIM
  5G Modem  USB-C2 ............... No SIM
```

When the count drops back to one, the remaining entry loses its port name again.

| Name | Port |
|---|---|
| `M.2` | The M.2 slot (onboard USB hub, port 4) |
| `USB-A` | The USB-A port (hub port 2) |
| `USB-C2` | The second USB-C port (hub port 3) |
| `USB-C1` | The charging and DisplayPort USB-C port (the other USB controller) |

A modem behind an external hub keeps the name of the Flipper port the hub is plugged into. Two modems on one hub get the hub's port number after it: `USB-A 1`, `USB-A 4`. The entries are in this order: M.2 first, then USB-A, USB-C1, USB-C2.

Which modem carries the traffic is NetworkManager's job (route metrics, and `gsm.device-id` or `gsm.sim-id` on each connection). The app shows each modem's connection but does not choose between them.

### Technical background: how a modem is identified

- **By port, not by MM index.** The name comes from the modem's USB device in sysfs, which MM reports as `Physdev`. The bus number is left out, so the same port has the same name whether the modem runs at USB 3 (`2-1.4`) or USB 2 (`1-1.4`). The port table is this board's, from the device tree.
- **A PCIe modem is in the M.2 slot**, since that is the only PCIe lane.
- **One IMEI is one modem.** In PCIe mode MM lists the RM520N-GL twice, once for each side. The app shows it once.
- **Restarts are followed.** When a modem disappears from under an open screen (a reset, a SIM switch), the screen shows `Restarting modem` and picks the modem up again when it comes back in the same port, as a new MM object.
- **One D-Bus connection for everything.** A single watcher reads every modem with one `GetManagedObjects` call (about 7 ms on the device) and reads again when MM signals a change. The menu entries, the status bar and every page of the app read from it.

***

## Main screen

::Image[]{src="/files/pics/cpu-software/5g-modem-main.png" size="60" width="768" height="432" position="center" caption="Main screen, first item selected: Info and Config on the soft keys"}

The main screen has four items. Up and down move the cursor between them, and a block of several lines is one item, framed as one.

| Item | What it shows | Ok | Info |
|---|---|---|---|
| 1. **5G Modem** | The modem's name in grey, and the radio switch, `ON` or `OFF` | Turns the radio on or off | Opens [Device info](#device-info) |
| 2. **SIM Card** | Which card is in use: `Physical` or `Flipper eSIM` | Opens [SIM card](#sim-card) | Opens [SIM card](#sim-card) |
| 3. Operator and signal | Operator, phone number, network, signal bars, RSRP and SNR | Opens [Verbose signal info](#verbose-signal-info) | — |
| 4. Data connection | IPv4, IPv6, APN, download and upload speed | Opens [Data connection](#data-connection-page) | — |

**Soft keys:** `Back` on Escape. `Info` on View, which is the help key in FlipCTL, shown only when the cursor is on item 1 or 2. `Config` on Edit, which opens [Config](#config). Back on any page returns to the main screen.

Special states:

- **No modem installed:** `No modem found` in the middle of the screen.
- **Modem restarting** (after a reset or a SIM switch): `Restarting modem` until it is back, about a minute.
- **Radio off:** only items 1 and 2. The SIM item stays, because switching cards does not need the radio.
- **A USB modem** has no radio switch and no SIM selector: those belong to the M.2 slot. Its SIM item says `SIM`.

### Technical background: layout

- The panel is 256 × 144 pixels. The four items take 1 + 1 + 3 + 3 rows of 12 pixels: 96 of the 102 pixels between the breadcrumb and the soft keys. The screen fits without scrolling but has no spare room; a fourth line in either block would make it scroll.
- The panel's fonts are printable ASCII only. That is why the screen says `Down` and `Up`, not arrows, and cuts long text with `..`.
- Every position on the screen is computed in Rust (`flipper_ui::modem::main_view`) and unit-tested, including that every line clears its neighbour. The Slint component only draws.

### Radio switch

Item 1 turns the modem's radio off and on. `OFF` is a hardware switch: the modem cannot transmit until it is turned back on, whatever any software asks.

What happens, as tested on the RM520N-GL:

- **Off:** the modem turns its radio off within a second. NetworkManager sees the switch and has MM disable the modem, and the data connection goes down. The modem stays on USB: its name, firmware, IMEI and SIM details are still shown.
- **On:** the modem registered on the network within 2 seconds and the data connection was back after 3 seconds.

:::hint{type="warning"}
The modem cannot be turned on from software while the switch is off: MM's own `Enable` fails with `QMI protocol error (4): 'Aborted'`. Only the switch turns it back on.
:::

**Technical background.** The switch is the M.2 slot's **W_DISABLE1#** line, which the kernel exposes as the rfkill switch `M.2 WWAN`.

- FlipCTL finds the switch by its name in `/sys/class/rfkill`, since rfkill numbers depend on probe order, and writes one `RFKILL_OP_CHANGE` event to `/dev/rfkill`. The `ON`/`OFF` on screen is read back from sysfs, so it is always what the kernel has.
- **Permission:** a udev rule gives `/dev/rfkill` to an `rfkill` group, and FlipCTL's service runs in that group. The HDMI desktop on seat0 keeps its own access to the radio switches.
- The second M.2 line, **W_DISABLE2#** (`M.2 WWAN (WDISABLE2)`), only turns GNSS off and is not in this app. Until its device-tree fix registers it as type `gps`, NetworkManager treats it as a cellular switch too; see [rfkill switches](../../testing/RM520N-GL.md#rfkill-switches).

### SIM item

Shows which card the modem is using: `Physical` (the SIM tray) or `Flipper eSIM` (the eSIM chip on the board). Ok or Info opens [SIM card](#sim-card), where you can switch.

### Operator and signal

::Image[]{src="/files/pics/cpu-software/5g-modem-main-signal.png" size="60" width="768" height="432" position="center" caption="The operator and signal block selected"}

- **Left:** the operator's name as the network sends it, with `(roaming)` when roaming. Under it, the SIM's phone number when the SIM stores one. Many SIMs do not, and then the line stays empty.
- **Right, first line:** the network, six signal bars and the signal strength in percent.
- **Right, second line:** RSRP, the signal strength in dBm, with a word: `weak`, `good` or `excellent`.
- **Right, third line:** SNR, the signal quality in dB, with a word: `poor`, `good` or `excellent`.

On 3G the two lines are RSCP and Ec/Io instead.

#### Network names

| Network | Shown | On the signal page |
|---|---|---|
| 5G standalone | `5G+` | `5G SA (Standalone 5G+)` |
| 5G non-standalone | `5G` | `5G NSA (5G + 4G LTE core)` |
| LTE | `4G` | `4G (LTE)` |
| HSPA+ | `3G` | `3G HSPA+ (WCDMA)` |
| HSPA | `3G` | `3G HSPA (WCDMA)` |
| UMTS | `3G` | `3G UMTS (WCDMA)` |

`5G+` for standalone 5G follows the iPhone. The RM520N-GL has no 2G.

MM reports 5G NSA as LTE and 5G together, and drops 5G from the list whenever the 5G leg is not active. On a weak or idle 5G link the label therefore moves between `5G` and `4G`. This is what the modem is doing, so the screen shows it as it is.

#### Signal bars and percentage

The bars and the percentage are computed from **RSRP**, on a straight line from **-125 dBm = 0%** to **-75 dBm = 100%**. Each of the six bars is about 8 dB. -125 dBm is about where an LTE link stops working; -75 dBm is as good as it gets in practice. The status bar's five bars use the same percentage, so the two always agree.

Why RSRP and not MM's own signal quality:

- RSRP is the power of the cell's reference signal, the number 3GPP defines for LTE and 5G signal strength. It does not change with the channel bandwidth or with how busy the cell is.
- MM's own `SignalQuality` follows RSSI: everything received in the channel, including neighbouring cells, noise and the cell's own traffic. It goes up when the cell gets busier, which says nothing about the antenna or the position.

In **5G NSA the bars follow the 4G link**. In NSA, LTE is much more than a login: it carries all the signalling (connection setup, handovers, registration with the 4G core), voice calls, often the upload and part of the download. If 4G drops, 5G drops with it; a weak 5G link only makes data slower. Both radios' values are on the signal page.

When there is no RSRP yet (for example right after the modem appears), MM's own percentage stands in.

#### The words

| | weak / poor | good | excellent |
|---|---|---|---|
| RSRP | below -105 dBm | -105 to -90 dBm | -90 dBm and above |
| SNR | below 10 dB | 10 to 20 dB | 20 dB and above |

These are the usual LTE steps, used for 5G as well.

**Technical background.** MM reads detailed signal (RSRP, RSRQ, RSSI, SNR) only after `Signal.Setup(rate)`. FlipCTL sets a 10-second rate on every modem as it appears, so the status bar always has an RSRP to work from, and a 2-second rate while the app is open. MM reports a missing value as `-3276.8`; FlipCTL shows `-` for it.

### Data connection

::Image[]{src="/files/pics/cpu-software/5g-modem-main-data.png" size="60" width="768" height="432" position="center" caption="The data connection block selected"}

- **Left:** the IPv4 address, the IPv6 address when the connection has one, and the APN. A long IPv6 address is cut with `..`; the full one is on the [Data connection](#data-connection-page) page.
- **Right:** the current download and upload speed, updated every second.
- **No connection:** `Not connected`.

**Technical background.** The addresses and the APN come from MM's bearer, the object for the active connection, so no NetworkManager call is needed. The speeds are computed from the interface's own byte counters in `/sys/class/net/<interface>/statistics`, read a second apart while the app is open.

***

## Device info

Opened with **Info** on the first item.

::Image[]{src="/files/pics/cpu-software/5g-modem-device.png" size="60" width="768" height="432" position="center" caption="Device info"}

::Image[]{src="/files/pics/cpu-software/5g-modem-device-2.png" size="60" width="768" height="432" position="center" caption="Device info, scrolled: ports and their roles"}

| Line | Meaning |
|---|---|
| Manufacturer, Model | As the modem reports them |
| Firmware | The firmware revision, e.g. `RM520NGLAAR03A04M4G` |
| Hardware | The hardware revision |
| IMEI | The modem's identity on the network |
| Connected | How the modem is attached: `USB 3, M.2`, `USB 2, USB-A`, or `PCIe` |
| Carrier config, Config version | The operator profile (MBN) the modem selected from the SIM |
| MM plugin | The ModemManager plugin that handles the modem, e.g. `quectel` |
| Primary port | The port MM controls the modem through, e.g. `cdc-wdm0` |
| Drivers | Kernel drivers bound to the modem, e.g. `option, qmi_wwan` |
| Ports | Every port and the role MM gives it: `qmi`, `at`, `gps`, `net`, `ignored` |

**Technical background.** All of it is MM's `Modem` properties, read in the same call as everything else. The USB speed comes from sysfs (`5000` is USB 3, `480` is USB 2).

***

## SIM card

Opened with **Ok** or **Info** on the SIM item.

::Image[]{src="/files/pics/cpu-software/5g-modem-sim.png" size="60" width="768" height="432" position="center" caption="SIM card, with the cursor on the switch"}

- **The first line switches the card:** `Switch to eSIM`, or `Switch to physical SIM` while the eSIM is in use. The cursor is on it; Ok asks first:

  ```
  Switch to Flipper eSIM?
  The modem restarts
           [Cancel]  [Switch]
  ```

  After Switch, the app returns to the main screen, which shows `Restarting modem` for about a minute until the modem is back on the new card.
- **Then the card's details:** which card is in use, PIN status (`Not required`, `PIN required`, `PUK required`), PIN and PUK tries left, ICCID, IMSI, the operator code the SIM belongs to, the eSIM's EID when it has one, and the phone number when the SIM stores one.

The switch line is only on the M.2 modem, the one behind the board's SIM selector. A USB modem's SIM page shows the details only.

### Technical background: the SIM selector

The physical SIM tray and the Flipper eSIM chip share the modem's SIM 1 lines through an analog switch on the board. One GPIO drives it: `sim_sel`, GPIO1_C0, set high at boot by the device tree. The modem itself sees one SIM slot either way.

| | |
|---|---|
| **High** (boot default) | Physical SIM |
| **Low** | Flipper eSIM |
| **Does the modem notice a switch by itself?** | No. 30 seconds after switching, MM still showed the old card. The modem reads the card again only when it restarts |
| **So switching is** | set the GPIO, then MM's `Reset()` |
| **How long** | About 60 seconds from the reset until MM lists the modem again |

- FlipCTL talks to the kernel's GPIO character device directly (the v2 line API), with no libgpiod and no processes. It finds the chip by its controller address (`2ae10000.gpio`), since chip numbers depend on probe order.
- **It never requests the line as an input.** A read requests the line "as is". As an input the switch would float and drop the SIM.
- The line keeps its level after the request ends, so FlipCTL sets it and lets go rather than holding it for as long as it runs.
- **Permission:** FlipCTL's service already runs in the `gpio` group, which owns `/dev/gpiochip*`. MM allows `Reset()` to FlipCTL's session.

:::hint{type="warning"}
The eSIM chip on current boards is empty. Selecting it ends in `No SIM`: the modem does not see the empty chip as a card at all. Production units will ship with a provisioned eSIM, so the app does not need to download profiles. This should be checked again with a provisioned eSIM.
:::

***

## Verbose signal info

Opened with **Ok** on the operator and signal block. A long page; up and down scroll it.

::Image[]{src="/files/pics/cpu-software/5g-modem-signal-0.png" size="60" width="768" height="432" position="center" caption="Network, operator, bands and the serving cell"}

::Image[]{src="/files/pics/cpu-software/5g-modem-signal-8.png" size="60" width="768" height="432" position="center" caption="Each radio's signal values, and the neighbour cells"}

::Image[]{src="/files/pics/cpu-software/5g-modem-signal-14.png" size="60" width="768" height="432" position="center" caption="Per-antenna measurements, by connector"}

| Section | Contents |
|---|---|
| Top | Network (`4G (LTE)`, `5G NSA (5G + 4G LTE core)`, ...), operator, and the bands in use |
| Serving cell | Band, channel number, PCI, cell ID, TAC |
| 4G, 5G, 3G | Each radio that has values: RSRP, RSRQ, RSSI and SNR (RSCP, Ec/Io and RSSI on 3G) |
| Neighbour cells | One line per cell the modem can hear: band, PCI and RSRP |
| Antennas | The per-antenna measurements, see below |

### Cells and bands

**Technical background.**

- Cells come from MM's `GetCellInfo()`, asked every 5 seconds while the app is open. It lists the serving cell and the neighbours, with PCI, cell ID and TAC as hex strings, which the page converts.
- **MM does not report the band.** It reports the serving cell's channel number: EARFCN on 4G, NR-ARFCN on 5G, UARFCN on 3G. FlipCTL works out the band and its frequency name (`B20 800 MHz`, `n78 3500 MHz`) from the 3GPP tables (TS 36.101, 38.104 and 25.101). Where 5G bands overlap, the band more networks use wins: n78 before n77, n1 before n66.
- **In 5G NSA** the page shows both bands, `B1 2100 MHz + n78 3500 MHz`, when MM lists the 5G cell as serving.
- **LTE carrier aggregation is not shown.** MM reports only the primary carrier as serving. During testing, B1 was serving while the aggregated B20 and B7 carriers appeared only as neighbours, and a neighbour list cannot tell a secondary carrier from a nearby cell. So the page shows only what MM reports as serving.
- **Permission:** `GetCellInfo` is not on MM's default D-Bus allow list, so a D-Bus policy file allows it for FlipCTL's user. MM then checks polkit, which allows FlipCTL's session.

### Per-antenna measurements

The RM520N-GL has four antenna connectors. Comparing the signal on each one shows whether an antenna is missing, damaged or badly placed, and helps to aim a directional antenna.

::Image[]{src="/files/pics/rm520n-gl-antenna-connectors.svg" size="60" width="640" height="720" position="center" caption="RM520N-GL antenna connectors, label side up"}

The section lists the connectors **ANT0 to ANT3 in the order they sit on the module**, each with the receive path it carries in the band in use, and **RSRP / RSRQ / SINR** for it:

```
Antennas
4G B20          RSRP / RSRQ / SINR
ANT0 PRX              -114 / -14 / 2
ANT1           not used on this band
ANT2           not used on this band
ANT3 DRX              -115 / -14 / 2
```

On a mid-band like B1 all four connectors read. On a low band only two do, and the other two say `not used on this band` rather than looking like broken antennas. On 5G NSA there is a block for each radio.

#### Which connector carries which path

The modem reports four receive paths: **PRX** (primary), **DRX** (diversity), **RX2** and **RX3** (the third and fourth paths, for 4×4 MIMO). Which connector each path uses depends on the band:

| Band | PRX | DRX | RX2 | RX3 |
|---|---|---|---|---|
| Low band, under 1 GHz (B20, B28, n28, ...) | ANT0 | ANT3 | — | — |
| Mid and high band, and n41 (B1, B3, B7, ...) | ANT0 | ANT3 | ANT1 | ANT2 |
| n77, n78, n79, B42, B43, B48 (3.3–5 GHz) | ANT2 | ANT0 | ANT1 | ANT3 |

From Table 32 of Quectel's *RM520N Series Hardware Design V1.3*, as written up in [What each connector does](../../testing/RM520N-GL.md#what-each-connector-does). RX2 and RX3 are taken to be its third and fourth receive paths; this fits the B20 readings, where exactly those two were empty. Until the cell info gives a band, the lines are named by path only.

#### Technical background: how the measurements are read

- The RM520N-GL reports per-antenna values only to Quectel's AT commands `AT+QRSRP`, `AT+QRSRQ` and `AT+QSINR`. Standard QMI (`nas-get-tx-rx-info`) answers `NotSupported`.
- FlipCTL sends them through MM's `Command()` method, which passes an AT command to the modem through MM's own port queue, so nothing collides with MM's own traffic. The reply is one line per radio: `+QRSRP: <PRX>,<DRX>,<RX2>,<RX3>,<LTE|NR5G>`. `-32768` means no reading on that path.
- **Only while this page is open**, every 2 seconds, and only these three commands. Leaving the page stops them. Only on modems MM handles with its `quectel` plugin; any other modem shows `Not on this modem`.
- **MM must run in debug mode** (`--debug`): `Command()` answers `Operation only allowed in debug mode` otherwise, and the page then says `Needs ModemManager debug mode`. The flag is read when MM starts, and changing it restarts MM (about 20 seconds without cellular), so it stays on. `--log-level=INFO` keeps MM's logging at its usual volume.

:::hint{type="warning"}
Debug mode lets any process that passes MM's D-Bus policy and polkit send any AT command through MM, including ones that change the modem's settings. Today that is root and FlipCTL's own session.
:::

Quectel describes these values as a reference, not a receiver sensitivity test, and recommends reading them while data is flowing. For a proper antenna check, see [Per-antenna signal](../../testing/RM520N-GL.md#per-antenna-signal).

***

## Data connection page

Opened with **Ok** on the data connection block.

::Image[]{src="/files/pics/cpu-software/5g-modem-network.png" size="60" width="768" height="432" position="center" caption="Data connection"}

::Image[]{src="/files/pics/cpu-software/5g-modem-network-2.png" size="60" width="768" height="432" position="center" caption="Data connection, scrolled: speeds and totals"}

Interface, APN, IPv4 address and gateway, IPv6 address, DNS servers, MTU, current download and upload speed, data received and sent, and how long the connection has been up.

**Technical background.** All of it comes from MM's bearer except the speeds and the totals, which come from the interface's own byte counters in sysfs: MM's bearer counters stay at zero unless something turns its statistics polling on.

***

## Config

Opened with the **Config** soft key. A placeholder for now.

::Image[]{src="/files/pics/cpu-software/5g-modem-config.png" size="60" width="768" height="432" position="center" caption="Config: a placeholder"}

The candidates for it, all through MM: radio mode lock (3G, 4G, 5G and the preferred one) and band lock.

***

## Not available on this modem

MM cannot report these on the RM520N-GL, so the app does not show them:

- Module temperature
- LTE carrier aggregation details (secondary carriers and their state)
- The serving cell's bandwidth, CQI and transmit power
- Switching 5G SA and NSA separately, and separate band lists for SA and NSA

They are all available through Quectel AT commands. Now that MM runs in debug mode for the per-antenna measurements, the same path could give carrier aggregation details (`AT+QCAINFO`). This is not planned unless asked for.

***

## Permissions and system files

FlipCTL runs as the user `user` in its own login session on seat1. What the app needs beyond that:

| What | Why | File |
|---|---|---|
| D-Bus policy allowing `GetCellInfo` | Cell info and the band. MM's default policy leaves it to root | `flipctl-modemmanager.conf`, in `/usr/share/dbus-1/system.d/` |
| `/dev/rfkill` to the `rfkill` group | The radio switch | A line in `70-flipctl-devices.rules`, the group in `flipctl.sysusers.conf`, both in the unit's `SupplementaryGroups` |
| MM in debug mode | Per-antenna measurements | `modemmanager-debug.conf`, as `ModemManager.service.d/50-flipctl-debug.conf` |
| GPIO access | The SIM selector | Already there: the `gpio` group and `char-gpiochip` |
| polkit `Device.Control` | Signal setup, reset | Already allowed: MM grants it to an active local session, which FlipCTL's is |

All of these files live in FlipCTL's repository, in `systemd/`. The image build (`linux-build-scripts/build-flipctl.sh`) installs them under `/usr`, and a development deploy (`./build_deploy.sh`) installs them under `/etc`.

***

## Implementation

The code is in the FlipCTL repository (`flipctl-slint`):

| Part | Where | What |
|---|---|---|
| MM watcher | `crates/flipper-ui/src/mm.rs` | The D-Bus connection (zbus, blocking API): reads every modem, follows MM's signals, sets the signal rate, asks for cells, SIM, bearer and per-antenna values while a screen wants them. Also the radio switch and `Reset()` |
| View model | `crates/flipper-ui/src/modem.rs` | Pure and unit-tested: port names, menu entries, states, network names, signal percentage and words, band tables, the per-antenna connector mapping, the main screen's layout and every page's lines |
| SIM selector | `crates/flipper-ui/src/simsel.rs` | The GPIO, through the kernel's character device |
| Main screen | `crates/flipper-ui/ui/modem.slint` | Draws what the view model laid out: the items, the selector, the six bars |
| Pages | `crates/flipper-ui/ui/detail.slint` | The shared detail screen, with an action row for the SIM switch |
| Wiring | `bin/flipctl/src/main.rs` | Menu entries, keys, pages, the confirmation dialog |

zbus adds 45 crates to the build, all MIT-licensed. ModemManager is read only in builds with FlipCTL's `device` feature.

### Testing

- **Unit tests** cover everything the view model decides, with values captured from the RM520N-GL: port naming, states, the main screen's layout and fit, the band tables, reply parsing for the AT commands, the connector mapping per band.
- **Screenshots** like the ones on this page come from FlipCTL's headless renderer, with the device's own data: `flipctl --png out.png --screen modem` (also `modem-device`, `modem-sim`, `modem-signal`, `modem-network`, `modem-config`; `--select` moves the cursor or scrolls). `FLIPCTL_MASK_IDS=1` replaces identifiers with placeholders.
- **The real panel** can be watched from a browser at `http://<device>:8899`.

***

## Plan

| Feature | Status |
|---|---|
| Network menu entry with state | Done |
| One entry per modem, named by port | Done; not yet tried with a second modem plugged in |
| Status bar badge from MM | Done |
| Main screen: four items, Info, Config | Done |
| Radio switch (W_DISABLE1#) | Done, tested |
| SIM switch (physical / eSIM) | Done, tested with the physical SIM; the eSIM is empty on current boards |
| Device info, SIM, data connection pages | Done |
| Verbose signal info: cells, bands, radios | Done |
| Per-antenna measurements, by connector | Done, tested on B1 and B20 |
| Config page | Placeholder |
| Scrolling a long modem name on item 1 | Not done: cut with `..` for now |

Still to check:

- A second modem on USB, to see the several-modems menu on real hardware.
- A provisioned Flipper eSIM, and whether the empty chip's `No SIM` is the chip or the modem's SIM detection.
- Which level of the tray's card-detect line (`sim_cd`, GPIO2_B2) means empty, so the SIM page can show an empty tray.
- 5G NSA with a stable 5G link: that MM lists the 5G cell as serving, and that `AT+QRSRP` answers with a 5G line.
- Physically confirm the RX2 and RX3 connectors, for example by removing ANT1 on B1 and seeing which line drops.
