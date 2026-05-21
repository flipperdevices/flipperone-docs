---
title: RK3576 Boot flow
slug: resources/rockchip/boot-flow
docTags:
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:30:14 GMT+0000 (Coordinated Universal Time)
---

This page describes the RK3576 boot flow, the bootloader stages used on Rockchip-based systems, and the flash layout used to store the boot images.

The main point is that the CPU does not start by reading Linux, a filesystem, or a normal partition. After reset, the CPU starts executing the immutable BootROM inside the SoC. BootROM reads the first external boot image from a fixed raw offset in flash, loads it into internal SRAM, and transfers execution to it. Only later, after DRAM is initialized, can larger boot images such as U-Boot and the Linux kernel be loaded.

## Bootloader structure

![RK3576 bootloader structure](/files/pics/rk3576-bootloader-structure.png "RK3576 bootloader structure")

The RK3576 boot chain is built from several stages. Each stage has a narrow responsibility and prepares the system for the next one.

```text
BootROM
  -> idbloader.img
      -> TPL / DDR initialization code
      -> SPL or Rockchip miniloader
  -> u-boot.itb or vendor uboot.img + trust.img
      -> BL31 / TF-A
      -> optional OP-TEE
      -> U-Boot proper
  -> Linux kernel + Device Tree
  -> root filesystem
```

### BootROM

BootROM is the first code executed by the CPU after reset. It is stored inside the RK3576 SoC and cannot be modified in normal flash.

BootROM performs the initial boot source selection, reads the Rockchip boot image header from the selected boot device, loads the first external bootloader image into internal SRAM, and jumps to it.

At this stage, DRAM is not initialized. This is why BootROM can only load a small early loader into SRAM.

### TPL

TPL means **Tertiary Program Loader**. In the open-source U-Boot flow, TPL is the earliest U-Boot stage executed after BootROM.

The main purpose of TPL is very early hardware setup, especially DRAM initialization. Without this step, the system cannot load larger images into RAM.

On Rockchip platforms, the equivalent role may also be performed by a proprietary Rockchip DDR initialization binary.

### SPL

SPL means **Secondary Program Loader**. It runs after TPL or after the equivalent early DDR initialization code.

SPL is a small, limited U-Boot build. It is not a full interactive bootloader. It normally does not provide the complete U-Boot shell, command set, filesystem support, or board-level boot logic.

Its main responsibility is to load the next boot image from flash into DRAM. In the mainline U-Boot flow, that next image is usually `u-boot.itb`.

### BL31 / TF-A

BL31 is part of Arm Trusted Firmware-A. It runs at EL3 and provides secure monitor functionality and low-level platform runtime services.

BL31 can handle operations such as CPU power state transitions, suspend/resume support, and other platform-specific secure monitor calls used by the non-secure operating system.

In the mainline U-Boot flow, BL31 is usually packed into `u-boot.itb` together with U-Boot proper.

### OP-TEE

OP-TEE is an optional Trusted Execution Environment. It is used only when the platform needs a secure OS for trusted applications.

OP-TEE is not required for a basic non-secure Linux boot. If the board does not use a trusted signed boot chain or secure applications, this stage can be absent.

### U-Boot proper

U-Boot proper is the full bootloader stage. It runs after the early loader stages have initialized DRAM and loaded the larger boot payload.

U-Boot proper can initialize additional devices, read filesystems and partitions, process environment variables and boot scripts, load the Linux kernel, load the Device Tree Blob, load an initramfs if required, pass boot arguments, and start Linux.

## idbloader vs miniloader

`idbloader.img` and `miniloader` are not the same thing.

`idbloader.img` is the image read by BootROM from flash. It is a Rockchip boot image container placed at a fixed raw offset.

`miniloader` is a Rockchip proprietary early loader implementation that can be stored inside `idbloader.img`.

In other words:

```text
idbloader.img = boot image / container read by BootROM
miniloader    = one possible proprietary loader inside idbloader.img
TPL + SPL     = open-source U-Boot alternative inside idbloader.img
```

There are two common boot flows.

### Open-source U-Boot TPL/SPL flow

```text
idbloader.img = TPL + SPL
u-boot.itb    = BL31 / TF-A + U-Boot proper
```

This is the common mainline U-Boot structure.

### Rockchip vendor miniloader flow

```text
idbloader.img = DDR init binary + Rockchip miniloader
uboot.img     = vendor U-Boot image
trust.img     = trusted firmware payload
```

This structure is usually seen in Rockchip vendor SDKs and vendor flashing tools.

## SD/eMMC flash layout

![RK3576 SD/eMMC flash layout](/files/pics/rk3576-flash-layout.png "RK3576 SD/eMMC flash layout")

