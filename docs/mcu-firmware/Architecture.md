---
title: MCU Firmware Architecture
slug: mcu-firmware/architecture
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:07:05 GMT+0000 (Coordinated Universal Time)
---

Flipper One uses a dual-processor architecture with **High-Performance Linux CPU (Rockchip RK3576)** and **Low-Power MCU (Raspberry Pi RP2350)**. While the CPU runs Linux and manages all high-level peripherals (USB, HDMI, M.2, Wi-Fi, Ethernet, and audio), the MCU is responsible for the following tasks:

- Rendering image on the LCD display
- Processing events from the buttons and touchpad
- Controlling the LEDs
- Managing the battery and power subsystems
- Implements Power Bank mode
- Managing system power states
- Handling communication through the CC pins of the USB-C ports
- Controlling the main CPU power-on and boot process

## CPU and MCU interconnection

The MCU and CPU are interconnected via several interfaces and GPIO pins, including:

- **SPI (Serial Peripheral Interface)** for transferring frame buffer from the Linux side to the RP2350 side for output to the display.
- **I²C (Inter-Integrated Circuit)** for transferring commands from Linux side and input events from MCU side.
- **UART (Universal Asynchronous Receiver-Transmitter)** connects Linux console serial port to the RP2350 (just in case).
- **BOOT\_0 & BOOT\_1** pins used for controlling of boot process of the main CPU.
- **2 x IRQ** pins provide instant notification to the opposite side of any asynchronous event.

![Flipper One dual processor architecture](/files/pics/flipper-one-dual-cpu-architecture.png "Flipper One dual processor architecture")

## RP2350 overview

As the low-power MCU, we use the [Raspberry Pi RP2350 microcontroller](https://pip.raspberrypi.com/documents/RP-008373-DS), which features:

- Two selectable ARM Cortex-M33 or Hazard3 RISC-V cores.
- 520 KB of SRAM.
- 2 MB of QSPI NOR flash memory.
- A rich set of peripheral interfaces, including SPI, I²C, UART, and PWM.
- A powerful PIO (Programmable Input/Output) subsystem for flexible, timing-precise hardware interfacing.

![RP2350 block diagram](/files/pics/rp2350-internals.png "RP2350 block diagram")

## Firmware architecture

The MCU firmware is built on the [FreeRTOS](https://www.freertos.org/) kernel and a set of libraries and drivers organized in a layered firmware architecture.

![MCU firmware architecture](/files/pics/mcu-firmware-architecture.jpg "MCU firmware architecture")

