---
title: GPIO modules
slug: hardware/gpio-port/modules
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 12:59:53 GMT+0000 (Coordinated Universal Time)
---

This page showcases hardware modules that can be created for Flipper One and connected via the GPIO port. Two modules are currently documented: the walkie-talkie module and the camera module.

***

## Walkie-talkie module

This module enables communication over standard VHF frequencies with walkie-talkies using the Flipper One microphone, speaker, and PTT button. It is built around an SA828-based walkie-talkie radio module.

![Walkie-talkie module structural diagram](../files/pics/walkie-talkie-module.png)

The module connects to Flipper One via the GPIO header's USB 2.0 pins (D+, D-, 5V, GND) and carries microphone audio, speaker audio, and a PTT control signal between Flipper One and the radio. RF transmission and reception go through an external antenna attached to the SA828 module.

***

## Camera module

Flipper One's Linux OS recognizes the module as a standard USB webcam, making it available for taking pictures and recording videos. The camera module is based on a typical USB webcam, connecting via the USB 2.0 pins (D+, D-) and powered through the 5V output pins on the GPIO header.

![Camera module structural diagram](/files/pics/camera-module.png)
