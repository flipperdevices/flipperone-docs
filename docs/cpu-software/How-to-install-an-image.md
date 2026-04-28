---
title: How to install an image
slug: cpu-software/install-image
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:20:03 GMT+0000 (Coordinated Universal Time)
---

Flipper OS can be installed on many Rockchip RK3576-based boards, many of which are commercially available. This page explains Rockchip’s MaskROM mode and boot priority logic, and provides installation guides as well as a list of boards supported by FlipperOS.

## Rockchip MaskROM mode

The Rockchip RK3576 supports a special **MaskROM mode** that allows writing to the on-board storage drives connected to the chip (SPI/eMMC/UFS flash chips) via USB. In this mode, only a dedicated MaskROM USB port of the RK3576 is used.

::Image[]{src="files/pics/rk3576_maskrom_mode.jpg" size="80" position="flex-start" sha="b6f1fb8a0896cf0187167ea96a261f68460a56b9" initialPath="files/pics/rk3576_maskrom_mode.jpg" githubPath="docs/files/pics/rk3576_maskrom_mode.jpg" width="2658" height="1504" darkWidth="2658" darkHeight="1504"}

The code implementing MaskROM mode on the RK3576 is stored in the chip’s internal ROM (read-only memory) during manufacturing and cannot be erased or modified by the user. As a result, the ability to restore the device’s operating system is always preserved, provided the hardware is not damaged.

Switching into MaskROM mode varies across different boards, so on the [Supported Boards](Supported-boards.md) page you will find the method for entering MaskROM mode and the USB port used in MaskROM mode for each supported board.

## Board boot priority

The RK3576 chip may have a different boot priority list for onboard storage drives. This list can contain up to two items (for example, eMMC flash and an SD card). The boot priority is determined by the voltage on the RK3576 `SARADC_VIN0_BOOT` pin, which is set using a resistor divider on the board and can also be pulled to ground via an onboard button or switch to trigger MaskROM mode.

::Image[]{src="files/pics/rk3576_boot_priority_logic.jpg" size="80" position="flex-start" sha="a377d28366e6535e8d37e083b6590661a4f80a5a" initialPath="files/pics/rk3576_boot_priority_logic.jpg" githubPath="docs/files/pics/rk3576_boot_priority_logic.jpg" width="1880" height="2126" darkWidth="1880" darkHeight="2126"}

After power-on, the RK3576 reads the voltage on the `SARADC_VIN0_BOOT` pin to determine the boot priority list and to check if MaskROM mode has been requested. If not, it attempts to boot from the first storage drive in the priority list. If no bootable OS is found on that device, it proceeds to the second storage drive in the list. If again no bootable OS is detected, the RK3576 switches to MaskROM mode and waits for commands from a PC via the MaskROM USB port.

The table below lists all supported boot priority lists (referred to by Rockchip as boot modes) for the RK3576, along with the corresponding resistor combinations and ADC values for each mode.

::Image[]{src="files/pics/rk3576_boot_mode_config.jpg" size="85" position="flex-start" caption="Boot mode depending on the voltage on SARADC_VIN0_BOOT pin of the RK3576 chip" sha="e4b9c6e09a92387e92dc2074d87d102ce630d4ff" initialPath="files/pics/rk3576_boot_mode_config.jpg" githubPath="docs/files/pics/rk3576_boot_mode_config.jpg" width="4658" height="3434" darkWidth="4658" darkHeight="3434"}

On the [Supported Boards](Supported-boards.md) page you will find the boot priority, the method for switching to MaskROM mode, and the MaskROM USB port for each supported board.

## How to install the OS

There are two main ways to install an operating system on the board:

- :Link[Writing an image to an SD card]{label="Writing an image to an SD card" overridedLabel="Writing an image to an SD card" spaceId docId="ArIvFnCX7_Or8oeQLXVoK" version="v2" docAnchorId="#writing-to-an-sd-card" loadingMethod="dynamic" newTab="false" href="How-to-install-an-image.md"} and inserting it into the device.
- :Link[Writing an image to the onboard storage drive]{label="Writing an image to the onboard storage drive" overridedLabel="Writing an image to the onboard storage drive" spaceId docId="ArIvFnCX7_Or8oeQLXVoK" version="v2" docAnchorId="#writing-to-the-onboard-storage-drive" loadingMethod="dynamic" newTab="false" href="How-to-install-an-image.md"} via USB (in MaskROM mode).

Please note that the RK3576 boots from storage drives according to its boot priority list, as described in the :Link[Board Boot Priority]{label="Board Boot Priority" overridedLabel="Board Boot Priority" spaceId docId="ArIvFnCX7_Or8oeQLXVoK" version="v2" docAnchorId="#board-boot-priority" loadingMethod="dynamic" newTab="false" href="How-to-install-an-image.md"} section. If you need the RK3576 to skip booting from the onboard storage drive that already contains a bootable OS, you can [erase it in MaskROM mode]().

