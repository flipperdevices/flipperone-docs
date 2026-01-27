# About Hardware

This section covers the hardware development of Flipper One. It includes the electronics (PCB, schematics) and mechanical (case, assembly, buttons) design.&#x20;

# Tech specs

TODO: Finalize naming, description and tech specs of controls, ports and interfaces&#x20;

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/L9hw7RZXHbTHmSLBySl3x_flipperone-controls-and-indicators-v003.png)

### Controls description

<table isTableHeaderOn="true" columnWidths="[object Object]">
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
    <td>
    </td>
    <td>
    </td>
    <td>
    </td>
    <td>
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
      <p><strong>Escape button</strong></p>
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
    <td>
    </td>
    <td>
    </td>
    <td>
    </td>
    <td>
    </td>
    <td>
    </td>
    <td>
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

<table isTableHeaderOn="true" columnWidths="[object Object]">
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
      <p>Hold <code>Power</code> button for 1 sec to turn ON device from Power OFF. </p>
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

### Ports description

<table isTableHeaderOn="true" columnWidths="[object Object]">
  <tr>
    <td align="center">
      <p><strong>Port</strong></p>
    </td>
    <td>
      <p><strong>Description</strong></p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><strong>USB-C Main</strong></p>
    </td>
    <td>
      <p>Main USB-C port for charging and device emulation. DisplayPort 4K video out for monitor connection.</p>
      <p><strong>Mode</strong>: Host, device emulation</p>
      <p><strong>Type</strong>: USB 3.1+USB 2.0</p>
      <p><strong>Video out:</strong> Alt DisplayPort 1.4, max 4k@120hz* (see HDMI section)</p>
      <p><strong>Charging:</strong> PD Sink/Source, 5v-24v (in), 5v-22v (out, PPS)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><strong>3.5 Audio</strong></p>
    </td>
    <td>
      <p>Analog stereo audio out + microphone input, button support</p>
      <p>3.5 TRRS (LR+MIC). CTIA pinout (L, R, Ground, Mic)</p>
      <p>compatible male jacks schematic: <a href="https://webhamster.ru/mytetrashare/index/mtb0/17023872216e9v828pyw"><strong>https://webhamster.ru/mytetrashare/index/mtb0/17023872216e9v828pyw</strong></a></p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><strong>USB-A</strong></p>
    </td>
    <td>
      <p><strong>Mode</strong>: Only host</p>
      <p><strong>Type:</strong> USB 3.1+USB 2.0</p>
      <p><strong>Charging:</strong> 5v, managed, overcurrent protection</p>
      <p>*Сonnected via internal USB hub</p>
      <p>TODO: better name</p>
    </td>
    <td>
    </td>
  </tr>
  <tr>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>USB-C</strong></p>
    </td>
    <td colSpan="1" rowSpan="1">
      <p><strong>Mode</strong>: Only host</p>
      <p><strong>Type:</strong> USB 3.1+USB 2.0</p>
      <p><strong>Charging:</strong> PD Source, only 5v, managed, overcurrent protection</p>
      <p>*Сonnected via internal USB hub</p>
    </td>
  </tr>
  <tr>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>HDMI Out</strong></p>
    </td>
    <td colSpan="1" rowSpan="1">
      <p>HDMI 2.1, CEC, ARC support, max 4k@120hz*</p>
      <p>*The RK3576 GPU has three video buffers (4K@120Hz, 2560x1600@60Hz, 1920x1080@60Hz) that can be arbitrarily connected to HDMI or TypeC Alt DP. Thus, if several monitors are connected to the flipper via different interfaces, only one of them can be 4K@120Hz</p>
    </td>
    <td>
    </td>
  </tr>
  <tr>
    <td align="center" colSpan="1" rowSpan="1">
      <p>2x Ethernet</p>
      <p><strong>Eth1</strong></p>
      <p><strong>Eth2</strong></p>
    </td>
    <td colSpan="1" rowSpan="1">
      <p>Each port uses RTL8211F-CG PHY: 1G Full-duplex (1G up, 1G down). Standards: 1000Base-T, 100Base-TX, , 10Base-T. Features: WOL, Auto-Negotiation, Crossover Detection</p>
    </td>
  </tr>
  <tr>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>GPIO</strong></p>
    </td>
    <td colSpan="1" rowSpan="1">
      <p>PBD-2×10S connector — 2 rows of 10 contacts, female, 2.54mm.</p>
      <p>On the connector:</p>
      <p>+3.3v/2A, (managed, overcurrent protection)</p>
      <p>+5v/2A (managed, overcurrent protection)</p>
      <p>USB 2.0 from SoC</p>
      <p>2 GPIO from MCU</p>
      <p>12 GPIO from SoC</p>
      <p>Schematic</p>
    </td>
  </tr>
  <tr>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>Micro SD slot</strong></p>
    </td>
    <td colSpan="1" rowSpan="1">
      <p>Connected directly to RK3576</p>
      <p>UHS-I, speed up to 104 MB/s.</p>
      <p>Schematic</p>
      <p>It has an SWD interface SoC for debugging, but it is only active if SD_DET is high. For debugging, you need to use a board with a special cutout.</p>
      <p>Example</p>
    </td>
  </tr>
  <tr>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>SIM-card slot</strong></p>
    </td>
    <td colSpan="1" rowSpan="1">
      <p>NanoSIM connector.</p>
      <p>Connected to the M.2 slot in line with the specifications of M.2</p>
      <p>*For the SIM card to work, you need a GSM modem in the M.2 slot. This is only a connector for the SIM card, its lines only lead to the M.2 slot.</p>
      <p>TODO: better name (Nano SIM feels confusing)</p>
    </td>
    <td>
    </td>
    <td>
    </td>
    <td>
    </td>
    <td>
    </td>
  </tr>
  <tr>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>M.2 module port</strong></p>
    </td>
    <td colSpan="1" rowSpan="1">
      <p>TODO: better name (Expansion port?), , full tech spec. Needs a separate block with description</p>
    </td>
  </tr>
  <tr>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>Debug port?</strong></p>
    </td>
    <td colSpan="1" rowSpan="1">
      <p>PLS1.27-2×7S — 2 rows of 7 contacts, male, 1.27mm</p>
      <p>In the connector: On the MCU side: RST, SWD, UART, 2xGPIO (the same GPIOs as in the GPIO Connector: 40, 41) On the SoC side: RST, UART, 2xGPIO *SoC SWD is located in the MicroSD connector</p>
      <p>Schematic</p>
      <p>TODO: better name</p>
    </td>
    <td>
    </td>
  </tr>
</table>

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/1SR0qCQMBYbxlUvYFxMX9_flipperone-ports-and-interfaces-v003.png)

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/nrxW81cCiJfuPqbDarJAs_flipperone-ports-and-interfaces-m2-v003.png)

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
