# Rockchip RK3576 mainline support

We use the Rockchip RK3756 system on chip for our main application processor, which includes CPU cores (4x ARM Cortex-A72 and 4x ARM Cortex-A53), GPU (ARM Mali-G52 MC3), 6 TOPS NPU as well as a wide assortment of built-in peripheral interfaces and controllers (storage, network, various I/O, etc.). It also includes a dedicated on-chip low-power MCU (Cortex-M0) which can be configured to control selected peripherals when the main OS is not running (but there are no documented users of it yet, and we don't use it either)

The reason we chose it was:
* Performance: beats Raspberry Pi 5 in multi-core benchmarks
* Energy efficiency: <1W idle, around 4W under heavy load, stated TDP of 10W
* Up-to-date architecture and peripheral standards:. UFS storage, Vulkan support, built-in neural engine, modern HDMI/DP display compatibility etc.
* Existing support in upstream Linux, U-boot and TF-A at least at some usable level

The last point above is especially important for us, as we strive to make Flipper One a mainline-first device not tied to vendor BSP software.

## What's that BSP thing about?

BSP, short for Board Support Package, is the traditional way hardware vendors provide software support for their devices in the embedded world. It's usually a tightly coupled set of vendor-specific packages of arbitrarily selected versions (usually outdated by years at the time of release), heavily modified by the vendor in incompatible ways, rarely (if ever) updated, buildable only in an environment and with the tools the vendor used at the time of shipping.

In short, it's what a silicon vendor would give you to check all the boxes in terms of advertised hardware features, but which condemns you to using old hastily assembled software of unknown quality, with limited realistic options to support new distros, use new peripheral hardware, etc.

Rockchip also supports their chips by the means of a BSP, which is a multi-gigabyte software download based around Linux 6.1 (over 4 years old at the time of this writing), targeting Debian 12 ("old stable" at the time of this writing), with a number of binary-only parts (specifically, the DDR memory trainer, BL31 and BL32 bootloader stages) and Rockchip-specific incompatible interfaces (for video encoding/decoding, for NPU, etc.).

Rockchip's software stack broadly comprises the following components:
* Boot ROM: pre-burned into the SoC itself, non-updatable, runs unconditionally as soon as power is applied to the SoC
* Boost binary: patches up some pointers in SRAM - apparently an in-field bug fix for the boot ROM - and initializes UFS power mode parameters
* DDR trainer: configures the memory controller, sets RAM frequency and timings
* U-boot SPL (heavily modified by Rockchip based on an old version from 2017): runs early hardware initialization and loads the main system bootloader (U-boot) via BL31+BL32
* BL31 (binary only): heavily modified version of the ARM Trusted Firmware. Controls CPU+GPU+NPU clocks, low-level power states etc., keeps running in the highest ARM exception level when the system is booted and provides callable services for the OS via the SCMI interface
* BL32 (binary only): heavily modified version of the OP-TEE. Controls "secure world" features including crypto, device authentication (hardware unique keys, one-time programmable hashes and cryptographic signatures, etc.) for DRM and verified boot functionality, among other things. Also keeps running when the system is booted and exposes "secure" SCMI calls to the OS and to BL31 services
* U-boot (heavily modified by Rockchip based on an old version from 2017): finds a Linux kernel on the "main" boot device, loads it along with a DTB and initrd, and boots it
* Linux kernel (heavily modified by Rockchip based on an old 6.1 version from 2022)
* Debian 12 userspace (or Android 14)
* Rockchip-specific userspace libraries and drivers (which need Rockchip-patched end user software to be useful)

To complicate matters further, the full BSP is only provided to hardware integrators via Rockchip's Gerrit, and not to end users. Parts of it contain code which puts limits on distribution.

## Mainline (a.k.a. upstream) software

The key alternative to BSP software (often called downstream) is the mainline Linux ecosystem. Mainline here refers to the fresh Linux kernel versions as released by Linux Torvalds, U-boot versions as released by the U-boot project, etc. Each of the respective "original" projects is referred to as upstream.

Upstream projects have rigorous peer review standards, with poorly written code regularly becoming subject of colorful remarks by seasoned maintainers who serve as the ultimate gatekeepers. They emphasize maintainability, compatibility across different platforms, stable user interfaces and thorough testing. This often means that getting new hardware supported upstream takes much more initial effort than cobbling together some piece of patched downstream software.

What mainline support brings as the upside though is substantial:
* Any distribution which ships a recent enough kernel version should work out of the box
* Any new hardware peripherals which have upstream drivers should work out of the box
* Bugs are fixed regularly
* New software features are made available regularly

Mainline ecosystem aligns much better with what we want Flipper One to be: an open device which can be used in limitless number of ways with all sorts of hardware attachments and software configurations. In fact, it is virtually impossible to achieve using vendor BSPs. Furthermore, we strongly believe that open collaboration the way upstream projects work is great!

## Current mainlining status

* Mainline Linux mostly works on RK3576, except NPU, video encoding, CSI camera, PCIe suspend, some niche peripherals
* Mainline U-boot fully works with a couple of in-progress patches
* TF-A (BL31): basic functions work well (clock scaling, suspend/resume)
* OP-TEE (BL32): no support for RK3576

Collabora has been working on mainline support for RK3588 and RK3576 for a long time, and maintains a more detailed status tracker for the support of individual hardware blocks: https://gitlab.collabora.com/hardware-enablement/rockchip-3588/notes-for-rockchip-3576/-/blob/main/mainline-status.md?ref_type=heads

Open tasks - TBD
