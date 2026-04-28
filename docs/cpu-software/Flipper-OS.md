---
title: Flipper OS
slug: cpu-software/flipper-os
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:17:42 GMT+0000 (Coordinated Universal Time)
---

We are building a highly open and user-friendly Linux distribution for the Flipper One, based on the latest mainline kernel, featuring atomic updates and OS profiles (overlays), as well as Flipper One's advanced features. We call it **Flipper OS**.

While Flipper OS is still under active development, we are currently validating Flipper One hardware using temporarily patched Debian OS builds. You can also try running these builds on a compatible RK3576-based board. You can also contribute by testing OS builds or developing code. A Flipper One is not required — the OS runs on various affordable single-board computers (SBCs). Learn more on the [How to install an image](How-to-install-an-image.md) page.

This page provides an overview of the key features of the future operating system.

## Open Linux distribution

Our goal is to build a fully open Linux distribution for the Flipper One, based on the latest mainline kernel and containing zero proprietary blobs. Achieving this on a modern SoC (System-On-Chip) is extremely challenging, as chip vendors in the consumer segment typically keep the source code for early boot stages and hardware drivers closed. Nevertheless, our current RK3576 mainline Linux build supports a wide range of features.

![Current status of Linux distribution and our goal](/files/pics/flipper-os-current-status-and-our-goal.png "Current status of Linux distribution and our goal")

While achieving 100% code openness is not possible (for example, due to the immutable boot ROM embedded in the SoC), we will continue working together with the community toward this goal.

## OS profiles

Operating system profiles let you load a preconfigured environment by selecting an OS profile during the device’s early boot stage without connecting an external monitor and keyboard. The menu also lets you clone profiles and restore them to their original preconfigured state.

![Flipper OS profiles menu](/files/pics/flipper-os-profiles-menu.jpg "Flipper OS profiles menu")

A list of built-in OS profiles:

- **Router Profile.** A system preconfigured to work with two wired ISPs, a Wi-Fi client + AP, and a 5G modem. It can share internet via a Wi-Fi hotspot, connect securely to a home NAS, and be controlled with a low-power display and physical buttons.
- **TV Media Box.** A system with a media player, DLNA server, automatic content metadata fetching, arcade game emulation, and support for popular game controllers.
- **Desktop Computer.** A full desktop environment based on Wayland, with support for 4K @ 120 Hz and hardware-accelerated 2D/3D graphics.
- **Minimal Profile.** A lightweight system without a GUI, containing only a basic set of packages for maximum performance and efficiency.
- **Network Multitool Profile.** A system with quick access to network diagnostics and traffic analysis tools such as `nmap`, `tcpdump`, `tshark`, `iperf`, `netcat`, and more.

And of course, you can create your own custom profiles for any use case.

## A/B atomic updates

In most Linux distributions, the update system is not fully reliable. If an error occurs during an update, the operating system can end up in an inconsistent state, where some files are updated and others are not.

![FlipCTL GUI demo](/files/pics/flipper-os-ab-updating.jpg "A/B update flow diagram")

In Flipper OS, updates are atomic. If an error occurs during installation, the system automatically rolls back to the previous working version.

## FlipCTL

FlipCTL is a lightweight GUI framework for embedded and headless Linux systems, designed as a modern replacement for traditional HMI solutions. Originally built for Flipper One, it runs on any Linux system — from servers and routers to single-board computers — with no desktop environment required.

![FlipCTL GUI demo](/files/pics/flipctl-nmap-wrapper.jpg "FlipCTL GUI demo (nmap wrapper)")

The core idea: instead of running a desktop GUI (GNOME, KDE) on a tiny screen, FlipCTL provides a pixel-rendered, navigation-friendly interface. Learn more about FlipCTL on a [dedicated page](FlipCTL.md).

## Flipper One features support

Flipper One hardware features supported in Flipper OS that are rarely found on typical Linux PCs:

- **Built-in display, buttons, and touchpad.** Flipper OS can use the built-in display as a small monitor, handle button events for UI navigation, and use the touchpad for cursor control and for text input via an on-screen keyboard. Wrappers for common Linux tools provide a UI optimized for the built-in display.
- **Advanced power monitoring.** Flipper One includes a battery gauge for charge and discharge currents measurement, multiple current and voltage sensors, and temperature sensors. All these parameters are available within Flipper OS.
- **Expansion module interface access.** From Linux user space, you can control GPIO pins and low-speed interfaces such as UART, SPI, I²C, CAN, and S/PDIF. Two pins can also be used as ADC inputs, PWM outputs, or PIO (Programmable Input/Output).
- **Built-in microphone and speaker.** Audio input and output are available in the operating system. A 3.5mm jack supports automatic switching and headset button.
