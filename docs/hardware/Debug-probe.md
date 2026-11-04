---
title: Debug Probe
slug: hardware/debug-probe
docTags: 
createdAt: Wed May 3 2026 18:02:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Wed May 3 2026 18:22:47 GMT+0000 (Coordinated Universal Time)
---

The Debug Probe lets you access the Flipper One debug interface without full disassembly. It connects to the debug port behind the back plate using a ribbon cable.

![Debug Probe Connection to Flipper One](/files/pics/debug-probe-connection-to-flipper-one.png "Debug Probe Connection to Flipper One")

Built around the RP2350 microcontroller, the Flipper One Debug Probe is fully open source, including its hardware design, manufacturing files, and firmware source code.

## Features

The Debug Probe provides the following functionality:

* **MCU debugging via SWD (Serial Wire Debug)**: the probe supports CMSIS-DAP, allowing you to control CPU execution, access memory and peripherals, and program the Flipper One MCU (RP2350) flash. The MCU Firmware VS Code project is preconfigured for CMSIS-DAP debugging, so you can start a debug session right away.
* **USB-serial 1**: Flipper One Linux terminal.
* **USB-serial 2**: Flipper One MCU CLI.
* **USB-serial 3**: real-time Flipper One MCU logs.
* **USB-serial 4**: Debug Probe CLI.
* **USB-GPIO bridge**: access to several GPIO pins of the Flipper One CPU and MCU. You can read from and write to these pins through the Debug Probe CLI.

## Buttons and LEDs

![Debug Probe buttons and LEDs](/files/pics/debug-probe-buttons-and-leds.png "Debug Probe buttons and LEDs")

The Debug Probe has two buttons:
* **CPU RESET**: resets the Flipper One CPU (RK3576).
* **MCU RESET & PROBE BOOT**: resets the Flipper One MCU (RP2350) and puts the Debug Probe into BOOTSEL mode for firmware flashing.

The Debug Probe has the following LEDs:
* **MCU power**: 3.3V power status.
* **MCU UART activity**: Tx and Rx.
* **MCU `IO40` and `IO41` pin state**: pin state indication.
* **CPU UART activity**: Tx and Rx.
* **CPU `GPIO0_D2` and `GPIO0_D3` pin state**: pin state indication.
* **Debug Probe `IO20` pin state**: pin state indication.

## Connectors

The Flipper One Debug Probe has the following connectors:
* **USB port**: connection to a PC.
* **Debug port**: connection to the Flipper One debug port.
* **5-pin header**: interface for a logic analyzer or oscilloscope to monitor CPU and MCU pins.

![Pinout of the Debug Port and 5-Pin Header on the Debug Probe](/files/pics/debug-probe-connectors.png "Pinout of the Debug Port and 5-Pin Header on the Debug Probe")

## Schematics

