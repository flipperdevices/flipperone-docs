---
title: About Hardware
slug: hardware/about
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:32:40 GMT+0000 (Coordinated Universal Time)
---

This section covers the hardware development of Flipper One. It includes the electronics (PCB, schematics) and mechanical (case, assembly, buttons) design.&#x20;

# Tech specs

TODO: Finalize naming, description, and tech specs of controls, ports, and interfaces.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/L9hw7RZXHbTHmSLBySl3x_flipperone-controls-and-indicators-v003.png)

### Controls description

<table isTableHeaderOn="true" columnWidths="331,332">
  <tr>
    <td align="center">
      <p><strong>Control</strong></p>
    </td>
    <td align="left">
      <p><strong>Description</strong></p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><strong>PTT Button</strong></p>
      <p><img src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/xsFRd7Ahws8dSdVisqNsB-20260122-124532.svg" alt=""></p>
    </td>
    <td align="left">
      <p>Push-to-talk button to activate microphone in walkie-talkie mode, for voice control and more.</p>
      <p>This button may be used as an adaptive App-Defined Button. In this case, the current action is context-dependent and displayed on the screen.</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><strong>Touchpad</strong></p>
      <p><img src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/JP__awtzIDsLFT4Nb-nco-20260122-124532.svg" alt=""></p>
    </td>
    <td align="left">
      <p>Touchpad for on-screen keyboard and menu navigation, content scrolling. Support horizontal and vertical scroll.</p>
      <p>Most likely will be always duplicate D-pad navigation and will be used for quick move in long lists.</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><strong>ESC button</strong></p>
      <p><img src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/6Xjs07cOI-ba4BxRR7EO0-20260122-124532.svg" alt=""></p>
    </td>
    <td align="left">
      <p>Adaptive App-Defined Button. Current action is context dependent and displayed on screen above the button.</p>
      <p><strong>Recommended UI actions:</strong> cancel, stop, pause, breake, abort, back, discard.</p>
      <p>TODO: finalize name?</p>
    </td>
  </tr>
  <tr>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>View button</strong></p>
      <p><img src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/rDgkRg_dF9IFOgihFVzjh-20260122-124532.svg" alt=""></p>
    </td>
    <td align="left" colSpan="1" rowSpan="1">
      <p>Adaptive App-Defined Button. Current action is context dependent and displayed on screen above the button.</p>
      <p><strong>Recommended UI actions:</strong> help, search, view.</p>
      <p>TODO: finalize icon and name</p>
    </td>
  </tr>
  <tr>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>Power button</strong></p>
      <p><img src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/Wajayyyz7n7hH5qMcgFR3-20260122-124532.svg" alt=""></p>
    </td>
    <td align="left" colSpan="1" rowSpan="1">
      <p><code>Long press for 1 second:</code> Device power mode control: turn ON/OFF, reboot.</p>
      <p><code>Short press on Linux level:</code> Action is context dependent and displayed on screen above the button.</p>
    </td>
  </tr>
  <tr>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>Edit button</strong></p>
      <p><img src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/Z8AnX2Jf40l1Zop7HwdWE-20260122-124532.svg" alt=""></p>
    </td>
    <td align="left" colSpan="1" rowSpan="1">
      <p>Adaptive App-Defined Button. Current action is context dependent and displayed on screen above the button.</p>
      <p><strong>Recommended UI actions:</strong> more, edit, extra, config, rename.</p>
    </td>
  </tr>
  <tr>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>Run button</strong></p>
      <p><img src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/7V284sTkyMo-Kh8iEm5FU-20260122-124532.svg" alt=""></p>
    </td>
    <td align="left" colSpan="1" rowSpan="1">
      <p>Adaptive App-Defined Button. Current action is context dependent and displayed on screen above the button.</p>
      <p><strong>Recommended UI actions:</strong> start, run, enter, save.</p>
    </td>
  </tr>
  <tr>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>App Switcher</strong></p>
      <p><img src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/QSbhOJEmg3J-QEZEoJ9Hf-20260122-124532.svg" alt=""></p>
    </td>
    <td align="left" colSpan="1" rowSpan="1">
      <p><strong>Works only on Linux level:</strong></p>
      <p>ALT+TAB like button, list all opened apps windows.</p>
    </td>
  </tr>
  <tr>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>Back button</strong></p>
      <p><img src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/isUzdRsHTCEmLK39viMeA-20260122-124532.svg" alt=""></p>
    </td>
    <td align="left" colSpan="1" rowSpan="1">
      <p>Back, exit in menus and apps.</p>
    </td>
  </tr>
  <tr>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>D-pad</strong></p>
      <p><img src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/8ws4ll4i12rS5doBU3TeK-20260122-124532.svg" alt=""></p>
    </td>
    <td align="left" colSpan="1" rowSpan="1">
      <p>Main navigation D-pad with 5-buttons: UP, DOWN, LEFT, RIGHT and OK in center.</p>
    </td>
  </tr>
</table>

### Buttons shortcuts&#x20;

Some buttons and their combinations have hardware-defined behavior that does not depend on software. These combinations can hardware-reset, power off, or put the device into full recovery mode.

<table isTableHeaderOn="true" columnWidths="331,332">
  <tr>
    <td align="center">
      <p><strong>Action</strong></p>
    </td>
    <td align="left">
      <p><strong>Description</strong></p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><strong>Hardware Restart</strong></p>
    </td>
    <td align="left">
      <p><code>Back + Left</code> — hold for 0.5 seconds, ⚠️ but we want 3 seconds? An analog circuit (OR gate) charges a capacitor and sends a reset to all chips: MCU, CPU, and two expanders.</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><strong>Power ON</strong></p>
    </td>
    <td align="left">
      <p>Hold <code>Power</code> button for 1 sec to turn ON device from Power OFF.</p>
      <p>First turn ON from transport mode is the same Power ON. Connecting USB to charging port also Power ON the device.</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><strong>Full Power Cycle (Hardware Reboot)</strong></p>
    </td>
    <td align="left">
      <p>Hold <code>Power</code> button for 10 seconds to complety power cycle device. It will quicly turn off and on battery.</p>
      <p>What will happen when USB charger connected?</p>
    </td>
  </tr>
  <tr>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>Firmware Recovery</strong></p>
    </td>
    <td align="left" colSpan="1" rowSpan="1">
      <p>Hold <code>??? + ???</code> before Powering ON or power cycle to enter in MCU Firmware Recovery.</p>
      <p>TODO: Find better shortcut</p>
    </td>
  </tr>
</table>

### Electronics Schematics

Electrical schematics of all Flipper One boards. TODO: INTERNAL LINK TO Schematics.md

### Mechanics

Mechanical design of the external surfaces of the front panel and rear cover with Flipper One modules.

### Modules

Modules for Flipper One, divided into two categories: GPIO and M.2 modules.

### GPIO modules

GPIO modules connect via the external GPIO port on the rear panel without the need to open the cover. These are DIY modules for enthusiasts that can be built on a prototyping board using off-the-shelf components.

### M.2 modules

M.2 modules are expansion boards in the M.2 form factor (formerly called NGFF). Such modules are often used in laptops and industrial computers. In this format, you commonly find SSD drives, cellular modems, Wi-Fi adapters, SDR radios, and more.&#x20;