For SD/eMMC-style boot media, the early Rockchip boot images are stored at raw sector offsets. These offsets are used before U-Boot starts reading normal partitions or filesystems.

| Component | Rockchip write offset | Sector offset | Byte offset | Purpose |
|---|---:|---:|---:|---|
| Reserved area / partition table area | `0x0000` | `0` | `0x000000` | Space before the Rockchip loader area |
| `idbloader.img` | `0x40` | `64` | `0x008000` / `32 KiB` | First external image loaded by BootROM |
| `u-boot.itb` | `0x4000` | `16384` | `0x800000` / `8 MiB` | BL31 / TF-A + U-Boot proper |
| `boot.img` or boot partition | `0x8000` | `32768` | `0x1000000` / `16 MiB` | Kernel, DTB, initramfs, or boot files |
| `rootfs.img` or rootfs partition | `0x40000` | `262144` | `0x8000000` / `128 MiB` | Linux root filesystem |

Example write commands for the mainline U-Boot flow:

```bash
dd if=idbloader.img of=/dev/sdX seek=64 conv=notrunc
dd if=u-boot.itb of=/dev/sdX seek=16384 conv=notrunc
sync
```

Equivalent Rockchip tool offsets:

```bash
rkdeveloptool wl 0x40 idbloader.img
rkdeveloptool wl 0x4000 u-boot.itb
```

The important detail is that `0x40` and `0x4000` are sector-based Rockchip write offsets, not byte offsets. With 512-byte sectors, `0x40` equals `32 KiB`, and `0x4000` equals `8 MiB`.

## Vendor miniloader flash layout

The Rockchip vendor miniloader flow commonly uses separate `uboot.img` and `trust.img` images.

| Component | Rockchip write offset | Sector offset | Byte offset | Purpose |
|---|---:|---:|---:|---|
| `idbloader.img` | `0x40` | `64` | `0x008000` / `32 KiB` | DDR init binary + Rockchip miniloader |
| `uboot.img` | `0x4000` | `16384` | `0x800000` / `8 MiB` | Vendor U-Boot image |
| `trust.img` | `0x6000` | `24576` | `0xC00000` / `12 MiB` | Trusted firmware payload |
| `boot.img` | `0x8000` | `32768` | `0x1000000` / `16 MiB` | Kernel or Android-style boot image |
| `rootfs.img` | `0x40000` | `262144` | `0x8000000` / `128 MiB` | Root filesystem |

This layout is mostly relevant when using Rockchip vendor tools and vendor bootloader binaries. For a mainline U-Boot flow, `trust.img` is normally not written separately because BL31 is packed into `u-boot.itb`.

## SPI flash boot layout

SPI NOR boot should not be treated as identical to SD/eMMC boot.

For SPI flash, U-Boot commonly generates a combined image named:

```text
u-boot-rockchip-spi.bin
```

This image is written from the beginning of SPI flash:

```bash
sf probe
sf update $fileaddr 0 $filesize
```

The combined SPI image contains the early Rockchip boot image and the later U-Boot payload arranged for SPI boot. The SD/eMMC offsets such as `0x40` and `0x4000` should not be blindly reused for SPI NOR.

## How the CPU reads flash during boot

![RK3576 CPU flash read sequence](/files/pics/rk3576-cpu-flash-read-sequence.png "RK3576 CPU flash read sequence")

The CPU executes the boot process in stages:

1. The CPU starts executing BootROM from inside the RK3576 SoC.
2. BootROM probes the selected boot device.
3. BootROM reads the Rockchip boot header and `idbloader.img` from the fixed loader offset.
4. BootROM loads the early code into internal SRAM.
5. The early loader initializes DRAM.
6. SPL or miniloader reads the next boot image from flash.
7. U-Boot proper starts from DRAM.
8. U-Boot reads the kernel, Device Tree, and optional initramfs.
9. U-Boot transfers execution to the Linux kernel.

Before DRAM initialization, the boot process is constrained by SRAM size. After DRAM initialization, the system can load larger images and use more complex boot logic.

## Summary

For the mainline U-Boot flow, the most important SD/eMMC offsets are:

```text
idbloader.img : sector 64    / Rockchip offset 0x40   / 32 KiB
u-boot.itb    : sector 16384 / Rockchip offset 0x4000 / 8 MiB
```

`idbloader.img` is the image read by BootROM. `miniloader` is only one possible proprietary loader implementation inside that image. In the open-source U-Boot flow, `idbloader.img` contains TPL/SPL instead.

## References

- U-Boot Rockchip documentation: https://docs.u-boot.org/en/latest/board/rockchip/rockchip.html
- U-Boot README.rockchip source: https://github.com/u-boot/u-boot/blob/master/doc/README.rockchip
- Rockchip open source boot option documentation: https://opensource.rock-chips.com/wiki_Boot_option
