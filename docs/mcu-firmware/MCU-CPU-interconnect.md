---
title: MCU↔CPU interconnect
slug: mcu-firmware/mcu-cpu-interconnect
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:09:06 GMT+0000 (Coordinated Universal Time)
---
![MCU↔CPU interconnect](/files/pics/cpu-and-mcu-interconnection.jpg)

The interconnect between the MCU and CPU consists of:

- **UART** (Universal Asynchronous Receiver-Transmitter) connects Linux console serial port to the RP2350.
- **SPI** (Serial Peripheral Interface) for transferring frame buffer from the Linux side to the RP2350 side for output to the display.
- **I²C** (Inter-Integrated Circuit) for transferring commands from Linux side (I²C master) and input events from MCU side (I²C slave).
- **INT** pin is used by the MCU to notify the CPU of new events.
- **BOOT0** & **BOOT1** pins are used to control the main CPU’s boot process. The BOOT0 pin can force the CPU into MaskROM mode, enabling UFS flash programming via USB. The BOOT1 pin selects the OS boot source; the MCU generates a PWM signal that is converted into a voltage level, which the CPU reads via its ADC during the early boot stage.

Reference:

- [Raspberry Pi RP1 Peripherals reference (PDF)](https://pip-assets.raspberrypi.com/categories/892-raspberry-pi-5/documents/RP-008370-DS-1-rp1-peripherals.pdf)