### Writing to an SD card

:::hint{type="warning"}
Use an SD card with a capacity of 4 GB or larger. The SD card will be erased during the OS writing process.
:::

1. Download or build an OS image. Use `debian-512-[Target name]-build-[Build ID].img.gz`, where the target name identifies your board. Available target names are listed on the [Supported Boards](Supported-boards.md) page.
2. Connect the microSD card to your PC using a card reader.
3. Install and run [balenaEtcher](https://etcher.balena.io/) on your PC.
4. Go to **Flash from file** and select the `.img.gz` image file.
5. Go to **Select target** and choose your SD card.
6. Click **Flash!** When the process finishes, remove the SD card from your PC and insert it into your RK3576-based board.
7. Reboot the board.

### Writing to the onboard storage drive

:::hint{type="warning"}
The recommended tools for flashing boards in MaskROM mode have only been tested on **Linux (Debian)** and **macOS**. Windows instructions will be available later.
:::

**Step 1: Install the flashing tools**

1. Install the required dependencies.

On Debian: `sudo apt update && sudo apt install -y git curl build-essential pkg-config libusb-1.0-0-dev`

On macOS: `brew install libusb`

2. Install the **Rust compiler** and **Cargo package manager**:

`curl https://sh.rustup.rs -sSf | sh`

3. Reopen the terminal.
4. Build the **rockusb tool**:

`cargo install --branch switch-storage --git https://github.com/collabora/rockchiprs.git --example rockusb --features=nusb rockusb`

**Step 2: Prepare the OS image and enter MaskROM mode**

:::hint{type="info"}
To complete this step, you need to know your board’s target name, the USB port used in MaskROM mode, and how to enter MaskROM mode. This information is available on the [Supported Boards](Supported-boards.md) page for your specific board.
:::

1. :Link[Download]{label="Download" overridedLabel="Download" spaceId docId="isVWIRz7zz0jE7gRAHigs" version="v2" docAnchorId="#public-build-server" loadingMethod="dynamic" newTab="false" githubPath="./Build-system.md#public-build-server" href="Build-system.md"} or [build an OS image locally](How-to-build-an-image-locally.md). You need:
   - The bootloader image for your board (the build system places it here: `/u-boot/[Target name]/rk3576_spl_loader_v*.bin`).
   - The compressed full-disk image `debian-4096-[Target name]-build-[Build ID].img.gz` and the corresponding `.bmap` file, which specifies which parts of the image are used.
2. Connect the board to your PC using the MaskROM USB port on your board.
3. Put the board into :Link[MaskROM mode]{label="MaskROM mode" overridedLabel="MaskROM mode" spaceId docId="ArIvFnCX7_Or8oeQLXVoK" version="v2" docAnchorId="#rockchip-maskrom-mode" loadingMethod="dynamic" newTab="false" href="How-to-install-an-image.md"}.

**Step 3: Flash the OS image**

1. List connected devices in MaskROM mode:

`rockusb list`

If no devices are listed, check the USB connection, make sure the correct USB port is being used, re-enter MaskROM mode, and run the command again.

2. Load the bootloader into RK3576 RAM:

`rockusb download-boot [path to rk3576_spl_loader_*.bin]`

3. Select the storage drive you want to use:

`rockusb change-storage X`

Where X can be: 1 — eMMC; 7 — NAND; 8 — SPI NAND; 9 — SPI NOR; 10 — UFS or SATA; 11 — NVMe.

4. Write the OS image to the storage drive:

`rockusb write-bmap [path to the OS image file for your board]`

5. Reboot the RK3576:

`rockusb reset-device`

### Erasing the onboard storage drive

To erase the onboard storage drive, follow steps 1 and 2 from the :Link[Writing to the onboard storage drive]{label="Writing to the onboard storage drive" overridedLabel="Writing to the onboard storage drive" spaceId docId="ArIvFnCX7_Or8oeQLXVoK" version="v2" docAnchorId="#writing-to-the-onboard-storage-drive" loadingMethod="dynamic" newTab="false" href="How-to-install-an-image.md"} instructions, excluding the OS image prepare step.

Then perform the following steps:

1. List connected devices in MaskROM mode:

`rockusb list`

If no devices are listed, check the USB connection, make sure the correct USB port is being used, re-enter MaskROM mode, and run the command again.

2. Load the bootloader into RK3576 RAM:

`rockusb download-boot [path to rk3576_spl_loader_*.bin]`

3. Select the storage drive to erase:

`rockusb change-storage X`

Where X can be: 1 — eMMC; 7 — NAND; 8 — SPI NAND; 9 — SPI NOR; 10 — UFS or SATA; 11 — NVMe.

4. Erase the storage drive:

`rockusb erase-flash`

5. Reboot the RK3576:

`rockusb reset-device`
