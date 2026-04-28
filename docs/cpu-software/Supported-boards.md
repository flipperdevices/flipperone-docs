---
title: Supported boards
slug: cpu-software/supported-boards
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:20:46 GMT+0000 (Coordinated Universal Time)
---

This page provides a list of boards that support installing Flipper OS using images built by the official build system. It also includes the target name, board-specific notes, hardware-defined boot priority, and instructions for switching each board to MaskROM mode for flashing via USB. Learn more about MaskROM mode in the :Link[Rockchip MaskROM mode]{label="Rockchip MaskROM mode" overridedLabel="Rockchip MaskROM mode" spaceId docId="ArIvFnCX7_Or8oeQLXVoK" version="v2" docAnchorId="#rockchip-maskrom-mode" loadingMethod="dynamic" newTab="false" githubPath="./How-to-install-an-image.md#rockchip-maskrom-mode" href="How-to-install-an-image.md"} section.

## Flipper One (HW ver. F0B0C1)

**Prototype. Not for sale!**

::Image[]{src="files/pics/flipper_one_prototype.jpg" size="50" position="flex-start" caption="Flipper One (HW ver. F0B0C1)" sha="dff3152b6d79cccddbd83ebbd304765e8184518c" initialPath="files/pics/flipper_one_prototype.jpg" githubPath="docs/files/pics/flipper_one_prototype.jpg" width="500" height="500" darkWidth="500" darkHeight="500"}

✅ DisplayPort on USB-C1.

✅ USB-A to USB-A cable not required for flashing via MaskROM mode.

**Target name:** `flipper-one`.

**Boot priority:** UFS flash → SD card → USB (MaskROM).

**Switching to MaskROM mode:** from the boot menu on the screen.

**MaskROM USB port:** :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/7BdCiDckZzDk-h4Qpo3E4_iconusbc.png" alt caption="usb-c icon"} USB-C1.

***

## Armsom Sige5 (aka Banana Pi BPI-M5 Pro)

**Recommended board!**

::Image[]{src="files/pics/banana-pi-m5-pro.png" size="38" position="flex-start" caption="Banana Pi BPI-M5 Pro" sha="2d83d808da6981fa0c2a044d184f77fddc55e1c5" initialPath="files/pics/banana-pi-m5-pro.png" githubPath="docs/files/pics/banana-pi-m5-pro.png" width="280" height="198" darkWidth="280" darkHeight="198"}

✅ DisplayPort on USB-C.

✅ USB-A to USB-A cable not required for flashing via MaskROM mode.

**Target name:** `sige5`.

**Boot priority:** eMMC flash → SD card → USB (MaskROM).

**Switching to MaskROM mode:** Hold the MASKROM button while powering on the board.

**MaskROM USB port:** :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/7BdCiDckZzDk-h4Qpo3E4_iconusbc.png" alt caption="usb-c icon"} OTG USB-C.

**Product documentation:**

