---
title: How to install a Linux image
slug: cpu-software/how-to-install-linux-image
---

Flipper OS can be installed on many Rockchip RK3576-based boards, including commercially available ones. This page explains Rockchip’s MaskROM mode and boot priority logic, and provides installation guides as well as a list of boards supported by Flipper OS.

***

## Rockchip MaskROM mode

The Rockchip RK3576 supports a special **MaskROM mode** that allows writing to the onboard storage drives connected to the chip (SPI/eMMC/UFS flash chips) via USB. In this mode, only a dedicated MaskROM USB port of the RK3576 is used.

::Image[]{src="files/pics/rk3576_maskrom_mode.jpg" size="80" position="flex-start" sha="b6f1fb8a0896cf0187167ea96a261f68460a56b9" initialPath="files/pics/rk3576_maskrom_mode.jpg" githubPath="docs/files/pics/rk3576_maskrom_mode.jpg" width="2658" height="1504" darkWidth="2658" darkHeight="1504"}

The code implementing MaskROM mode on the RK3576 is stored in the chip’s internal ROM (read-only memory) during manufacturing and cannot be erased or modified by the user. As a result, the ability to restore the device’s operating system is always preserved, provided the hardware is not damaged.

Switching into MaskROM mode varies across boards, so on the [Supported Boards](Supported-boards.md) page you will find the method for entering MaskROM mode and the USB port used in MaskROM mode for each supported board.

***

## Board boot priority

The RK3576 chip can be configured with one of several boot priority lists for onboard storage drives. This list can contain up to two items (for example, eMMC flash and an SD card). The boot priority is determined by the voltage on the RK3576 `SARADC_VIN0_BOOT` pin, which is set using a resistor divider on the board and can also be pulled to ground via an onboard button or switch to trigger MaskROM mode.

::Image[]{src="files/pics/rk3576_boot_priority_logic.jpg" size="80" position="flex-start" sha="a377d28366e6535e8d37e083b6590661a4f80a5a" initialPath="files/pics/rk3576_boot_priority_logic.jpg" githubPath="docs/files/pics/rk3576_boot_priority_logic.jpg" width="1880" height="2126" darkWidth="1880" darkHeight="2126"}

After power-on, the RK3576 reads the voltage on the `SARADC_VIN0_BOOT` pin to determine the boot priority list and to check if MaskROM mode has been requested. If not, it attempts to boot from the first storage drive in the priority list. If no valid Rockchip-compatible bootloader signature is found on that device, it proceeds to the second storage device. If no bootloader signature is found there either, the RK3576 enters MaskROM mode and waits for commands from a PC via the MaskROM USB interface.

The table below lists all supported boot priority lists (referred to by Rockchip as boot modes) for the RK3576, along with the corresponding resistor combinations and ADC values for each mode.

::Image[]{src="files/pics/rk3576_boot_mode_config.jpg" size="85" position="flex-start" caption="Boot mode depending on the voltage on SARADC_VIN0_BOOT pin of the RK3576 chip" sha="e4b9c6e09a92387e92dc2074d87d102ce630d4ff" initialPath="files/pics/rk3576_boot_mode_config.jpg" githubPath="docs/files/pics/rk3576_boot_mode_config.jpg" width="4658" height="3434" darkWidth="4658" darkHeight="3434"}

On the [Supported Boards](Supported-boards.md) page you will find the boot priority, the method for switching to MaskROM mode, and the MaskROM USB port for each supported board.

***

## How to install the OS

There are two main ways to install an operating system on the board:

