---
title: RK3576 Boot flow
slug: resources/rockchip/boot-flow
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Thu May 21 2026 00:00:00 GMT+0000 (Coordinated Universal Time)
---

This page describes the cold-boot sequence of the Rockchip RK3576 SoC used in Flipper One: from the on-chip Boot ROM through DDR initialization, SPL, the FIT-packaged main bootloader (U-Boot + ARM Trusted Firmware), and finally the operating system. It also documents the on-flash layout that the Boot ROM and SPL rely on.

The legacy [Rockchip Boot option wiki](https://opensource.rock-chips.com/wiki_Boot_option) covers older SoCs (RK33xx and earlier) and uses obsolete terminology (`miniloader`, `idbloader`) that is **not** part of the current RK3576 stack.

***

## Overview

```mermaid
flowchart TD
  A[Power-on / reset] --> B[On-chip Boot ROM]
  B -->|Enumerate boot sources<br/>per SARADC_VIN0 strapping| C{Valid RKNS at<br/>byte offset 0x8000?}
  C -- No on any device --> M[Maskrom mode<br/>USB upload]
  C -- Yes --> D[RKNS image<br/>boost.bin → ddr.bin → SPL]
  D -->|DDR trained,<br/>SPL running in DRAM| E[Load FIT image<br/>default offset 0x800000]
  E --> F[BL31 / TF-A]
  F --> G[U-Boot proper]
  G -->|Standard Boot<br/>extlinux.conf / EFI / PXE| H[Linux kernel + rootfs]
```

***

## Stage 1 — On-chip Boot ROM

The Boot ROM is mask-programmed silicon that runs the moment power is applied to the RK3576. It is responsible for:

1. Reading the **`SARADC_VIN0`** strapping pin to determine the priority order of boot sources. Typical orderings are `eMMC → SD → Maskrom` or `UFS → SD → Maskrom`, depending on the board design.
2. Walking the boot-source list and, for each device, looking for a valid **RKNS** image signature at **byte offset `0x8000`**.
3. Falling back to **Maskrom mode** (USB upload from a host PC) if no bootable device is found.

:::hint{type="info"}
The `SARADC_VIN0` pin samples an analog voltage divider on the board; the divider ratio encodes the boot-priority configuration. See the RK3576 TRM, chapter *Boot configuration*, for the full table of recognized voltage ranges.
:::

For details on entering and using Maskrom mode, see :Link[Rockchip RK3576 — Maskrom]{href="./Rockchip-RK3576.md#maskrom" newTab="false" hasDisabledNofollow="true"}.

***

## Stage 2 — RKNS image (early bootloaders)

The RKNS (Rockchip Boot Image) container is loaded by the Boot ROM into on-chip SRAM and executed in place. On older Rockchip SoCs this stage was split between a TPL (DDR init) and an SPL (bootloader hand-off); on RK3576 the equivalent functionality is delivered as a small set of binaries bundled into one RKNS image, executed in order:

<table isTableHeaderOn="true" columnWidths="180,480">
  <tr>
    <td><p><strong>Binary</strong></p></td>
    <td><p><strong>Purpose</strong></p></td>
  </tr>
  <tr>
    <td><p><code>boost.bin</code></p></td>
    <td><p>Patches parts of the Boot ROM code already loaded in SRAM and configures power-mode parameters for UFS flash. Optional on boards that do not boot from UFS.</p></td>
  </tr>
  <tr>
    <td><p><code>ddr.bin</code></p></td>
    <td><p>Initializes the DDR memory controller and runs RAM <em>training</em> (timing calibration). After this stage DRAM is usable.</p></td>
  </tr>
  <tr>
    <td><p><code>SPL</code></p></td>
    <td><p>U-Boot Secondary Program Loader. Runs from DRAM, re-discovers the boot device, and loads the FIT-packaged main bootloader.</p></td>
  </tr>
</table>

:::hint{type="warning"}
On RK3576 the `ddr.bin` produced by Rockchip is a closed-source binary blob — there is currently no open-source replacement. This is tracked in :Link[flipperone-linux-build-scripts#56]{href="https://github.com/flipperdevices/flipperone-linux-build-scripts/issues/56" newTab="true" hasDisabledNofollow="false"}.
:::

***

## Stage 3 — FIT image (main bootloader)

Once SPL is running in DRAM it loads the **main bootloader FIT image** from a fixed offset on the boot device — by default **byte offset `0x800000`**. The exact offset is hard-coded in the SPL build configuration and can be changed at compile time.

The FIT image is a Flattened Image Tree container (`u-boot.itb`) that may include any combination of:

<table isTableHeaderOn="true" columnWidths="180,480">
  <tr>
    <td><p><strong>Component</strong></p></td>
    <td><p><strong>Role</strong></p></td>
  </tr>
  <tr>
    <td><p><strong>DTB</strong></p></td>
    <td><p>Device tree blob describing on-board peripherals to U-Boot and (later) Linux.</p></td>
  </tr>
  <tr>
    <td><p><strong>U-Boot proper</strong></p></td>
    <td><p>The main bootloader binary that runs after BL31 hands off control.</p></td>
  </tr>
  <tr>
    <td><p><strong>BL31</strong></p></td>
    <td><p>ARM Trusted Firmware-A — the EL3 secure monitor. Mandatory on ARMv8.</p></td>
  </tr>
  <tr>
    <td><p><strong>BL32</strong></p></td>
    <td><p>Optional TEE OS (OP-TEE). Tracked for RK3576 in :Link[flipperone-linux-build-scripts#57]{href="https://github.com/flipperdevices/flipperone-linux-build-scripts/issues/57" newTab="true" hasDisabledNofollow="false"}.</p></td>
  </tr>
</table>

The FIT *configuration* node decides which images are loaded and in what order. In a normal boot **BL31 runs first**; it then drops to EL2 and starts U-Boot proper.

***

## Stage 4 — U-Boot proper

U-Boot is feature-rich enough to load almost anything from almost anywhere, so the flow becomes board- and image-specific from this point on.

<table isTableHeaderOn="true" columnWidths="220,440">
  <tr>
    <td><p><strong>U-Boot flavour</strong></p></td>
    <td><p><strong>Boot behaviour</strong></p></td>
  </tr>
  <tr>
    <td><p>Rockchip vendor U-Boot (~2017 base)</p></td>
    <td><p>Boots via hard-coded commands defined at build time. Used in Rockchip's BSP / SDK images.</p></td>
  </tr>
  <tr>
    <td><p>Mainline U-Boot (Flipper One)</p></td>
    <td><p>Uses <strong>Standard Boot</strong>: enumerates available storage, scans each for bootable partitions, and tries multiple boot methods per partition (<code>extlinux.conf</code>, plain EFI binaries, PXElinux scripts, …).</p></td>
  </tr>
</table>

Current Flipper One test images boot through **`extlinux.conf`**, but this may change.

***

## Flash structure

Only two on-flash offsets are fixed by the boot chain — everything else is determined by the partition table and the SPL build configuration.

<table isTableHeaderOn="true" columnWidths="220,140,300">
  <tr>
    <td><p><strong>Region</strong></p></td>
    <td><p><strong>Byte offset</strong></p></td>
    <td><p><strong>Notes</strong></p></td>
  </tr>
  <tr>
    <td><p>RKNS image (TPL + SPL)</p></td>
    <td><p><code>0x8000</code></p></td>
    <td><p>Sector <strong>64</strong> on 512-byte-sector media (SD, eMMC); sector <strong>8</strong> on 4096-byte-sector media (UFS). Searched by Boot ROM.</p></td>
  </tr>
  <tr>
    <td><p>FIT image (U-Boot proper + BL31 [+ BL32] + DTB)</p></td>
    <td><p><code>0x800000</code> (default)</p></td>
    <td><p>Loaded by SPL. The actual offset is set in the SPL build config and can be moved.</p></td>
  </tr>
  <tr>
    <td><p>Partition table (GPT or Rockchip parameter)</p></td>
    <td><p>varies</p></td>
    <td><p>Read by U-Boot proper; not consulted by Boot ROM or SPL.</p></td>
  </tr>
  <tr>
    <td><p>Bootable partition(s) — kernel, rootfs, <code>extlinux.conf</code>, EFI binaries, …</p></td>
    <td><p>per partition table</p></td>
    <td><p>Discovered by U-Boot Standard Boot.</p></td>
  </tr>
</table>

:::hint{type="info"}
**Modern packaging.** Upstream U-Boot now produces a single combined image, `u-boot-rockchip.bin`, in which the RKNS part and the FIT part are already placed at the correct offsets with the required padding between them. Writing this one file to the start of the boot device takes care of both pieces, so the on-disk layout of the individual sub-images rarely needs to be touched by hand.
:::

:::hint{type="danger"}
The combined image is normally written with `dd`, e.g. `dd if=u-boot-rockchip.bin of=/dev/<target> bs=512 seek=64 conv=fsync`. **Verify the target device with `lsblk` before running** — `dd` overwrites the target unconditionally, and pointing it at the wrong disk will destroy data on the host system.
:::

***

## References

- alchark, [comment on flipperone-docs#52](https://github.com/flipperdevices/flipperone-docs/issues/52#issuecomment-4509109037) — primary source for the boot flow and flash offsets documented here.
- Rockchip, *RK3576 Technical Reference Manual* — chapter *Boot configuration* covers `SARADC_VIN0` strapping and the RKNS signature.
- Mainline U-Boot, [`doc/board/rockchip/rockchip.rst`](https://docs.u-boot.org/en/latest/board/rockchip/rockchip.html) — documents `u-boot-rockchip.bin` packaging and Standard Boot.
- ARM Trusted Firmware-A documentation, [TF-A boot flow](https://trustedfirmware-a.readthedocs.io/en/latest/design/firmware-design.html#cold-boot).
