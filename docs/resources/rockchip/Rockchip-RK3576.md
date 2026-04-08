---
title: Rockchip RK3576
slug: resources/rockchip
docTags: 
createdAt: Tue Apr 07 2026 18:42:40 GMT+0000 (Coordinated Universal Time)
updatedAt: Wed Apr 08 2026 12:25:44 GMT+0000 (Coordinated Universal Time)
---

This section contains technical resources and documentation for the Rockchip RK3576 processor used in Flipper One.

## Maskrom

In maskrom mode, when miniloader in not loaded in RAM, device does not printing anything in UART.

How to find maskrom device via `lsusb`:

`ID 2207:350e Fuzhou Rockchip Electronics Company  ## <--- Maskrom device`

## Test maskrom device

1. Build latest rkdeveloptool [**https://github.com/rockchip-linux/rkdeveloptool**](https://github.com/rockchip-linux/rkdeveloptool)
   Possible options:

```javascript
./rkdeveloptool

---------------------Tool Usage ---------------------
Help:                   -h or --help
Version:                -v or --version
ListDevice:             ld
DownloadBoot:           db <Loader>
UpgradeLoader:          ul <Loader>
ReadLBA:                rl  <BeginSec> <SectorLen> <File>
WriteLBA:               wl  <BeginSec> <File>
WriteLBA:               wlx  <PartitionName> <File>
WriteGPT:               gpt <gpt partition table>
WriteParameter:         prm <parameter>
PrintPartition:         ppt
EraseFlash:             ef
TestDevice:             td
ResetDevice:            rd [subcode]
ChangeStorage:          cs [storage: 1=EMMC, 2=SD, 9=SPINOR]
ReadFlashID:            rid
ReadFlashInfo:          rfi
ReadChipInfo:           rci
ReadCapability:         rcb
PackBootLoader:         pack
UnpackBootLoader:       unpack <boot loader>
TagSPL:                 tagspl <tag> <U-Boot SPL>
-------------------------------------------------------
```

2. Check if maskrom device visible:

```javascript
./rkdeveloptool ld
DevNo=1 Vid=0x2207,Pid=0x350e,LocationID=102    Maskrom
```

3. Upload loader into device RAM
   You can get `rk3576_spl_loader.bin` file here [**https://dl.radxa.com/rock4/4d/images/rk3576\_spl\_loader.bin**](https://dl.radxa.com/rock4/4d/images/rk3576_spl_loader.bin)
   At this moment devices will print into UART

```javascript
# ./rkdeveloptool db ./rk3576_spl_loader.bin
 Downloading bootloader succeeded.
```