- [Writing an image to an SD card](#writing-to-an-sd-card) and inserting it into the device.
- [Writing an image to the onboard storage drive](#writing-to-the-onboard-storage-drive) via USB (in MaskROM mode).

Please note that the RK3576 boots from storage drives according to its boot priority list, as described in the [Board Boot Priority](#board-boot-priority) section. If you need the RK3576 to skip booting from the onboard storage drive that already contains a bootable OS, you can [erase it in MaskROM mode](#erasing-the-onboard-storage-drive).

***

### Writing to an SD card

:::hint{type="warning"}
Use an SD card with a capacity of 8 GB or larger. The SD card will be erased during the OS writing process.
:::

:::::WorkflowBlock
:::WorkflowBlockItem
Download or build an OS image. Use `debian-512-[Target name]-build-[Build ID].img.gz`, where the target name identifies your board. Available target names are listed on the [Supported Boards](Supported-boards.md) page.
:::

:::WorkflowBlockItem
Connect the microSD card to your PC using a card reader.
:::

:::WorkflowBlockItem
Install and run [balenaEtcher](https://etcher.balena.io/) on your PC.
:::

:::WorkflowBlockItem
Go to **Flash from file** and select the `.img.gz` image file.
:::

:::WorkflowBlockItem
Go to **Select target** and choose your SD card.
:::

:::WorkflowBlockItem
Click **Flash!** When the process finishes, remove the SD card from your PC and insert it into your RK3576-based board.
:::

:::WorkflowBlockItem
Reboot the board.
:::
:::::

***

### Writing to the onboard storage drive

:::hint{type="warning"}
The recommended tools for flashing boards in MaskROM mode have only been tested on **Linux (Debian)** and **macOS**. Windows instructions will be available later.
:::

**Step 1:** Install the flashing tools

:::::WorkflowBlock
:::WorkflowBlockItem
Install the required dependencies.

- On Debian: `sudo apt update && sudo apt install -y git curl build-essential pkg-config libusb-1.0-0-dev`
- On macOS: `brew install libusb`
:::

:::WorkflowBlockItem
Install the **Rust compiler** and **Cargo package manager**:

`curl https://sh.rustup.rs -sSf | sh`
:::

:::WorkflowBlockItem
Reopen the terminal.
:::

:::WorkflowBlockItem
Build the **rockusb tool**:
```
cargo install --git https://github.com/collabora/rockchiprs.git --example rockusb --features=nusb rockusb
```
:::
:::::

‎ 

**Step 2:** Prepare the OS image and enter MaskROM mode

:::hint{type="info"}
To complete this step, you need to know your board’s target name, the USB port used in MaskROM mode, and how to enter MaskROM mode. This information is available on the [Supported Boards](Supported-boards.md) page for your specific board.
:::

:::::WorkflowBlock
:::WorkflowBlockItem
[Download](Build-system.md#public-build-server) or [build an OS image locally](How-to-build-linux-image.md). You need:

- The bootloader image for your board (the build system places it here: `/u-boot/[Target name]/rk3576_spl_loader_v*.bin`).
- The compressed full-disk image `debian-[Block size]-[Target name]-build-[Build ID].img.gz` and the corresponding `.bmap` file, which specifies which parts of the image are used. Block size is 512 for eMMC and 4096 for UFS.

:::

:::WorkflowBlockItem
Connect the board to your PC via its MaskROM USB port.
:::

:::WorkflowBlockItem
Put the board into [MaskROM mode](#rockchip-maskrom-mode).
:::
:::::

‎ 

**Step 3:** Flash the OS image

:::::WorkflowBlock
:::WorkflowBlockItem
List connected devices in MaskROM mode:

`rockusb list`

If no devices are listed, check the USB connection, make sure the correct USB port is being used, re-enter MaskROM mode, and run the command again.
:::

:::WorkflowBlockItem
Load the bootloader into RK3576 RAM:

`rockusb download-boot [path to rk3576_loader_*.bin]`
:::

:::WorkflowBlockItem
Select the storage drive you want to use:

`rockusb change-storage X`

Where X can be: 1 — eMMC; 7 — NAND; 8 — SPI NAND; 9 — SPI NOR; 10 — UFS or SATA; 11 — NVMe.
:::

:::WorkflowBlockItem
Write the OS image to the storage drive:

`rockusb write-bmap [path to the OS image file for your board]`
:::

:::WorkflowBlockItem
Reboot the RK3576:

`rockusb reset-device`
:::
:::::

***

### Erasing the onboard storage drive

To erase the onboard storage drive, follow steps 1 and 2 from the [Writing to the onboard storage drive](#writing-to-the-onboard-storage-drive) instructions, excluding the OS image prepare step.

Then perform the following steps:

:::::WorkflowBlock
:::WorkflowBlockItem
List connected devices in MaskROM mode:

`rockusb list`

If no devices are listed, check the USB connection, make sure the correct USB port is being used, re-enter MaskROM mode, and run the command again.
:::

:::WorkflowBlockItem
Load the bootloader into RK3576 RAM:

`rockusb download-boot [path to rk3576_spl_loader_*.bin]`
:::

:::WorkflowBlockItem
Select the storage drive to erase:

`rockusb change-storage X`

Where X can be: 1 — eMMC; 7 — NAND; 8 — SPI NAND; 9 — SPI NOR; 10 — UFS or SATA; 11 — NVMe.
:::

:::WorkflowBlockItem
Erase the storage drive:

`rockusb erase-flash`
:::

:::WorkflowBlockItem
Reboot the RK3576:

`rockusb reset-device`
:::
:::::
