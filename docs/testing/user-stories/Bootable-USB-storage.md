---
title: Bootable Virtual USB mass storage / ISO mount
slug: testing/user-stories/bootable-usb-storage
docTags: 
---

## Description

Flipper One can expose a virtual USB mass storage device to the target machine. The user can store multiple bootable ISO images on Flipper One's internal storage and select which one to present to the target at boot time without re-formatting a drive or physically swapping media.

## Status

Possible using Flipper One.

## User story

I need to reinstall the OS on a server, boot a recovery environment, or test multiple Linux distros without hunting for USB sticks or repeatedly flashing drives. I store several ISO images on Flipper One and mount whichever I need as a virtual bootable USB. The target machine sees it as a physical drive and boots from it directly. I can switch ISOs between reboots from the Flipper One interface without touching the target machine.

Inspiration: Ventoy