The Debug Probe hardware is open source and available as a [public Altium 365 project](https://flipper.365.altium.com/designs/14B8CA82-B532-4581-BF6F-641FED8AF7F5). The project allows you to view and export the schematic, PCB layout, 3D model, manufacturing drawings, and bill of materials (BOM).

![Viewing the Debug Probe project in Altium 365](/files/pics/debug-probe-altium-365-view.png "Viewing the Debug Probe project in Altium 365")

## Firmware

The Flipper One Debug Probe firmware is open source. The full firmware source code and prebuilt firmware binaries (`.UF2`) are available in the [flipperone-debug-probe](https://github.com/flipperdevices/flipperone-debug-probe) repository.

Below are instructions on:

- [How to build the firmware](/hardware/Debug-probe#how-to-build-firmware).
- [How to flash the firmware via USB](/hardware/Debug-probe#how-to-flash-firmware).

### How to build firmware

This guide explains how to build the firmware (`.UF2`) from source code. The resulting file can be flashed (uploaded) to the Flipper One Debug Probe MCU via USB.

Prerequisites:

:::::WorkflowBlock
:::WorkflowBlockItem
Install [Visual Studio Code](https://code.visualstudio.com/), [Python](https://www.python.org/downloads/), and [Git](https://git-scm.com/).
:::
:::::

Build the firmware:

:::::WorkflowBlock
:::WorkflowBlockItem
In a terminal, go to the folder where you want to store the Debug Probe firmware source code.
:::

:::WorkflowBlockItem
Clone the MCU firmware repository:

```shell
git clone --recursive https://github.com/flipperdevices/flipperone-debug-probe
```
:::

:::WorkflowBlockItem
Open Visual Studio Code, go to **File > Open Folder...**, and select the **flipperone-debug-probe** folder cloned.
:::

:::WorkflowBlockItem
When Visual Studio Code prompts you to install the recommended extensions, click **Install** and wait for the process to complete.

![VS Code prompt to install recommended extensions](/files/pics/mcu-firmware-vscode-install-extensions.png)
:::

:::WorkflowBlockItem
In the **Activity Bar** (left sidebar), click the **Raspberry Pi Pico Project** icon to open the project.
:::

:::WorkflowBlockItem
In the opened **Raspberry Pi Pico Project** view, click **Configure CMake**, and then click **Compile Project** to build the firmware.

![](/files/pics/debug-probe-firmware-compilation.png)
:::
:::::

:::hint{type="success"}
After a successful build, the resulting `.UF2` file is located in the `flipperone-debug-probe/build` folder.
:::

### How to flash firmware

This guide explains how to flash the firmware (`.UF2`) to the Flipper One Debug Probe via USB:

:::::WorkflowBlock
:::WorkflowBlockItem
Get the `.UF2` firmware file:
- [Download from repository](https://github.com/flipperdevices/flipperone-debug-probe/releases)
    or
- [Build from source code](./#how-to-build-firmware) if you modified the firmware.
:::

:::WorkflowBlockItem
Hold the **MCU RESET & PROBE BOOT** button and connect the Debug Probe to a PC via USB. The Debug Probe MCU switches to **BOOTSEL** mode.

![Switching debug probe MCU to BOOTSEL mode](/files/pics/debug-probe-switching-to-bootsel.png "Switching debug probe MCU to BOOTSEL mode")

:::
 
:::WorkflowBlockItem
After the Debug Probe MCU enters **BOOTSEL** mode, the device appears on your PC as the **RP2350** mass storage device.

If it does not appear, try a different USB cable and repeat the **BOOTSEL** procedure.
:::
 
:::WorkflowBlockItem
Upload the `.UF2` firmware file to the **RP2350** mass storage device.
:::
:::::

:::Iframe{code="<video&#xA;    autoplay muted loop playsinline style=&#x22;width: 100%; margin: 0 !important;&#x22;&#xA;    src=&#x22;https://cdn.flipperzero.one/Update-debug-probe-firmware-compressed.mp4&#x22;&#xA;></video>" iframeHeight="350"}
:::

:::hint{type="success"}
Once the `.UF2` file has been uploaded, the Debug Probe automatically reboots and the **RP2350** mass storage device disconnects from your PC. The Debug Probe has been successfully updated.
:::

# Usage

## Serial Ports

The Flipper One Debug Probe is detected by the operating system as four serial ports.  
Port names and paths may vary depending on your operating system.

Example device paths on macOS:

| Port | Device path | Description | Baud rate |
| ---- | ----------- | ----------- | --------- |
| Port 1 | `/dev/tty.usbmodemflip_one_debug2` | RK3576 CPU console | `1500000` |
| Port 2 | `/dev/tty.usbmodemflip_one_debug4` | Flipper One MCU CLI | `230400` |
| Port 3 | `/dev/tty.usbmodemflip_one_debug6` | MCU debug log | `230400` |
| Port 4 | `/dev/tty.usbmodemflip_one_debug8` | Debug Probe MCU CLI | `230400` |

## Connect to the RK3576 CPU Console on macOS

This example shows how to connect to the RK3576 CPU console on macOS.

We recommend using [`tio`](https://github.com/tio/tio), because it is lightweight and stable. You can install it with `brew install tio`  

### Basic connection

`tio -b 1500000 /dev/tty.usbmodemflip_one_debug2`

### Connection with timestamps
Use timestamps to see delays between boot log lines and identify where the boot process slows down:  

`tio --timestamp --timestamp-format 24hour-delta -b 1500000 /dev/tty.usbmodemflip_one_debug2`
