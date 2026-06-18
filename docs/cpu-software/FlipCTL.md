---
title: FlipCTL
slug: cpu-software/flipctl
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:18:11 GMT+0000 (Coordinated Universal Time)
---

## Flipper's Universal Control Interface

::Image[]{src="/files/pics/flipctl_scheme.png" alt="FlipCTL logic scheme"}

FlipCTL is a **lightweight GUI framework for embedded and headless Linux systems**, designed as a modern replacement for traditional HMI (Human-Machine Interface) solutions. Originally built for Flipper One, it runs on any Linux system, from servers and routers to single-board computers, with no desktop environment required.

The core idea: instead of running a desktop GUI (GNOME, KDE) on a tiny screen, FlipCTL provides a **pixel-rendered, navigation-friendly interface** — similar in spirit to `nmtui` or Midnight Commander, but graphically richer and hardware-aware.

***

## The problem FlipCTL solves

```text
:::Iframe{code="<video&#xA;    autoplay muted loop playsinline style=&#x22;width: 100%; margin: 0 !important;&#x22;&#xA;    src=&#x22;https://cdn.flipper.net/desktopUI_VS_FlipCTL.mp4&#x22;&#xA;></video>&#xA;<div class=&#x22;text-center mt-2.5 text-gray-400 pb-5&#x22;>&#xA;Caption&#xA;</div>" iframeHeight="500"}

:::
```

Existing GUI solutions for embedded computers, also known as HMI (Human-Machine Interface), have several pain points:

- **Need a graphical desktop (Xorg or Wayland) to run** — don't work on headless servers, routers, or embedded devices.

- **Desktop UIs are hard to use** with a d-pad or joystick.

- **CLI tools have no unified wrapper** — you need a keyboard and a terminal to run interactive commands like `ping` or `nmap`.

- **Existing control panels are complex** to install and configure.

***

## The FlipCTL concept vision

On any Linux system, with or without a display, FlipCTL should be immediately useful. Plug in the FlipCTL Control Panel via USB, install and run the service, and you instantly have a working interface — no Xorg, no desktop, no configuration.

FlipCTL is installed with a single command. For Debian-based systems:

`apt install flipctl` — and everything works.

Once installed, FlipCTL provides a default dashboard with system data and actions:

- CPU load & uptime
- Disk usage
- Network configuration
- System reboot / shutdown

‎ 

### Supported frontends

FlipCTL can work with different frontends for input and output:

<table isTableHeaderOn="true" columnWidths="250,410">
  <tr align="center">
    <td align="center">
      <p><strong> Frontend</strong></p>
    </td>
    <td align="center">
      <p><strong>Description</strong></p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="/files/pics/flipctl-on-flipper-one.png"/>
      <p><strong>Flipper One</strong></p>
    </td>
    <td>
      <p>The primary target device is an ARM Linux computer with a built-in 256×144 px LCD and physical controls. Includes boot menu functionality as part of the FlipCTL package</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="/files/pics/flipctl-control-panel.png"/>
      <p><strong>FlipCTL Control Panel</strong></p>
    </td>
    <td>
      <p>A compact standalone module with a screen and buttons, connecting via USB or SPI — designed to add a physical HMI to any embedded system, server, single-board computer, or router</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="/files/pics/flipctl-in-terminal.png"/>
      <p><strong>TUI (Text UI)</strong></p>
    </td>
    <td>
      <p>A pseudo-graphical interface rendered in any Linux terminal — usable locally or over SSH, similar to <code>nmtui</code> or Midnight Commander.</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="/files/pics/flipctl-in-browser.png"/>
      <p><strong>Web UI</strong></p>
    </td>
    <td>
      <p>A browser-based interface — renders the same layout and navigation accessible from any device on the network.</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="/files/pics/flipctl-in-app.png"/>
      <p><strong>Desktop App</strong></p>
    </td>
    <td>
      <p>A native desktop application for Linux, useful for development, testing, or general use on a workstation.</p>
    </td>
  </tr>
</table>

***

## Physical interface

![Flipper One controls](/files/pics/controls-explainer.png)

### Screen

- **Diagonal:** 2.39 inch
- **Resolution:** 256 × 144 px
- **Depth:** 6-bit grayscale (64 shades)

‎ 

### Soft keys

Flipper One has five app-defined buttons.

<table isTableHeaderOn="true" columnWidths="100,560">
  <tr align="center">
    <td>
      <p>Button</p>
    </td>
    <td>
      <p>Default Role</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Escape</strong></p>
    </td>
    <td>
      <p>Exit app / cancel / go back</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>View</strong></p>
    </td>
    <td>
      <p>Help, tooltips, toggle view mode</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Power</strong></p>
    </td>
    <td>
      <p>Opens Power menu overlay (sleep, backlight, reboot); hold = hardware shutdown regardless of system state</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Edit</strong></p>
    </td>
    <td>
      <p>Edit fields, switch view types</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Run</strong></p>
    </td>
    <td>
      <p>Confirm / OK / next step / start</p>
    </td>
  </tr>
</table>

The Power button is intercepted at the MCU level — it works even if the OS is frozen, similar to a hardware power button on a standard PC.

‎

### D-Pad + back button

The D-Pad is used for standard directional navigation: up / down / left / right / center (OK).
Back button returns to the previous screen; functionally mirrors Escape in most contexts.

‎ 

### App switcher button 

The app switcher button shows all running applications and allows switching between them — similar to a double-tap home button on older phones.

‎

