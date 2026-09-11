---
title: Firmware update
slug: mcu-firmware/firmware-update
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:14:38 GMT+0000 (Coordinated Universal Time)
---

This page explains how to flash the MCU firmware file (`.UF2`) to the Flipper One MCU via USB. The process differs depending on the Flipper One hardware revision.

***

# Identify the hardware revision

You can identify Flipper One hardware revision by checking the following:

<table isTableHeaderOn="true" columnWidths="80,80,80">
  <tr>
    <td align="center"><p><strong>Difference</strong></p></td>
    <td align="center"><p><strong>Rev. F0B0C1</strong></p></td>
    <td align="center"><p><strong>Rev. 2.F0B1C2</strong></p></td>
  </tr>
  <tr>
    <td>Label on the Main PCB</td>
    <td align="center">ONE-Main-F0B0C1</td>
    <td align="center">ONE-Main-2.F0B1C2</td>
  </tr>
  <tr>
    <td>Screws on the back</td>
    <td align="center">5 Hex screws</td>
    <td align="center">6 Philips screws</td>
  </tr>
  <tr>
    <td>LAN port LEDs visible</td>
    <td align="center">No</td>
    <td align="center">Yes</td>
  </tr>
  <tr>
    <td>LED in the Power button</td>
    <td align="center">No</td>
    <td align="center">Yes</td>
  </tr>
</table>

If you are still unsure which hardware revision you have, try both guides one after the other.

***

# Flash the MCU firmware

To flash firmware to the Flipper One MCU:

:::::::::::Tabs
::::::::::Tab{title="On rev. F0B0C1"}

:::::::::WorkflowBlock
::::::::WorkflowBlockItem

