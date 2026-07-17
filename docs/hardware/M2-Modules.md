---
title: M.2 modules
slug: hardware/m2-port/modules
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:00:55 GMT+0000 (Coordinated Universal Time)
---

This page lists the categories of M.2 modules that can extend Flipper One's capabilities. We'll add more details to each category as the corresponding modules are developed and tested.

## About M.2 modules

M.2 modules are off-the-shelf expansion boards in the M.2 form factor (formerly NGFF), commonly used in laptops and industrial computers. The format covers a wide range of devices, which makes the M.2 port a flexible way to extend Flipper One's capabilities.

Flipper One uses a Key B connector exposing PCIe 2.1 ×1, USB 2.0 / 3.1, SATA3, UART, I²C, Serial Audio, and SIM + eSIM lines. Full pinout, supported sizes, and the schematic are on the [M.2 port](M2-port.md) page.

Some Flipper One M.2 modules also include a custom back cover that mounts SMA antennas and routes RF cables out of the device.

***

## Cellular modems

M.2 cellular modems add 4G/5G connectivity over a SIM or eSIM, turning Flipper One into a portable mobile-connected device.

***

## Wi-Fi adapters

M.2 Wi-Fi cards add wireless networking and, on most modules, Bluetooth as well.

The [ESP32-E22](https://www.espressif.com/en/products/socs/esp32-e22) is a Wi-Fi 6E and Bluetooth 5.4 co-processor from Espressif. It recently [passed Wi-Fi CERTIFIED 6E testing](https://www.espressif.com/en/news/E22_Wi-Fi_6E_Certificate) and ships with an [open-source Linux driver](https://github.com/espressif/esp32e22-linux-driver), which is why people keep asking us to add it here.

:::hint{type="warning"}
We can't confirm the ESP32-E22 fits Flipper One's M.2 port yet. Espressif's module, the [ESP32-E22-M2-1](https://www.espressif.com/en/products/modules?id=ESP32-E22), is an M.2 2230 card that lists SDIO 3.0 as a host interface alongside PCIe 2.1. SDIO is only wired on Key E sockets, not on Key B, and Espressif hasn't published the module's key type. Every SDIO-capable Wi-Fi/Bluetooth M.2 card we're aware of uses Key E for that reason, which would stop it from going into Flipper One's Key B slot at all.

The Linux driver currently uses PCIe for Wi-Fi and USB for Bluetooth, both of which Key B does carry. If a Key B version of this module shows up, it should work over those two interfaces. Until then, we're leaving the ESP32-E22 off the confirmed list.
:::

***

## SDR radios

Software-defined radio modules turn Flipper One into a portable SDR platform for receiving and transmitting across a wide range of frequencies. One example is the [sSDR by Wavelet Lab](https://www.crowdsupply.com/wavelet-lab/ssdr), though which revision you get matters for fit.

:::hint{type="warning"}
Flipper One's M.2 port is Key B only. The current sSDR Rev3 is keyed M (PCIe 3.0 ×4 + USB 2.0) and won't go into a Key B socket at all, since Key M sits at a different notch. The older Rev2 is keyed B+M (PCIe 2.0 ×2 + USB 2.0), so it does fit mechanically, but Flipper One only wires a single PCIe lane. Best case, the card links down to PCIe ×1 with less bandwidth than on a native ×2 slot; worst case, it needs both lanes and won't link up. USB 2.0 works over Key B's USB pins on either revision. See [Wavelet Lab's own specs](https://docs.wsdr.io/hardware/ssdr.html) for the full breakdown.
:::

***

## Satellite (NTN) modems

M.2 NTN (Non-Terrestrial Network) modems provide connectivity through satellites and high-altitude platforms. Standardized by 3GPP (3rd Generation Partnership Project) as part of 5G and LTE specifications. Learn more about [Satellite modems](M2-satellite-modem.md).

***

## GNSS receivers

M.2 GNSS modules add satellite positioning (GPS, GLONASS, Galileo, BeiDou) for location-aware applications. Learn more about [GNSS receivers](M2-gnss-receiver.md).

***

## NVMe SSDs

M.2 NVMe SSDs add fast onboard storage over PCIe for logging, captured RF data, or large datasets.

***

## AI accelerators

M.2 AI accelerators (NPUs / TPUs) offload on-device inference for vision, audio, and signal-processing workloads.