### Touchpad (optional)
Only exist on Flipper One, completely optional and can be used to speed up scrolling and navigation. It duplicates the functions of the D-pad:
* Scrolling through lists
* Navigating the on-screen keyboard
* Quick directional input (left / right / up / down).

‎ 

### PTT button (optional)

A PTT (Push-to-Talk) button is a programmable button originally designed for walkie-talkie use (press and hold to transmit audio). On Flipper One it may serve secondary UI functions like screen lock.

***

## FlipCTL Control Panel

![](/files/pics/flipctl-control-panel-raspberry-pi.jpg)
![](/files/pics/flipctl-control-panel-in-rack.jpg)

FlipCTL Control Panel - a compact device featuring the same display as the Flipper One and the same set of controls, except for the touchpad and the PTT (Push-to-Talk) button. 

FlipCTL Control Panel can be:
* Placed on a desk
* Mounted directly to a single-board computer, such as a Raspberry Pi
* Mounted on a server or server rack

FlipCTL Control Panel connects to any Linux-based system via USB or SPI (or I2C?), providing a physical human–machine interface (HMI) for headless servers, routers, and embedded devices, without requiring a desktop environment. The hardware design for this project hasn't been finalized yet — you can join the open discussion: [FlipCTL Control Panel hardware design](https://github.com/flipperdevices/flipperone-hardware/issues/133)

***

## FlipCTL Architecture

![](/files/pics/FlipCTL-architecture-vertical.png)

FlipCTL core components:

* **Backend** is responsible for managing the operating system itself. It can interact with systemd, control OS services, configure networking through NetworkManager or systemd-networkd, and wrap existing command-line utilities such as nmap, ping, and traceroute. The backend exposes these capabilities through APIs that are consumed by the frontend.

* **Frontend UI** is currently built using HTML and JavaScript. Despite the associated overhead, this approach enables rapid UI development and compact implementation, while avoiding the need for specialized expertise required by many embedded UI frameworks.

* **Renderer** is a web browser. On Flipper One, we currently use a headless WebKit instance running directly on top of DRM (Direct Rendering Manager), without Xorg or Wayland. We also want to support multiple renderer options — for example, a TUI (Text User Interface) for use directly from the console.

<table isTableHeaderOn="true" columnWidths="200,460">
  <tr align="center">
    <td>
      <p>Frontend</p>
    </td>
    <td>
      <p>Description</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Flipper One</strong></p>
    </td>
    <td>
      <p>The primary target device is an ARM Linux computer with a built-in 256×144 px LCD and physical controls. <strong>Includes boot menu functionality</strong> as part of the FlipCTL package</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>FlipCTL Control Panel</strong></p>
    </td>
    <td>
      <p>A compact standalone module with a screen and buttons, connecting via USB, SPI, or UART — designed to add a physical HMI to any embedded system, server, single-board computer, or router</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>TUI (Terminal UI)</strong></p>
    </td>
    <td>
      <p>A pseudo-graphical interface rendered in any Linux terminal — usable locally or over SSH, similar to <code>nmtui</code> or Midnight Commander. <strong>May be built using React + Ink</strong> for component-based terminal rendering</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Web UI</strong></p>
    </td>
    <td>
      <p>A browser-based interface served by the FlipCTL daemon — renders the same layout and navigation accessible from any device on the network. <strong>Can share the same React codebase as the Desktop App</strong></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Desktop App</strong></p>
    </td>
    <td>
      <p>A native desktop application for Linux, useful for development, testing, or general use on a full workstation. <strong>Can share the same React codebase as the Web UI</strong></p>
    </td>
  </tr>
</table>

‎

### Rendering approach

The 256×144 px screen requires **pixel-level rendering**, which standard TUI libraries (ncurses, etc.) cannot provide. The proposed solution is an **HTML/CSS rendering engine** running as a background daemon — a lightweight browser-based renderer that draws menus, popups, and UI components.

The key principle: **data and UI logic are separated from the renderer**. The same data can be displayed differently depending on the frontend:

- Pixel-rendered on the LCD
- Character-rendered in a terminal (React + Ink)
- HTML in a browser (React)

‎ 

### Backend + plugin system

FlipCTL runs as a **system daemon** with a plugin architecture:

- The **core daemon** handles input, routing, rendering communication, and the plugin API
- **Plugins** are wrappers around CLI tools or services, written in any language

Developers can write wrappers in whatever language they prefer:

- **Python** — e.g., a wrapper for `nmap` or `nginx` stats
- **Bash** — quick scripts for simple tools
- **Rust, Node.js, Go** — for performance-critical or complex plugins

Example: a `ping` plugin presents a menu to enter a host/IP, runs the underlying `ping` command, and displays live output — all navigable with the d-pad.

**Example plugins:** `ping` · `nmap` · `traceroute` · `nginx status` · `iptables` · `disk manager`

***

## How to contribute

This page outlines the FlipCTL vision and its architecture at a high level. We believe there are many good ways to bring this architecture to life, and we invite the community to share ideas and propose implementation approaches. Our goal is to collaboratively discover the best solutions for FlipCTL.

We have created a dedicated [FlipCTL repository](http://github.com/flipperdevices/flipctl) where contributors can submit pull requests, discuss design proposals, and collaborate on implementation ideas.

A Pull Request should include:

- A description of your proposed FlipCTL architecture implementation, including the components you would use and how they would interact with each other.

- A description of your vision for the plugin system and the wrappers for standard command-line utilities like `ping` or `nmap`.

- A minimal working FlipCTL prototype capable of driving multiple frontends. One frontend should be a Web UI, while another should be a TUI.
