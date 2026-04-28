---
title: Graphics
slug: testing/graphics
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:24:41 GMT+0000 (Coordinated Universal Time)
---

## Graphics Integrity Tests

This section covers graphics and video output testing procedures for Flipper One.

***

# GPU driver performance

- Boot device in `Default` boot target with 4k\@120 monitor connected to HDMI
- Check screen resolution and frame rate automatically configured.&#x20;
  **Expected: 4K\@120hz**
- Run `/rk3576-linux-tests/gpu/gpu_info.sh`&#x20;
  **Expected output:**

:::CodeblockTabs{indent="1"}
Output: gpu\_info.sh

```bash
....
=== Conclusion ===
KMS/display driver : rockchip-drm
GPU kernel module  : none
GL vendor          : Mesa
GL renderer        : Mali-G52 r1 (Panfrost)
Session type       : wayland
=== Display resolution & refresh rate ===
  Display mode     : 3840x2160 @ 119.98*+ Hz
```
:::

- Run `/rk3576-linux-tests/gpu/glxgears_quick.sh`
  **Expected output:**

:::CodeblockTabs{indent="1"}
Output: glxgears\_quick.sh

```bash
GL_RENDERER   = Mali-G52 r1 (Panfrost)
GL_VERSION    = 3.1 Mesa 25.0.7-2
GL_VENDOR     = Mesa
GL_EXTENSIONS = GL_....

7176 frames in 5.0 seconds = 1435.139 FPS
```
:::

***

# HDMI — Default target

In `Default` boot target HDMI is routed to main video out `(vo0)` and USB-DisplayPort routed to second video out `(vo2)` . So HDMI should support 4K\@120 output and USB-C DisplayPort only 1080p.

- Boot device in `Default` boot target with 4k\@120 monitor connected to HDMI&#x20;
- Check what screen resolution and frame rate are automatically configured&#x20;
  **Expected: 4K\@120hz**
- Run `GPU driver performance` tests
- Hotplug test: unplug HDMI cable from working device displaying image and reconnect HDMI cable
  **Expected: video output restored on monitor&#x20;**&#xA;**⚠️ Currently failed&#x20;**
- ❌ TODO: Run `HDMI CEC` tests
- ❌ TODO Run `HDMI Audio` tests

***

# HDMI — 4K-USB-DisplayPort target

In `4K-USB-DisplayPort` boot target HDMI is routed to second `(vo2)` and USB-C DisplayPort routed to main video out `(vo0)` . So HDMI should only support 1080p and USB-C DisplayPort should support 4K\@120

- Boot device in `4K-USB-DisplayPort` boot target with 4k\@120 monitor connected to HDMI&#x20;
- Check what screen resolution and frame rate are automatically configured&#x20;
  **Expected: FullHD\@60hz**
- Run `GPU driver performance` tests
- ❌ TODO: Run `HDMI CEC` tests
- ❌ TODO Run `HDMI Audio` tests

***

# USB-DisplayPort — Default target

In `Default` boot target HDMI is routed to main video out `(vo0)` and USB-C DisplayPort routed to second video out `(vo2)` . So HDMI should support 4K\@120 output and USB-C DisplayPort only 1080p.

- Boot device in `4K-USB-DisplayPort` boot target with 4k\@120 monitor connected to USB-C DisplayPort over USB Type-C cable&#x20;
- Check screen resolution and frame rate automatically configured.&#x20;
  **Expected: 1080\@60hz???**
  **⚠️ Currently failed&#x20;**
- Run `GPU driver performance` tests
- ❌ TODO: Test USB device (mouse+keyboard) connected to monitor USB hub

***

# USB-C Display Port —  4K-USB-DisplayPort target

In `4K-USB-DisplayPort` boot target HDMI is routed to second video out `(vo2)` and USB-C DisplayPort routed to second video out `(vo0)` . So HDMI should support 4K\@120 output and USB-C DisplayPort only 1080p.

- Boot device in `4K-USB-DisplayPort` boot target with 4k\@120 monitor connected to USB-C DisplayPort over USB Type-C cable&#x20;
- Check screen resolution and frame rate automatically configured.&#x20;
  **Expected: 1080\@60hz???**
  **⚠️ Currently failed&#x20;**
- Run `GPU driver performance` tests
- ❌ TODO: Test USB device (mouse+keyboard) connected to monitor USB hub

***

# NO Graphics target

In `NO Graphics` boot target HDMI and USB-DisplayPort are null-routed and not connected to any video core. So no video output should work

- Boot device in `NO Graphics` boot target with monitor connected to USB-C and HDMI ports
  **Expected: No video ouput**
