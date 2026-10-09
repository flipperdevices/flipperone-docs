---
title: Supported boards
slug: cpu-software/supported-boards
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:20:46 GMT+0000 (Coordinated Universal Time)
---

This page provides a list of boards that support installing Flipper OS using images built by the official build system. For each board, it also lists the target name, notes, hardware-defined boot priority, and instructions for switching to MaskROM mode for flashing via USB. Learn more about MaskROM mode in the [Rockchip MaskROM mode](Maskrom-mode.md) section.

***

## Flipper One (HW ver. F0B0C1)

:::hint{type="info"}
Prototype. Not for sale!
:::

::Image[]{src="/files/pics/flipper_one_prototype.jpg" size="50" position="center" alt="Flipper One (HW ver. F0B0C1)"}

- ✅ DisplayPort on USB-C1.
- ✅ USB-A to USB-A cable not required for flashing via MaskROM mode.
- **Target name:** `flipper-one`.
- **Boot priority:** UFS flash → SD card → USB (MaskROM).
- **Switching to MaskROM mode:** From the MCU mode home screen, go to **Settings → MaskROM**.
- **MaskROM USB port:** :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/7BdCiDckZzDk-h4Qpo3E4_iconusbc.png" alt caption="usb-c icon"} USB-C1.

***

## Armsom Sige5 (aka Banana Pi BPI-M5 Pro)

:::hint{type="success"}
Recommended board!
:::

::Image[]{src="/files/pics/banana-pi-m5-pro.png" size="38" position="center" alt="Banana Pi BPI-M5 Pro"}

- ✅ DisplayPort on USB-C.
- ✅ USB-A to USB-A cable not required for flashing via MaskROM mode.
- **Target name:** `sige5`.
- **Boot priority:** eMMC flash → SD card → USB (MaskROM).
- **Switching to MaskROM mode:** Hold the MASKROM button while powering on the board.
- **MaskROM USB port:** :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/7BdCiDckZzDk-h4Qpo3E4_iconusbc.png" alt caption="usb-c icon"} OTG USB-C.
- **Product documentation:** [Banana Pi BPI-M5 Pro](https://docs.banana-pi.org/en/BPI-M5/BananaPi_BPI-M5_Pro), [Armsom Sige5](https://docs.armsom.org/armsom-sige5)

***

## FireFly ROC-RK3576-PC

::Image[]{src="/files/pics/roc-rk3576.jpg" size="42" position="center" alt="FireFly ROC-RK3576-PC"}

- ✅ DisplayPort on USB-C.
- ✅ USB-A to USB-A cable not required for flashing via MaskROM mode.
- **Target name:** `rock-pc`.
- **Boot priority:** eMMC flash → SD card → USB (MaskROM).
- **Switching to MaskROM mode:** Hold the MASKROM button while powering on the board.
- **MaskROM USB port:** :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/7BdCiDckZzDk-h4Qpo3E4_iconusbc.png" alt caption="usb-c icon"} USB-C port.
- **Product documentation:** [https://wiki.t-firefly.com/en/ROC-RK3576-PC/](https://wiki.t-firefly.com/en/ROC-RK3576-PC/)

***

## Luckfox Omni3576

::Image[]{src="/files/pics/luckfox-omni3576.png" size="48" position="center" alt="Luckfox Omni3576"}

- ✅ DisplayPort on USB-C.
- ✅ USB-A to USB-A cable not required for flashing via MaskROM mode.
- **Target name:** `omni3576`.
- **Boot priority:** eMMC flash → SD card → USB (MaskROM).
- **Switching to MaskROM mode:** Connect the ADC0 pin to the GND pin while powering on the board.
- **MaskROM USB port:** :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/7BdCiDckZzDk-h4Qpo3E4_iconusbc.png" alt caption="usb-c icon"} USB-C port next to the HDMI port.
- **Product documentation:** [https://wiki.luckfox.com/Luckfox-Omni3576/Luckfox-Omni3576-quick-start](https://wiki.luckfox.com/Luckfox-Omni3576/Luckfox-Omni3576-quick-start)

***

## Radxa ROCK 4D

::Image[]{src="/files/pics/radxa-rock-4d.png" size="38" position="center" alt="Radxa ROCK 4D"}

- ❌ No DisplayPort on USB-C.
- ❌ USB-A to USB-A cable required for flashing via MaskROM mode.
- **Target name:** `rock-4d`.
- **Boot priority:** FSPI0 flash → UFS flash → USB (MaskROM).
- **Switching to MaskROM mode:** Hold the MaskROM button while powering on the board.
- **MaskROM USB port:** :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/L3nvkdJxbzOuHJHTQoP9R_icontopusb3.png" alt caption="usb-a icon"} Top USB-A 3.0 port.
- **Product documentation:** [https://docs.radxa.com/en/rock4/rock4d](https://docs.radxa.com/en/rock4/rock4d)

***

## NanoPi M5

::Image[]{src="/files/pics/nanopi-m5.png" size="38" position="center" alt="NanoPi M5"}

- ❌ No DisplayPort on USB-C.
- ❌ USB-A to USB-A cable required for flashing via MaskROM mode.
- **Target name:** `nanopi-m5`.
- **Boot priority**:
  - Boot mode switch in the FSPI position: FSPI1\_M1 flash → eMMC flash → USB (MaskROM).
  - Boot mode switch in the UFS/SD position: UFS flash → SD card → USB (MaskROM).
- **Switching to MaskROM mode:** Hold the MASK button while powering on the board.
- **MaskROM USB port:** :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/L3nvkdJxbzOuHJHTQoP9R_icontopusb3.png" alt caption="usb-a icon"} Top USB-A 3.0 port.
- **Product documentation:** [https://wiki.friendlyelec.com/wiki/index.php/NanoPi\_M5](https://wiki.friendlyelec.com/wiki/index.php/NanoPi_M5)

***

## Rockchip RK3576 EVB1

:::hint{type="info"}
Evaluation board. Not for sale!
:::

::Image[]{src="/files/pics/evb1.jpg" size="55" position="center" alt="Rockchip RK3576 EVB1"}

**Target name:** `evb1`.

Rockchip's official RK3576 EVB1 evaluation board. This board is supported by Flipper OS; however, we cannot disclose detailed information about it due to NDA restrictions.
