# General 

## General system tests 

This section covers general system tests like boot target, testing equipment, etc.

# Flipper RnD Debian

For development and testing purposes, we use our own Linux builds based on Debian.  
These builds are made for several RK3576-based single board computers: Radxa 4D, ArmSom Sige5, EVB1, Omni3576.

- Build scripts https://github.com/flipperdevices/rk3576-linux-build
- Ready to use images https://dl-linux-images.flipp.dev/full-img/

## Boot targets

Our Flipper RnD Debian Linux has several boot targets for different testing scenarios:

- `Default` — graphical interface boot target with Wayland and KDE autostart. In this boot target HDMI port is routed to main video out `(vo0)` and USB-C DisplayPort routed to second video out `(vo2)`. So HDMI should support 4K\@120 output and USB-C DisplayPort only 1080p.
 
- `4K-USB-DisplayPort` — Same as Default boot target, but with USB-C DisplayPort routed to main video out `(vo0)` so should support 4K\@120. HDMI is routed to second `(vo2)` and only supports 1080p.

- `NO Graphics` — minimal console-only boot target. All video outputs and graphical services are disabled.