Get the `flipper-one-mcu-f1-firmware-*.uf2` file, where `f1` corresponds to the F0B0C1 revision. There are two options:
- Download the file from the [Update Server](https://update.flipperzero.one/builds/flipper-one-mcu/dev/).
- [Build the file from source](How-to-build-firmware.md) if you have modified the firmware source code.
::::::::

::::::::WorkflowBlockItem
Connect Flipper One to your PC via the **USB-C 1** port.

![](/files/pics/mcu-firmware-usbc1-connection.png)
::::::::
 
::::::::WorkflowBlockItem
Switch the MCU to **BOOTSEL (DFU)** mode. There are two ways to do this:
- **Via the App Switcher menu.** This method works if MCU mode is working on your device.
- **Using a button combination.** This method works even if the MCU has never been flashed before and MCU mode is not working.

To Switch the MCU to BOOTSEL (DFU) mode:

:::::::Tabs
::::::Tab{title="Via the App Switcher menu"}

:::::WorkflowBlock

::::WorkflowBlockItem
Switch the device to MCU mode. Turn it on if it is off, and stop Flipper OS if it is running.
::::

::::WorkflowBlockItem
Press the :inlineImage[]{src="/files/icons/app-switcher-button.png"} **App switcher** button from the MCU mode main screen.
::::

::::WorkflowBlockItem
Press the **DFU** soft button.
::::
:::::

::::::
::::::Tab{title="Using a button combination"}

:::::WorkflowBlock

::::WorkflowBlockItem
Press and hold the **PTT** button.

![BOOTSEL step 1: hold PTT button](/files/pics/mcu-bootsel-f0b0c1-step-1.png)
::::
::::WorkflowBlockItem
Keep holding **PTT** button. Press and hold **Left** and **Back** buttons for **3 seconds**, then release.

![BOOTSEL step 2: hold Left and Back buttons](/files/pics/mcu-bootsel-f0b0c1-step-2.png)
::::

::::WorkflowBlockItem

Release the **PTT** button.

![BOOTSEL step 3: release PTT button](/files/pics/mcu-bootsel-f0b0c1-step-3.png)

::::
:::::

::::::
:::::::

After switching the MCU to BOOTSEL mode, Flipper One's screen backlight will turn OFF and the device will appear on your PC as a Mass Storage Device named `RP2350`. If Flipper One does not appear, try a different USB cable and repeat the BOOTSEL procedure.

::::::::
 
::::::::WorkflowBlockItem
Upload the `.UF2` firmware file to the Mass Storage Device.

:::Iframe{code="<video&#xA;    autoplay muted loop playsinline style=&#x22;width: 100%; margin: 0 !important;&#x22;&#xA;    src=&#x22;https://cdn.flipperzero.one/Upload_uf2_file.mp4&#x22;&#xA;></video>" iframeHeight="350"}
:::

:::hint{type="success"}
**MCU firmware successfully updated!**
Once the `.UF2` file upload is complete, Flipper One will automatically reboot, and the Mass Storage Device will disconnect from your PC.
:::

::::::::
:::::::::

::::::::::

::::::::::Tab{title="On rev. 2.F0B1C2"}

:::::::::WorkflowBlock
::::::::WorkflowBlockItem

Get the `flipper-one-mcu-f2-firmware-*.uf2` file, where `f2` corresponds to the 2.F0B1C2 revision. There are two options:
- Download the file from the [Update Server](https://update.flipperzero.one/builds/flipper-one-mcu/dev/).
- [Build the file from source](How-to-build-firmware.md) if you have modified the firmware source code.
::::::::

::::::::WorkflowBlockItem
Connect Flipper One to your PC via the **USB-C 1** port.

![](/files/pics/mcu-firmware-usbc1-connection.png)
::::::::
 
::::::::WorkflowBlockItem
Switch the MCU to **BOOTSEL (DFU)** mode. There are two ways to do this:
- **Via the App Switcher menu.** This method works if MCU mode is working on your device.
- **Using a button combination.** This method works even if the MCU has never been flashed before and MCU mode is not working.

To Switch the MCU to BOOTSEL (DFU) mode:

:::::::Tabs
::::::Tab{title="Via the App Switcher menu"}

:::::WorkflowBlock

::::WorkflowBlockItem
Switch the device to MCU mode. Turn it on if it is off, and stop Flipper OS if it is running.
::::

::::WorkflowBlockItem
Press the :inlineImage[]{src="/files/icons/app-switcher-button.png"} **App switcher** button from the MCU mode main screen.
::::

::::WorkflowBlockItem
Press the **DFU** soft button.
::::
:::::

::::::
::::::Tab{title="Using a button combination"}

:::::WorkflowBlock

::::WorkflowBlockItem
**Step 1:** Press and hold the :inlineImage[]{src="/files/icons/esc-button.png"} and :inlineImage[]{src="/files/icons/run-button.png"} buttons.

![BOOTSEL step 1: hold the Esc and Run buttons](/files/pics/mcu-bootsel-2f0b1c2-step-1.png)
::::
::::WorkflowBlockItem
**Step 2:** Keep holding the :inlineImage[]{src="/files/icons/esc-button.png"} **Esc** and :inlineImage[]{src="/files/icons/run-button.png"} **Run** buttons. Press and hold **Left** and **Back** buttons for **3 seconds**, then release.

![BOOTSEL step 2: hold Left and Back buttons](/files/pics/mcu-bootsel-2f0b1c2-step-2.png)
::::
::::WorkflowBlockItem
**Step 3:** Release the :inlineImage[]{src="/files/icons/esc-button.png"} **Esc** and :inlineImage[]{src="/files/icons/run-button.png"} **Run** buttons.

![BOOTSEL step 3: release hold the Esc and Run buttons](/files/pics/mcu-bootsel-2f0b1c2-step-3.png)
::::
:::::

::::::
:::::::

After switching the MCU to BOOTSEL mode, Flipper One's backlight will turn OFF, the Power button LED will turn purple, and the device will appear on your PC as a Mass Storage Device named `FlipperOneMCU`. If Flipper One does not appear, try a different USB cable and repeat the BOOTSEL procedure.

::::::::
 
::::::::WorkflowBlockItem
Upload the `.UF2` firmware file to the Mass Storage Device.

:::Iframe{code="<video&#xA;    autoplay muted loop playsinline style=&#x22;width: 100%; margin: 0 !important;&#x22;&#xA;    src=&#x22;https://cdn.flipperzero.one/Upload_uf2_file.mp4&#x22;&#xA;></video>" iframeHeight="350"}
:::

:::hint{type="success"}
**MCU firmware successfully updated!**
Once the `.UF2` file upload is complete, Flipper One will automatically reboot, and the Mass Storage Device will disconnect from your PC.
:::

::::::::
:::::::::

::::::::::
:::::::::::
