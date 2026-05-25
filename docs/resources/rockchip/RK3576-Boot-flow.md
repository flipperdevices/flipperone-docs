---
title: RK3576 Boot flow
slug: resources/rockchip/boot-flow
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:30:14 GMT+0000 (Coordinated Universal Time)
---

The RK3576 starts from code stored in the SoC boot ROM. That code cannot be changed after manufacturing. It selects a boot source, looks for the first-stage Rockchip boot image on that storage device, and runs the early boot stages that bring up DRAM and load U-Boot.

For MaskROM recovery and image flashing commands, see [How to install a Linux image](../../cpu-software/How-to-install-linux-image.md).

***

## Boot source selection

At power-on, the boot ROM reads the `SARADC_VIN0_BOOT` strap to choose the boot priority list. The priority list is board-specific and may include storage such as eMMC, UFS, SD, SPI flash, SATA, or NVMe.

The boot ROM checks each storage device in priority order:

1. Read the boot-mode strap from `SARADC_VIN0_BOOT`.
2. Try the first storage device in the selected priority list.
3. Look for a valid Rockchip RKNS image signature at byte offset `0x8000`.
4. If the signature is missing or invalid, try the next device in the priority list.
5. If no bootable image is found, enter Rockchip MaskROM mode and wait for a host computer over the dedicated MaskROM USB port.

`0x8000` is the same physical byte offset on the storage device. On 512-byte sector devices such as SD or eMMC, this is sector 64. On 4096-byte sector devices such as UFS, this is sector 8.

***

## First-stage image

The first image loaded by the boot ROM is an RKNS-format image. On RK3576 this image may contain early binaries such as:

- `boost.bin`, used for early platform setup on boards that need it.
- `ddr.bin`, used to initialize and train DRAM.
- SPL, the U-Boot Secondary Program Loader. SPL runs after DRAM is available and locates the main U-Boot FIT image.

Older Rockchip documentation may refer to `miniloader` or `idbloader`. Those names are from older Rockchip boot stacks. For RK3576, modern upstream U-Boot produces `u-boot-rockchip.bin`, which contains the RKNS image and the FIT image at the expected offsets.

***

## U-Boot FIT image

After SPL is running, it loads the main U-Boot FIT image. The FIT offset is configured in SPL. A common default is byte offset `0x800000`.

The FIT image can contain:

- U-Boot proper.
- The device tree blob used by U-Boot.
- ARM Trusted Firmware BL31.
- An optional TEE-OS payload, also called BL32.

The FIT configuration decides which binaries are loaded and where they are placed in memory. SPL typically transfers control to BL31, which then enters U-Boot proper as BL33.

***

## Flash layout

The only fixed offsets needed by the boot ROM are the offsets for the first-stage RKNS image. The FIT image location is normally an SPL configuration detail.

Typical layout:

| Offset | 512-byte sectors | 4096-byte sectors | Contents |
| --- | --- | --- | --- |
| `0x8000` | 64 | 8 | RKNS first-stage image with early binaries and SPL |
| `0x800000` | 16384 | 2048 | U-Boot FIT image, if SPL is configured to load it from this common offset |

Modern U-Boot can package the RKNS image and the FIT image into one `u-boot-rockchip.bin` file with the required padding between them. In that case, users normally write one bootloader image instead of manually placing each part at a separate offset.

***

## Operating system handoff

Once U-Boot proper is running, the boot flow becomes a U-Boot policy decision rather than a boot ROM rule. Rockchip vendor U-Boot builds often use fixed boot commands. Depending on configuration, mainline U-Boot can use Standard Boot to scan available boot devices and partitions for supported boot methods.

Current Flipper test images boot through `extlinux.conf`. This may change as the Flipper One software stack develops.
