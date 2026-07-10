---
title: NTN satellite modems
slug: testing/network/satellite
---

This page contains tests for non-terrestrial network (NTN) satellite modems — modules that provide satellite connectivity.

![](/files/pics/flipperone-ntn-module.jpg)

## Blues Notecard for Skylo (NOTE-NBGLWX)

::Image[]{src="/files/pics/m2-notecard-for-skylo.jpg" size="40" position="flex-start" caption="Caption text"}

[Blues Notecard for Skylo](https://shop.blues.com/collections/notecard/products/notecard-for-skylo) is an M.2 E-key module (30 × 42 mm) that supports NTN NB-IoT satellite connectivity, terrestrial LTE, Wi-Fi, and GNSS positioning. It features a built-in eSIM and a SIM multiplexer that allows switching between the integrated eSIM and an external SIM card. For details see the [official datasheet](https://dev.blues.io/datasheets/notecard-datasheet/note-nbglwx/).

The module provides satellite connectivity through [Skylo](https://www.skylo.tech/). Current satellite service coverage is available on the [Skylo coverage map](https://www.skylo.tech/resources/geographical-coverage).

The module is not designed for broadband internet access. Instead, it is intended for low-bandwidth IoT applications that exchange small amounts of data over satellite networks at infrequent intervals.

## Connecting the module to Flipper One

The NOTE-NBGLWX module cannot be installed directly inside Flipper One because it uses an M.2 Key E connector, while Flipper One provides an M.2 Key B slot.

For testing, the module was connected to a [Notecarrier CX v1.7](https://dev.blues.io/datasheets/notecarrier-datasheet/notecarrier-cx-v1-7/) board, which was connected to the Flipper One GPIO port through a protoboard.

**Power:** 5 V supplied by the Flipper One GPIO port.

**Interface:** Notecard AUX UART (115200 8N1).

:::hint{type="info"}
In future, we plan to use satellite modems with an M.2 Key B connector so they can be installed directly inside Flipper One.
:::

## Testing NTN Connectivity

![](/files/pics/ntn-module-test-diagram.jpg)

Data transmitted from the module over NTN NB-IoT is received by Blues Notehub service, where it can be viewed, processed, or forwarded to your own backend using the [Notehub API](https://dev.blues.io/api-reference/notehub-api/api-introduction/). Downlink messages follow the same path in reverse: data is sent to Notehub, which delivers it to the module over the Skylo satellite network.


The following antennas were used during testing:
* **NTN antenna:** [Quectel YFCA011](https://www.quectel.com/product/yfca011aa-5g-adhesive-mount-fpc-cable-dipole-embedded-antenna/) (120x47 mm).
* **GNSS antenna:** generic 1559-1609 MHz.

During testing, the module transmitted messages containing sample telemetry: two floating-point values representing temperature and humidity.

Extended logging was enabled on the NTN module, providing a detailed trace of the communication between the module's MCU and the NTN modem using AT commands. The trace includes information about the cellular network, satellite connection, and the synchronization process.

See the [complete test log](https://cdn.flipper.net/notecard_2026-07-03T15_00_07.log.txt).
