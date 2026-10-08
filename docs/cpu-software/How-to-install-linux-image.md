---
title: How to install a Linux image
slug: cpu-software/how-to-install-linux-image
---

Flipper OS can be installed on many Rockchip RK3576-based boards, including commercially available ones (see [supported boards](Supported-boards.md) page).

There are two ways to install Flipper OS:

- [Using Flipper OS Installer](#install-os-using-flipper-os-installer) — a tool that runs on the device, downloads official Flipper OS images and profiles, and installs them to microSD card or UFS storage.
- [By writing an OS image to a microSD card](#write-an-os-image-to-a-microsd-card) using a card reader.

:::hint{type="info"}
**RK3576 boots from storage devices according to the boot priority**
For example, Flipper One uses the following boot order: UFS → SD card → USB. If you need RK3576 to skip booting from UFS, see [How to erase the bootloader on UFS](#how-to-erase-the-bootloader-on-ufs).
:::

***

## Install OS using Flipper OS Installer

You'll need:

* Flipper One or another supported board.
* A Linux (Debian) or macOS PC to load the OS Installer onto the board.
* A USB-C cable to connect the device to your PC.
* An Ethernet cable with internet access.

For boards other than Flipper One, you'll also need:
* An HDMI monitor.
* A USB keyboard.

‎ 

The OS installation process consists of three steps:
1. [Install rockusb on your PC](#step-1-install-rockusb-on-your-pc).
2. [Run Flipper OS Installer on your board](#step-2-run-flipper-os-installer-on-your-board).
3. [Install the OS](#step-3-install-the-os).

‎ 

### Step 1. Install rockusb on your PC

The rockusb tool is required to load the Flipper OS Installer image into the RK3576's RAM using [MaskROM mode](Maskrom-mode.md) of the SoC.

To install rockusb on your PC, follow the instructions for your operating system:

:::::::::::Tabs

::::::::::Tab{title="On Linux (Debian)"}

:::::WorkflowBlock
::::WorkflowBlockItem
Run the command:
`sudo apt update && sudo apt install rockusb`
::::

::::WorkflowBlockItem
Run rockusb to verify that it works:
`rockusb`
::::
:::::

::::::::::

::::::::::Tab{title="On macOS"}
:::::WorkflowBlock
::::WorkflowBlockItem
Install the **Rust compiler** and **Cargo package manager**:
`curl https://sh.rustup.rs -sSf | sh`
::::

::::WorkflowBlockItem
Reopen the terminal.
::::

::::WorkflowBlockItem
Build the **rockusb tool**:
`cargo install --git https://github.com/collabora/rockchiprs.git --example rockusb --features=nusb rockusb`
::::

::::WorkflowBlockItem
Run rockusb to verify that it works:
`rockusb`
::::

:::::

::::::::::

:::::::::::

‎ 

### Step 2. Run Flipper OS Installer on your board

:::::WorkflowBlock
:::WorkflowBlockItem
Go to the [installer build artifacts](https://dl-linux-images.flipp.dev/falcon-installer/#sort=mtime.desc&full=1) page and select the latest installer build (the first item in the list).
:::

:::WorkflowBlockItem
Click your board's target name and download `installer-falcon-loader.bin`.
If you don't know the target name, check [Supported Boards](Supported-boards.md).
:::

:::WorkflowBlockItem
Connect the cables:
* **Flipper One**: Disconnect the HDMI monitor, if connected.
* **Other boards**: Connect an HDMI monitor and USB keyboard.
* Connect the board to your PC via its MaskROM USB port. If unsure which port to use, check [Supported Boards](Supported-boards.md).
* Connect the board to a LAN with internet access.
:::

:::WorkflowBlockItem
Put the board into MaskROM mode as described in [Supported Boards](Supported-boards.md).
:::

:::WorkflowBlockItem
On your PC list connected devices in MaskROM mode:
`rockusb list`

If no devices are listed, check the USB connection and port, re-enter MaskROM mode, and run the command again.
:::

:::WorkflowBlockItem
To upload and run the Flipper OS Installer on your device, run the command on your PC from the folder containing the Installer image:
`rockusb download-boot installer-falcon-loader.bin`
:::

:::WorkflowBlockItem
Flipper OS Installer UI will appear:
* **Flipper One:** On the device screen. Use the buttons to navigate.
* **Other boards:** On the HDMI monitor. Use a USB keyboard to navigate. The keys work as follows:

<table isTableHeaderOn="true" columnWidths="200,200">
  <tr>
    <td align="center">
      <p><strong>Key on Flipper One</strong></p>
    </td>
    <td align="center">
      <p><strong>Key on USB keyboard</strong></p>
    </td>
  </tr>
  <tr>
    <td>
      <p>D-pad Ok button</p>
    </td>
    <td>
      <p>↵ Enter</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff">
      <p>D-pad arrow buttons</p>
    </td>
    <td lightBackgroundColor="#f0f7ff">
      <p>← ↑ → ↓ Arrow buttons</p>
    </td>
  </tr>
  <tr>
    <td>
      <p>Back button</p>
    </td>
    <td>
      <p>⌫ Backspace</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff">
      <p>Esc button</p>
    </td>
    <td lightBackgroundColor="#f0f7ff">
      <p>Z</p>
    </td>
  </tr>
  <tr>
    <td>
      <p>View button</p>
    </td>
    <td>
      <p>X</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff">
      <p>Power button</p>
    </td>
    <td lightBackgroundColor="#f0f7ff">
      <p>C</p>
    </td>
  </tr>
  <tr>
    <td>
      <p>Edit button</p>
    </td>
    <td>
      <p>V</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff">
      <p>Run button</p>
    </td>
    <td lightBackgroundColor="#f0f7ff">
      <p>B</p>
    </td>
  </tr>
</table>
:::

:::::

‎ 

### Step 3. Install the OS

::Image[]{src="files/pics/flipper-os-installer-ui.png" size="100" position="center"}

In the Flipper OS Installer, do the following:

:::::WorkflowBlock
::::WorkflowBlockItem
In **Source**, select the OS release branch:

* `Release` — Stable and tested builds.
* `Release candidate` — Builds ready for final testing before release.
* `Nightly` — Latest daily builds.
* `Dev` — Builds in active development.

After selecting a branch, choose an OS build from the list.
::::

::::WorkflowBlockItem
In **Device**, select the storage device to install the OS on:
* `/dev/mmcblk0 [eMMC]` — microSD card.
* `/dev/sda [UFS]` — UFS storage.

If UFS is present but lacks the required hardware partitions (logical units) for the Flipper OS installation, you will need to select `Reprovision UFS` first. **Reprovisioning will erase all data on the UFS storage!**
::::

::::WorkflowBlockItem
In **Profiles**, select the official OS profiles to install. The `Minimal` profile is always installed. Other profiles are optional.

See [OS profiles and snapshots](profiles.md) for more information about OS profiles.
::::

::::WorkflowBlockItem
In **Fetch**, select how the installer downloads and verifies the OS image:

* `Download & verify` (more reliable, but slower) — Downloads the entire image, verifies its integrity, and writes it to storage.
* `Stream` (faster, but less reliable) — Writes the image while downloading. Each block is verified before being written, but a verification failure only generates warnings in the installation log.
::::

::::WorkflowBlockItem
Press **Install** and wait for the installation to complete. Then press **Reboot**.
::::
:::::

***

## Write an OS image to a microSD card

:::hint{type="danger"}
**The microSD card will be erased during this process!**
:::

‎ 

To write the OS image on a microSD card:

:::::WorkflowBlock
::::WorkflowBlockItem
[Download](https://dl-linux-images.flipp.dev/full-img/) or [build](How-to-build-linux-image.md) an OS image. Use `debian-512-[Target name]-build-[Build ID].img.zst`, where `[Target name]` identifies your board. 
See [Supported Boards](Supported-boards.md) for available target names.
::::

::::WorkflowBlockItem
Connect an 8 GB or larger microSD card to your PC using a card reader.
::::

::::WorkflowBlockItem
Download and run [Raspberry Pi Imager](https://www.raspberrypi.com/software/) on your PC.
::::

::::WorkflowBlockItem
Click the **OS** tab. Then click **Use custom**, select the `.zst` OS image and click **NEXT**. 

![](/files/pics/flipper-os-write-os-image-step1.png)
::::

::::WorkflowBlockItem
In the **Storage** tab, select your microSD card in the list and click **NEXT**.

![](/files/pics/flipper-os-write-os-image-step2.png)
::::

::::WorkflowBlockItem
On the **Writing** tab, click **WRITE** and wait until the process finishes.

![](/files/pics/flipper-os-write-os-image-step3.png)
::::

::::WorkflowBlockItem
Insert the microSD card into your board and reboot the board.
::::
:::::

:::hint{type="info"}
**Mind the boot priority**

The RK3576 boots from storage devices according to their boot priority. For example, Flipper One uses the following boot order: UFS → SD card → USB.

If UFS contains a bootable OS, the device will boot from UFS instead of the microSD card. To make the UFS storage unbootable, see [How to erase the bootloader on UFS](#how-to-erase-the-bootloader-on-ufs).
:::
***

## How to erase the bootloader on UFS
:::hint{type="warning"}
**This will erase the bootloader from UFS, making it unbootable until it is reflashed**. User data will not be affected.
:::

To erase the bootloader on UFS storage, do the following:

:::::WorkflowBlock
:::WorkflowBlockItem
First, boot your device from UFS storage.
:::

:::WorkflowBlockItem
Run in the terminal:

`sudo blkdiscard /dev/sdb`
`sudo blkdiscard /dev/sdc`
:::

:::WorkflowBlockItem
Reboot the device.
:::
:::::
