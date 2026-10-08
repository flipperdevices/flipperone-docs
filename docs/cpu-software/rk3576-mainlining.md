---
title: Rockchip RK3576 mainline support
slug: cpu-software/rk3576-mainlining
docTags: 
---

![RK3576 location on the Flipper One mainboard](/files/pics/flipper_one_rk3576_in_body_outline.png "RK3576 on the Flipper One mainboard")

We use the Rockchip RK3576 system-on-chip for our main application processor, which includes CPU cores (4x ARM Cortex-A72 and 4x ARM Cortex-A53), GPU (ARM Mali-G52 MC3), 6 TOPS NPU, as well as a wide assortment of built-in peripheral interfaces and controllers (storage, network, various I/O, etc.). It also includes a dedicated on-chip low-power MCU (Cortex-M0), which can be configured to control selected peripherals when the main OS is not running (but there are no documented users of it yet, and we don't use it either). Read the full [RK3576 Datasheet](https://cdn.flipper.net/RK3576-Brief-Datasheet-V1.2-20240311.pdf) and [Tech specs](https://docs.flipper.net/one/general/tech-specs#main-cpu-rk3576).

## Why we chose RK3576:
* Performance: comparable to Raspberry Pi 5
* Energy efficiency: \<1W idle, around 4W under heavy load, stated TDP of 10W
* Up-to-date architecture and peripheral standards: UFS storage, Vulkan support, built-in neural engine, modern HDMI/DP display compatibility, etc.
* Existing support in upstream Linux, U-boot, and TF-A at least at some usable level

The support in upstream Linux, U-boot, and TF-A is especially important for us, as we strive to make Flipper One a mainline-first device not tied to vendor BSP software.

## What's that BSP thing about?

BSP, short for Board Support Package, is the traditional way hardware vendors provide software support for their devices in the embedded world. It's usually a tightly coupled set of vendor-specific packages of arbitrarily selected versions (usually outdated by years at the time of release), heavily modified by the vendor in incompatible ways, rarely (if ever) updated, and buildable only in an environment and with the tools the vendor used at the time of shipping.

In short, it's what a silicon vendor would give you to check all the boxes in terms of advertised hardware features, but which condemns you to using old, hastily assembled software of unknown quality, with limited realistic options to support new distros, use new peripheral hardware, etc.

Rockchip also supports their chips by the means of a BSP, which is a multi-gigabyte software download based around Linux 6.1 (over 4 years old at the time of this writing), targeting Debian 12 ("old stable" at the time of this writing), with a number of binary-only parts (specifically, the DDR memory trainer, BL31 and BL32 bootloader stages) and Rockchip-specific incompatible interfaces (for video encoding/decoding, for NPU, etc.).

Rockchip's software stack broadly comprises the following components:

* **Boot ROM** — pre-burned into the SoC itself, non-updatable, runs unconditionally as soon as power is applied to the SoC.

* **Boost binary** — patches up some pointers in SRAM - apparently an in-field bug fix for the boot ROM - and initializes UFS power mode parameters.

* **DDR trainer** — configures the memory controller, sets RAM frequency and timings.

* **U-boot SPL** (heavily modified by Rockchip based on an old version from 2017) — runs early hardware initialization and loads the main system bootloader (U-boot) via BL31+BL32.

* **BL31 (binary only)** — heavily modified version of the ARM Trusted Firmware. Controls CPU+GPU+NPU clocks, low-level power states, etc., keeps running in the highest ARM exception level when the system is booted, and provides callable services for the OS via the SCMI interface.

* **BL32 (binary only)** — heavily modified version of the OP-TEE. Controls "secure world" features, including crypto, device authentication (hardware unique keys, one-time programmable hashes, and cryptographic signatures, etc.) for DRM and verified boot functionality, among other things. Also keeps running when the system is booted and exposes "secure" SCMI calls to the OS and to BL31 services.

* **U-boot** (heavily modified by Rockchip based on an old version from 2017) — finds a Linux kernel on the "main" boot device, loads it along with a DTB and initrd, and boots it.

* **Linux kernel** (heavily modified by Rockchip based on an old 6.1 version from 2022)

* **Debian 12 userspace** (or Android 14)

* Rockchip-specific userspace libraries and drivers (which need Rockchip-patched end user software to be useful)

To complicate matters further, the full BSP is only provided to hardware integrators via closed Rockchip's Gerrit repo, and not to end users. Parts of it contain code that puts limits on distribution.

## Mainline (a.k.a. upstream) software

The key alternative to BSP software (often called downstream) is the mainline Linux ecosystem. Mainline here refers to the fresh Linux kernel versions as released by Linus Torvalds on [kernel.org](https://kernel.org), U-boot versions as released by the U-boot project, etc. Each of the respective "original" projects is referred to as upstream.

Upstream projects have rigorous peer review standards, with poorly written code regularly becoming the subject of colorful remarks by seasoned maintainers who serve as the ultimate gatekeepers. They emphasize maintainability, compatibility across different platforms, stable user interfaces, and thorough testing. This often means that getting new hardware supported upstream takes much more initial effort than cobbling together some piece of patched downstream software.

What mainline support brings as the upside though is substantial:
* Any distribution that ships a recent enough kernel version should work out of the box on Flipper One
* Any new hardware peripherals that have upstream drivers should work out of the box
* Bugs are fixed regularly
* New software features are made available regularly

Mainline ecosystem aligns much better with what we want Flipper One to be: an open device that can be used in an unlimited number of ways with all sorts of hardware attachments and software configurations. In fact, it is virtually impossible to achieve using vendor BSPs. Furthermore, we strongly believe that open collaboration the way upstream projects work is great!

## Current mainlining status

* Mainline Linux mostly works on RK3576, except NPU, video encoding, CSI camera, PCIe suspend, and some niche peripherals
* Mainline U-boot fully works with a couple of in-progress patches
* TF-A (BL31): basic functions work well (clock scaling, suspend/resume)
* OP-TEE (BL32): no support for RK3576

Collabora has been working on mainline support for RK3588 and RK3576 for a long time, and maintains a more detailed status tracker for the support of individual hardware blocks: https://gitlab.collabora.com/hardware-enablement/rockchip-3588/notes-for-rockchip-3576/-/blob/main/mainline-status.md

# How to contribute

Our main goal is to build a truly open hardware platform with full mainline support. We invite anyone in the community who cares about this to get involved.

You can contribute at any level, from submitting code to advocacy with vendors.

1. Read about our [CPU Software sub-project](https://docs.flipper.net/one/cpu-software/about) and how development is organized on our side.

2. Take a look at the current [Open Tasks](https://docs.flipper.net/one/open-tasks) — you may be able to help with specific issues in Flipper One development.

3. Explore [Collabora's kernel repository](https://gitlab.collabora.com/hardware-enablement/rockchip-3588/linux), where mainlining work for the RK3588 and RK3576 is ongoing.

4. Send your kernel and U-Boot changes upstream, as described in [Sending kernel and U-Boot patches](#sending-kernel-and-u-boot-patches) below.

## Sending kernel and U-Boot patches

For the Linux kernel and U-Boot, we prefer that you send patches directly to the upstream mailing lists instead of opening a pull request in our forks. Our goal is for Flipper One to work on unpatched kernels from kernel.org, so we don't carry changes that can't go upstream. Once your patch is on the list, we may also apply it to our [kernel](https://github.com/flipperdevices/flipper-linux-kernel) and [U-Boot](https://github.com/flipperdevices/u-boot) trees.

### Before you send

- **Test on real hardware.** Run your change on Flipper One or a [supported RK3576 board](Supported-boards.md). Untested patches are not accepted.
- **Have a real reason for the change.** A good way to find one is to use an RK3576 board for your own workloads and fix what doesn't work well. A real use case also helps you convince upstream maintainers.
- **Want to discuss it first?** Open an issue in our [kernel](https://github.com/flipperdevices/flipper-linux-kernel/issues) or [U-Boot](https://github.com/flipperdevices/u-boot/issues) repository.

### Follow the upstream rules

Each project has its own rules, and maintainers expect you to follow them:

- Linux: [Submitting patches](https://docs.kernel.org/process/submitting-patches.html). For device tree changes, also read [Submitting devicetree binding patches](https://docs.kernel.org/devicetree/bindings/submitting-patches.html).
- U-Boot: [Development process](https://docs.u-boot.org/en/latest/develop/process.html) and [Sending patches](https://docs.u-boot.org/en/latest/develop/sending_patches.html).

A few rules that are easy to miss:

- Sign off every commit with `git commit -s`. Both projects require a known identity in the `Signed-off-by` line, so anonymous contributions are not accepted.
- Split large changes into a series of small commits, and add a cover letter that explains the whole series.

### Send the patches

1. Use [b4](https://b4.docs.kernel.org/en/latest/contributor/overview.html) or `git send-email` ([setup guide](https://git-send-email.io/)). Both send your commits as plain-text emails in the format maintainers expect. With b4, `b4 prep --auto-to-cc` also fills in the recipients for you.
2. Without b4, find the recipients with `scripts/get_maintainer.pl`, which both the kernel and U-Boot trees include. U-Boot patches always go to u-boot@lists.u-boot-project.org.
3. If your patch is relevant to Flipper One or one of our supported boards, add Alexey Charkov (alchark@flipper.net) to Cc.

### After sending

- Answer review comments on the mailing list, then send a new version (v2, v3, and so on) that lists what changed.
- Maintainers rarely look at new patches during the merge window, the two weeks after each Linux release. If there is no reply after it closes, a short and polite reminder is fine.
- If you also opened an issue or pull request in our repositories, post a link to your patch there.
