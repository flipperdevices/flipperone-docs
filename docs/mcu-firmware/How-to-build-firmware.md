---
title: How to build firmware
slug: mcu-firmware/how-to-build-firmware
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:14:38 GMT+0000 (Coordinated Universal Time)
---

This page explains how to build the MCU firmware file (`.UF2`) from source code. The resulting file can be uploaded to the MCU of Flipper One via USB.

To build the MCU firmware locally:

:::::WorkflowBlock
::::WorkflowBlockItem
Install [Visual Studio Code](https://code.visualstudio.com/), [Python](https://www.python.org/downloads/), and [git](https://git-scm.com/).
::::

::::WorkflowBlockItem
Open a terminal in the folder where you want to store the firmware source code.
::::

::::WorkflowBlockItem
Clone the MCU firmware repository to your computer:

`git clone --recursive https://github.com/flipperdevices/flipperone-mcu-firmware`
::::

::::WorkflowBlockItem
Open Visual Studio Code and go to **File → Open Folder...** and select the **flipperone-mcu-firmware** folder you just cloned.
::::

::::WorkflowBlockItem
Visual Studio Code will prompt you to install the recommended extensions. Click **Install** to accept, and wait until the process is complete.

![VS Code prompt to install recommended extensions](/files/pics/mcu-firmware-vscode-install-extensions.png)
::::

::::WorkflowBlockItem
Click **Raspberry Pi Pico Project** in the left sidebar. If VS Code prompts you to import the project as a Raspberry Pi Pico project, click **Yes** and import it with the default settings.
::::

::::WorkflowBlockItem
Click **Configure CMake**.
::::

::::WorkflowBlockItem
Click **Compile Project**. 

![Building the MCU firmware in VS Code](/files/pics/mcu-firmware-vscode-compilation.png)

::::

::::WorkflowBlockItem
After a successful build, the firmware file is located in the `flipperone-mcu-firmware/build` folder.
::::

:::::

***

:::hint{type="info"}
By default, the firmware file is built for the Flipper One rev. `F0B0C1` (target `f1`). 
If you need to build the firmware for rev. `2.F0B1C2` (target `f2`), go to **Terminal → Run Task → Select Target** and select the `f2` target. 
After changing the target, click **Compile Project** again.
:::

To flash the firmware to the MCU, follow the instructions on the [Firmware Update](Firmware-update.md) page.
