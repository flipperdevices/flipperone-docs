---
title: Flipper OS
slug: cpu-software/flipper-os
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Thu Aug 13 2026 12:00:00 GMT+0000 (Coordinated Universal Time)
---

**Flipper OS** is a Linux-based operating system we are developing for Flipper One. It's an additional layer on top of a standard Debian-based Linux system that lets you switch between multiple preconfigured OS profiles for different tasks, so you can experiment freely without worrying about breaking your setup or turning it into a mess.

This page outlines the core concept behind Flipper OS: what we want to build, and why.

***

::embed[]{url="https://www.youtube.com/watch?v=yFCLM971Upw"}

## What we want to build into Flipper OS

- **OS profiles** — preconfigured OS images for different tasks, such as a network router, a radio lab, a desktop computer, and a TV media box. Each profile has its own settings, kernel, device tree, and set of applications.
- **An unbreakable playground** — clone any profile and modify anything inside it, from the kernel to system files, without worrying about breaking the device.
- **Reset to default** — roll back your changes and return a profile to its clean, default state at any time.
- **Atomic updates** — no matter how badly a profile has been broken, it should still be possible to update it to a new version reliably.

***

## Why not just customize another OS?

Why build Flipper OS, yet another operating system, when there are already so many? Why not simply take a standard Debian-based system — the way Raspberry Pi does — and customize it?

Conventional Linux distributions are designed for traditional computers and servers. They aren't convenient for a multitool like Flipper One, which can be a network router, a radio lab, a desktop computer, or a TV media box, all on the same device.

***

## The messy system problem

When you try to use any Linux-based SBC as a universal "on-the-go" tool and keep changing its purpose over time — for example using it as a media server, a Wi-Fi router, or a desktop — **you eventually end up with a messy system**. You install so many packages and modify so many system configuration files that, at some point, reconfiguring the system becomes harder than reinstalling the OS and rebuilding the entire setup from scratch.

![A typical scenario with the common approach](/files/pics/linux-os-classic-problem.png "A typical scenario with the common approach")

Containers such as Docker solve part of this problem, but only for user-space applications. They work well when you need to isolate an application, but not when you need to work close to the bare metal: patch the kernel, modify the device tree, reconfigure an HDMI port or Wi-Fi driver, or bit-bang GPIOs. In these cases, you need full access to the hardware — something containers can't give you.

Flipper OS is designed to resolve the messy system problem. To better understand what Flipper OS does and why, let's first look at other ways to approach this problem.

## Common approach and its issues

One approach to the messy system problem is to use separate SD cards for different preconfigured setups. However, juggling SD cards is inconvenient and does not scale well.

Issues with the SD card approach:

* **Cannot restore configuration to default.** The only way to revert to default settings is to reinstall the operating system.
* **Single configuration state, no alternative profiles, and no recovery points.** The system has only one current configuration. Once you modify config files or install packages, the previous state is lost. You cannot easily switch between setups, save working versions, or roll back after breaking something.
* **Easy to break the system.** Small changes, incorrect packages, or edits to config files can easily make the system unstable or cause it to stop working correctly.
* **No atomic updates.** If an update fails midway, the system can end up in a partially updated or broken state. Updates may also conflict with modified system config files, and newer packages can conflict with your customized environment.

***

## What is Flipper OS?

Flipper OS is not exactly an operating system, but rather a higher-level toolset that enables centralized management of OS profiles from a single device. You can think of it as similar to Docker containers, but without virtualization — offering full access to bare metal.

Ultimately, we aim to create a tool that hardware hackers can use to build their own versatile Linux boxes for various tasks, and share the resulting images with the community. We want Flipper OS to be usable not just on Flipper One, but on other platforms too.

***

## Flipper OS architecture

Flipper OS introduces the concept of **operating system profiles**, which are architecturally separated from the base system.

Thus, the operating system consists of two distinct parts:

**Flipper OS base system** — a clean, unmodified Debian-based system. It consists of `Linux kernel`, `RootFS`, and `MCU firmware`. The base system is distributed through official updates. This part of the operating system remains unchanged during user customization and configuration.

**OS profiles** — an overlay on top of the base system that contains all user customizations, including installed packages, containers, and modifications to the RootFS including config files edits. By applying an OS profile to the Flipper OS base system, you get a fully configured system tailored for a specific use case.

- **Official built-in OS profiles** are distributed as part of the operating system, for example: `Minimal system`, `Wi-Fi router`, `TV media box`, `Network sniffer`, and `Desktop`.

- **User OS profiles** contain user-modified packages and RootFS changes. Users configure the system in the usual way by editing configs and installing packages using a package manager. The process remains fully transparent to the user, while all changes are automatically stored inside the active profile. In addition to OS profiles, users can separately store personal files such as media files, documents, and other data not related to the operating system.

  User OS profiles can be stored on removable media, allowing users to select and boot a profile from the boot menu, for example from an SD card.

![Flipper OS architecture](/files/pics/flipper-os-architecture.png "Flipper OS architecture")

***

## OS profile selection at boot

