---
title: Schematics
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 11:00:48 GMT+0000 (Coordinated Universal Time)
---

This section contains the electrical schematics of Flipper One. They are published in the format ???

The source files are located in the repository:

Flipper One runs on two controllers—one of them is a SoC (system-on-chip) with Linux inside, to which all interfaces are connected—Wi-Fi, Bluetooth, Ethernet, USB, HDMI, M2 connector, SD card.

The second is a microcontroller that performs two functions: it controls the device when its big brother is absent — when the SoC is not loaded or is asleep — and when it is loaded, it provides it with access to all HIDs — buttons, LEDs, screen, touchpad, haptics.

The two controllers are connected to each other by several interfaces:

SPI — the screen image is transmitted via this interface. It is proxied through the MC: this way, it can draw its overlay on top of it, or simply display its image on the screen when the main processor is not loaded or is asleep.

UART — a Linux terminal is connected to it, and the MCU, for example, can show the Linux boot log, even if the boot process failed long before the graphics were initialized or any drivers were loaded. It can even show just uboot

I2C — with two buses, one of which is dedicated to communication between the microcontroller and the SoC (through which it provides access to hid), and the second is shared, to which devices are connected that ensure the operation of the device but do not protrude outward — all kinds of DC-DC converters, port expanders, battery controllers, current meters, and so on.

The Soc has two USB ports — one is external (this is the side “main” USB), and the second is connected to a 4-port hub.

The following are connected to the internal hub: wifi/bt, lines on the m2 connector, lines on the debug connector, upper USB ports.

The controller can be either a USB device or a USB host, so the side connector can perform both of these roles, while the hub is only a host, so only devices can be connected to the upper USB ports.

The controller can also use USB Type-C alt mode, in which case a DisplayPort appears in the connector instead of USB.

## Main block scheme

Here we publish an overall diagram showing all the blocks.

## Buttons

## Bus (i2c, spi)

## GPIO Connectors

## Display

Custom IPS monochrome display

Funny RGB controller

## LEDs

## Touchpad

## Haptic

## Audio subsystem

## MCU

## SOC

## Power

### Charger

### Current meters

## USB system

Flipper One has several USB ports available to the user: one on the side and two on top. Additional USB devices can be connected via the GPIO connector and M.2 connector, but these are not ports, just data lines.

The port on the side is the main one. It is the most functional: it has PD input and output with different voltages, it can work as both a host and a device (you can connect devices to it and connect it to other devices, such as laptops), and it can switch to Display Port mode to show the image on a connected monitor.

<table isTableHeaderOn="true" columnWidths="165,165,165,168">
  <tr>
    <td lightBackgroundColor="rgb(242, 243, 245)" darkBackgroundColor="rgb(242, 243, 245)" align="left">
    </td>
    <td lightBackgroundColor="rgb(242, 243, 245)" darkBackgroundColor="rgb(242, 243, 245)" align="left">
      <p>Power</p>
    </td>
    <td lightBackgroundColor="rgb(242, 243, 245)" darkBackgroundColor="rgb(242, 243, 245)" align="left">
      <p>USB</p>
    </td>
    <td lightBackgroundColor="rgb(242, 243, 245)" darkBackgroundColor="rgb(242, 243, 245)" align="left">
      <p>Role</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p>⬅ Side USB-C [SCH]</p>
    </td>
    <td align="left">
      <p>PD 5-24V input-output</p>
    </td>
    <td align="left">
      <p>3.1+2.0</p>
      <p>alt DP</p>
    </td>
    <td align="left">
      <p>Host+Device</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p>]</p>
      <p><em>⬆</em> Top USB-C [</p>
      <p>SCH</p>
    </td>
    <td align="left">
      <p>PD 5v</p>
    </td>
    <td align="left">
      <p>3.1+2.0</p>
    </td>
    <td align="left">
      <p>Only Host</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p>]</p>
      <p><em>⬆</em> Top USB-A [</p>
      <p>SCH</p>
    </td>
    <td align="left">
      <p>5v</p>
    </td>
    <td align="left">
      <p>3.1+2.0</p>
    </td>
    <td align="left">
      <p>Only Host</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p>]</p>
      <p>USB in GPIO connector [</p>
      <p>SCH</p>
    </td>
    <td align="left">
      <p>3.3/5V power on connector</p>
    </td>
    <td align="left">
      <p>2.0</p>
    </td>
    <td align="left">
      <p>Only Host</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p>]</p>
      <p>USB in M.2 connector [</p>
      <p>SCH</p>
    </td>
    <td align="left">
      <p>3.3V power on connector</p>
    </td>
    <td align="left">
      <p>3.1+2.0</p>
    </td>
    <td align="left">
      <p>Only Host</p>
    </td>
  </tr>
</table>

## M2

M.2 slot specifications

Supported module types

## Ethernet

## Debug connectors

# Boot process