Banana Pi BPI-M5 Pro:
[https://docs.banana-pi.org/en/BPI-M5/BananaPi\_BPI-M5\_Pro](https://docs.banana-pi.org/en/BPI-M5/BananaPi_BPI-M5_Pro)

Armsom Sige5:
[https://docs.armsom.org/armsom-sige5](https://docs.armsom.org/armsom-sige5)

***

## FireFly ROC-RK3576-PC

::Image[]{src="files/pics/roc-rk3576.jpg" size="42" position="flex-start" caption="FireFly ROC-RK3576-PC" sha="625c47e1c70bf6d099ee877be9e5da6ad72f0bb0" initialPath="files/pics/roc-rk3576.jpg" githubPath="docs/files/pics/roc-rk3576.jpg" width="1534" height="979" darkWidth="1534" darkHeight="979"}

✅ DisplayPort on USB-C.

✅ USB-A to USB-A cable not required for flashing via MaskROM mode.

**Target name:** `rock-pc`.

**Boot priority:** eMMC flash → SD card → USB (MaskROM).

**Switching to MaskROM mode:** Hold the MASKROM button while powering on the board.

**MaskROM USB port:** :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/7BdCiDckZzDk-h4Qpo3E4_iconusbc.png" alt caption="usb-c icon"} USB-C port.

**Product documentation:** [https://wiki.t-firefly.com/en/ROC-RK3576-PC/](https://wiki.t-firefly.com/en/ROC-RK3576-PC/)

***

## Luckfox Omni3576

::Image[]{src="files/pics/luckfox-omni3576.png" size="48" position="flex-start" caption="Luckfox Omni3576" sha="5ad0f24e5a69de1ee4bf77f4239fdad3307d6611" initialPath="files/pics/luckfox-omni3576.png" githubPath="docs/files/pics/luckfox-omni3576.png" width="621" height="464" darkWidth="621" darkHeight="464"}

✅ DisplayPort on USB-C.

✅ USB-A to USB-A cable not required for flashing via MaskROM mode.

**Target name:** `omni3576`.

**Boot priority:** eMMC flash → SD card → USB (MaskROM).

**Switching to MaskROM mode:** Connect the ADC0 pin to the GND pin while powering on the board.

**MaskROM USB port:** :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/7BdCiDckZzDk-h4Qpo3E4_iconusbc.png" alt caption="usb-c icon"} USB-C port next to the HDMI port.

**Product documentation:** [https://wiki.luckfox.com/Luckfox-Omni3576/Luckfox-Omni3576-quick-start](https://wiki.luckfox.com/Luckfox-Omni3576/Luckfox-Omni3576-quick-start)

***

## Radxa ROCK 4D

::Image[]{src="files/pics/radxa-rock-4d.png" size="38" position="flex-start" caption="Radxa ROCK 4D" sha="26bd3166e461632b84fd366e11791fa5c8db8411" initialPath="files/pics/radxa-rock-4d.png" githubPath="docs/files/pics/radxa-rock-4d.png" width="1200" height="800" darkWidth="1200" darkHeight="800"}

❌ No DisplayPort on USB-C.

❌ USB-A to USB-A cable required for flashing via MaskROM mode.

**Target name:** `rock-4d`.

**Boot priority:** FSPI0 flash → UFS flash → USB (MaskROM).

**Switching to MaskROM mode:** Hold the MaskROM button while powering on the board.

**MaskROM USB port:** :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/L3nvkdJxbzOuHJHTQoP9R_icontopusb3.png" alt caption="usb-a icon"} Top USB-A 3.0 port.

**Product documentation:** [https://docs.radxa.com/en/rock4/rock4d](https://docs.radxa.com/en/rock4/rock4d)

***

## NanoPi M5

::Image[]{src="files/pics/nanopi-m5.png" size="38" position="flex-start" caption="NanoPi M5" sha="568baeee09ac6b17566a0b101b92f299bb3d5df2" initialPath="files/pics/nanopi-m5.png" githubPath="docs/files/pics/nanopi-m5.png" width="1104" height="810" darkWidth="1104" darkHeight="810"}

❌ No DisplayPort on USB-C.

❌ USB-A to USB-A cable required for flashing via MaskROM mode.

**Target name:** `nanopi-m5`.

**Boot priority:**

- Boot mode switch in the FSPI position: FSPI1\_M1 flash → eMMC flash → USB (MaskROM).
- Boot mode switch in the UFS/SD position: UFS flash → SD card → USB (MaskROM).

**Switching to MaskROM mode:** Hold the MASK button while powering on the board.

**MaskROM USB port:** :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/L3nvkdJxbzOuHJHTQoP9R_icontopusb3.png" alt caption="usb-a icon"} Top USB-A 3.0 port.

**Product documentation:** [https://wiki.friendlyelec.com/wiki/index.php/NanoPi\_M5](https://wiki.friendlyelec.com/wiki/index.php/NanoPi_M5)

***

## Rockchip RK3576 EVB1

**Evaluation board. Not for sale!**

::Image[]{src="files/pics/evb1.png" size="38" position="flex-start" caption="Rockchip RK3576 EVB1" sha="ec731e80438e05355afe2d8fd22d2536e2bcaafe" initialPath="files/pics/evb1.png" githubPath="docs/files/pics/evb1.png" width="200" height="120" darkWidth="200" darkHeight="120"}

**Target name:** `evb1`.

Official Rockchip RK3576 Evaluation board EVB1. This board is supported by Flipper OS; however, we cannot disclose detailed information about it due to NDA restrictions.