An operating system profile can be selected directly from the boot menu without connecting an external monitor or keyboard. The menu also allows users to clone profiles and restore them to their original preconfigured state, and it shows each profile's last-used timestamp.

![Boot menu with OS profile selection](/files/pics/flipper-os-switching-os-profile-on-boot.png "Boot menu with OS profile selection")

Official built-in OS profiles cannot be deleted, but they can be cloned and used as a base for creating user profiles. At any time, a profile can be quickly reset to the default state of the original official built-in OS profile.

***

## Boot stages

Flipper One has a dual-processor architecture (MCU + CPU), so you can interact with the device via its LCD screen and buttons even when Linux and the CPU are powered off. Because of this, the device goes through several distinct stages before an OS profile is up and running:

- **MCU Mode** — the CPU and Linux are powered down, and only the microcontroller firmware is active. It starts the CPU and hands over control of the screen to the software running at the CPU level.
- **Boot Menu** — a standalone program that runs on the CPU and displays the OS profile selection menu; the full Linux system hasn't loaded yet. The boot menu can render graphics on the LCD screen and process button input, read profile metadata such as size and last-used date, and manage profiles by resetting, deleting, or cloning them. We currently use U-Boot for this; in the future, we plan to switch to a lightweight Linux distribution with the boot menu program compiled into it.
- **Profile started** — the selected OS profile is now running as a full-fledged operating system without restrictions. See [Unbreakable profiles](#unbreakable-profiles) below.

:::hint{type="info"}
See [Operation modes](../user-interface/Operation-modes.md) for the full set of Flipper One's power and display states, including Power OFF and Linux Mode.
:::

***

## Unbreakable profiles

We want to give you complete freedom within a loaded profile — the ability to break and tinker with the system however you please: installing packages, modifying system files, and altering the kernel and device tree. That means a profile's root filesystem must be writable, with no restrictions placed on the user.

At the same time, we want the ability to roll back all changes and revert a profile to its default state. All modifications to the original profile are stored on a separate overlay layer, which can be deleted to reset the profile to default.

Changes are saved seamlessly, without the need to run specific commands to preserve them: if you keep booting into the same profile and modifying it, those **changes persist across reboots** — just as they would on a standard, traditional operating system.

***

## Managing OS profiles on running system

On a running system, the user can:

- View the current OS profile info, including the profile name, size, creation date, modification date, and other details.
- Clone the built-in OS profile or rename the user OS profile.
- Delete the user OS profile or reset a built-in OS profile to its default state.

![Managing OS profiles on running system UI](/files/pics/flipper-os-managing-os-profile-on-running-system.png "Managing OS profiles on running system UI")

***

## Cloning and sharing profiles

Say you've spent a long time fine-tuning a `Router` profile and you're happy with the result. From the boot menu, you can select `Edit`, clone the profile, and save it under a unique name, such as `[MyTravelRouter]`. We call this a **user profile**, and mark it by enclosing its name in square brackets to distinguish it from the built-in profiles.

:::hint{type="info"}
The bracket notation (`[Name]`) is the boot menu's display naming for user profiles. At the command-line level, profiles use a separate `@Name` convention — see [Profiles CLI](profiles.md) for the CLI reference.
:::

With this approach, you don't have to worry about losing a successful configuration — you can keep experimenting in a separate profile, similar to working with branches in Git.

We'd also like to let users share their profiles with the community, so others can download and use them, along with deduplication so the same file isn't stored twice on disk across different profiles.

:::hint{type="warning"}
**Not yet implemented.** Community profile sharing and deduplication are goals we want to build toward, not current features.
:::

***

## User data and volatile files

User data needs to be accessible from all profiles, so a portion of the filesystem must remain independent of any single profile. For instance, if you download a video to `/home/user/Downloads` in the `Desktop` profile, you should be able to watch it later from the `TV Media Box` profile.

We're leaning towards keeping `/home/user` tied to a specific profile, with only a single shared folder — such as `/home/user/user_data` — common to all profiles.

:::hint{type="warning"}
**Open question.** We haven't yet decided how to handle other volatile, profile-generated data, such as caches and settings. For example, should a Wi-Fi password saved in one desktop profile be available in another? Making all of `/home` shared would prevent distinct per-profile configurations and cause conflicts, so we're leaning against that — but the exact boundary is still undecided.
:::

***

## System update

The main challenge with the entire Flipper OS concept lies in system updates: how do we release new profile versions and deploy them over existing ones, when the user has root access and multiple cloned profiles?

We don't want updating to be a complex migration between versions that could easily fail — a standard `apt upgrade` is unpredictable, and you never know where things might break when upgrading to a new distribution version. Ideally, we need an atomic update that guarantees a predictable transition to a new profile version.

:::hint{type="warning"}
**As of now, there is no solution to this problem.** We're experimenting with several approaches, including the [OSTree](https://ostreedev.github.io/ostree/) approach and testing [Btrfs](https://btrfs.readthedocs.io/en/latest/) images.
:::

***

## Join the development

We invite you to join the discussion and help us work through these open problems — from the update mechanism to how shared data should work.

See [how to join the development](../How-to-join.md) to get started.
