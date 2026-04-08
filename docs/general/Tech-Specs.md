# Tech Specs

This page describes the full technical specifications of the Flipper One. Since the device is under active development, specifications may change.

![Flipper One outline](files/pics/flipper_one_outline_no_screen.png)

## Main CPU — RK3576

<table isTableHeaderOn="false" columnWidths="220,660">
  <tr>
    <td>
      <p><strong>CPU</strong></p>
    </td>
    <td>
      <p>Rockchip RK3576</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Cores</strong></p>
    </td>
    <td>
      <p>8 Cores up to 2.2 GHz<br><sub>(4x High-performance ARM Cortex-A72 + 4x Efficiency ARM Cortex-A53)</sub></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>GPU</strong></p>
    </td>
    <td>
      <p>ARM Mali G52 MC3 — OpenGL ES 1.1/2.0/3.2, OpenCL 2.1, Vulkan 1.2</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>NPU</strong></p>
    </td>
    <td>
      <p>6 TOPS @INT8<br><sub>Supports int4/int8/int16/FP16/BF16/TF32</sub></p>
    </td>
  </tr>
</table>

## Low-Power MCU — RP2350

<table isTableHeaderOn="false" columnWidths="220,660">
  <tr>
    <td>
      <p><strong>MCU</strong></p>
    </td>
    <td>
      <p>Raspberry Pi RP2350B</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Cores</strong></p>
    </td>
    <td>
      <p>Dual ARM Cortex-M33 @ 150 MHz + Dual RISC-V Hazard3 @ 150 MHz</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>SRAM</strong></p>
    </td>
    <td>
      <p>520 KB</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Flash</strong></p>
    </td>
    <td>
      <p>16 MB</p>
    </td>
  </tr>
</table>

## Memory and Storage

<table isTableHeaderOn="false" columnWidths="220,660">
  <tr>
    <td>
      <p><strong>RAM</strong></p>
    </td>
    <td>
      <p>8 GB LPDDR5</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Internal Storage</strong></p>
    </td>
    <td>
      <p>64 GB UFS 2.2</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>MicroSD</strong></p>
    </td>
    <td>
      <p>MicroSD card slot (⚠️UHS-I SDR104???)</p>
    </td>
  </tr>
</table>

## Battery and Power

<table isTableHeaderOn="false" columnWidths="220,660">
  <tr>
    <td>
      <p><strong>Battery</strong></p>
    </td>
    <td>
      <p>24000 mWh</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Charger IC</strong></p>
    </td>
    <td>
      <p>TI BQ25792, up to 3.32 A</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Fuel Gauge</strong></p>
    </td>
    <td>
      <p>TI BQ28Z610</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Charging</strong></p>
    </td>
    <td>
      <p>USB-C Power Delivery up to 26 V</p>
    </td>
  </tr>
</table>

## Monochrome LCD Display

<table isTableHeaderOn="false" columnWidths="220,660">
  <tr>
    <td>
      <p><strong>Resolution</strong></p>
    </td>
    <td>
      <p>256 x 144 pixels</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Grayscale</strong></p>
    </td>
    <td>
      <p>64 levels (6-bit)</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Interface</strong></p>
    </td>
    <td>
      <p>QSPI (driven by MCU)</p>
    </td>
  </tr>
</table>

## Wi-Fi & Bluetooth

<table isTableHeaderOn="false" columnWidths="220,660">
  <tr>
    <td>
      <p><strong>Module</strong></p>
    </td>
    <td>
      <p>WXT2AM2101</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Wi-Fi Chipset</strong></p>
    </td>
    <td>
      <p>MediaTek MT7921U</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Wi-Fi Modes</strong></p>
    </td>
    <td>
      <p>WiFi 6 (802.11ax), Bands 2.4 GHz / 5 GHz / 6 GHz, 2x2 MIMO</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Bluetooth</strong></p>
    </td>
    <td>
      <p>Bluetooth 5.2 (integrated in MT7921U)</p>
    </td>
  </tr>
</table>

## Gigabit Ethernet

<table isTableHeaderOn="false" columnWidths="220,660">
  <tr>
    <td>
      <p><strong>Ports</strong></p>
    </td>
    <td>
      <p>2x Ethernet (1 Gbit/s)</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>PHY IC</strong></p>
    </td>
    <td>
      <p>Realtek RTL8211F-CG</p>
    </td>
  </tr>
</table>

## Video Output

<table isTableHeaderOn="false" columnWidths="220,660">
  <tr>
    <td>
      <p><strong>HDMI</strong></p>
    </td>
    <td>
      <p>HDMI v2.1, Full-size connector (Type-A), CEC support, up to 4K@120 Hz</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Display Port</strong></p>
    </td>
    <td>
      <p>DisplayPort v1.4 Alt Mode via USB-C1, up to 4K@120 Hz</p>
    </td>
  </tr>
</table>

## Audio

<table isTableHeaderOn="false" columnWidths="220,660">
  <tr>
    <td>
      <p><strong>Codec</strong></p>
    </td>
    <td>
      <p>Nuvoton NAU8822</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Speaker</strong></p>
    </td>
    <td>
      <p>&#x26a0;&#xfe0f; NEEDS CLARIFICATION</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>3.5 Audio</strong></p>
    </td>
    <td>
      <p>3.5 mm Audio Jack, Stereo Out + Microphone Input (TRRS)</p>
    </td>
  </tr>
</table>

## Ports

![Flipper One ports — top](files/pics/flipper_one_ports_top.png "Flipper One ports — top")

![Flipper One ports — bottom](files/pics/flipper_one_ports_bottom.png "Flipper One ports — bottom")

<table isTableHeaderOn="false" columnWidths="220,660">
  <tr>
    <td>
      <p><strong>USB-C1</strong></p>
    </td>
    <td>
      <p>USB 3.1 (5 Gbps) + DisplayPort Alt Mode + USB Power Delivery charging</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>USB-C2</strong></p>
    </td>
    <td>
      <p>USB 3.1 (5 Gbps), Host Only, Power Out</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>USB-A</strong></p>
    </td>
    <td>
      <p>USB 3.1 (5 Gbps), Host Only, Power Out</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>HDMI</strong></p>
    </td>
    <td>
      <p>Full-size HDMI v2.1</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Ethernet</strong></p>
    </td>
    <td>
      <p>2x RJ45 Gigabit Ethernet</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>3.5 Audio Out</strong></p>
    </td>
    <td>
      <p>3.5 mm Audio Jack</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>MicroSD</strong></p>
    </td>
    <td>
      <p>MicroSD card slot</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>SIM Card Slot</strong></p>
    </td>
    <td>
      <p>Nano SIM (4FF), passively connected to M.2 port</p>
    </td>
  </tr>
</table>

## M.2 Expansion Port


<table isTableHeaderOn="false" columnWidths="220,660">
  <tr>
    <td>
      <p><strong>M.2 Type</strong></p>
    </td>
    <td>
      <p>Key B</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Supported Sizes</strong></p>
    </td>
    <td>
      <p>2242, 3042, 3052 mm</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Supported Thickness</strong></p>
    </td>
    <td>
      <p>Up to S3 (double-sided modules)</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Interfaces</strong></p>
    </td>
    <td>
      <p>PCIe 2.1 x1 / USB 2.0 / USB 3.1 / SATA3 / Serial Audio / UART / I2C / SIM card</p>
    </td>
  </tr>
</table>

## GPIO Pinout

![Flipper One GPIO port pinout](files/pics/flipper_one_gpio_port_pinout.jpg "Flipper One GPIO pinout")

<table isTableHeaderOn="true" columnWidths="360,80,80,360">
  <tr>
    <td><p>Pin Description</p></td>
    <td align="center"><p>PIN</p></td>
    <td align="center"><p>PIN</p></td>
    <td><p>Pin Description</p></td>
  </tr>
  <tr>
    <td><p>3.3 V Power, up to 2A EFUSE</p></td>
    <td align="center"><p><strong>3V3</strong></p></td>
    <td align="center"><p><strong>GND</strong></p></td>
    <td><p>Ground</p></td>
  </tr>
  <tr>
    <td><p>MCU GPIO 40 (Connected to Raspberry Pi MCU RP2350), PIO, ADC0, PWM8_A</p></td>
    <td align="center"><p><strong>M40</strong></p></td>
    <td align="center"><p><strong>M41</strong></p></td>
    <td><p>MCU GPIO 41 (Connected to Raspberry Pi MCU RP2350), ADC0, PIO, PWM8_B</p></td>
  </tr>
  <tr>
    <td><p>CPU GPIO4_B4_D, SPDIF_RX0_M0, I2C3_SDA_M0, UART2_RX_M1, CAN1_RX_M2</p></td>
    <td align="center"><p><strong>B4</strong></p></td>
    <td align="center"><p><strong>B5</strong></p></td>
    <td><p>CPU GPIO4_B5_D, SPDIF_TX0_M0, I2C3_SCL_M0, UART2_TX_M1, CAN1_TX_M2</p></td>
  </tr>
  <tr>
    <td><p>CPU GPIO4_B2_D, SAI1_SDO3_M0, SAI1_SDI1_M0, PDM1_SDI1_M1, SPI4_MISO_M2</p></td>
    <td align="center"><p><strong>B2</strong></p></td>
    <td align="center"><p><strong>B3</strong></p></td>
    <td><p>CPU GPIO4_B3_D, PWM2_CH7_M0, SPI3_CSN1_M2, SPI4_CSN0_M2, PDM1_SDI0_M1, SAI4_SD0_M0, SAI1_SDI0_M0</p></td>
  </tr>
  <tr>
    <td><p>CPU GPIO4_B0_D, SAI1_SDO1_M0, SAI1_SDI3_M0, PDM1_CLK1_M1, SPI4_CLK_M2, UART5_TX_M1, UART6_RTSN_M0, UART2_RTSN_M1</p></td>
    <td align="center"><p><strong>B0</strong></p></td>
    <td align="center"><p><strong>B1</strong></p></td>
    <td><p>CPU GPIO4_B1_D, UART2_CTSN_M1, UART6_CTSN_M0, UART5_RX_M1, SPI4_MOSI_M2, PDM1_SDI2_M1, SAI1_SDI2_M0, SAI1_SDO2_M0</p></td>
  </tr>
  <tr>
    <td><p>CPU GPIO4_A6_D, SAI4_LRCK_M0, PDM1_CLK0_M1, SPI3_MISO_M2, I2C4_SDA_M1, UART6_RX_M0, CAN0_RX_M2</p></td>
    <td align="center"><p><strong>A6</strong></p></td>
    <td align="center"><p><strong>A7</strong></p></td>
    <td><p>CPU GPIO4_A7_D, PWM2_CH6_M0, SPI3_CLK_M2, SAI4_SDI1_M0, SAI1_SDO0_M0</p></td>
  </tr>
  <tr>
    <td><p>CPU GPIO4_A4_D, SAI4_SCLK_M0, PDM1_SDI3_M1, SPI3_MOSI_M2, I2C4_SCL_M1, UART6_TX_M0, CAN0_TX_M2</p></td>
    <td align="center"><p><strong>A4</strong></p></td>
    <td align="center"><p><strong>A5</strong></p></td>
    <td><p>CPU GPIO4_A5_D, I2C2_SDA_M2, UART5_CTSN_M1, SPI4_CSN1_M2, SAI1_LRCK_M0</p></td>
  </tr>
  <tr>
    <td><p>CPU GPIO4_A2_D, SAI1_MCLK_M0, SAI4_MCLK_M0, PWM2_CH5_M0</p></td>
    <td align="center"><p><strong>A2</strong></p></td>
    <td align="center"><p><strong>A3</strong></p></td>
    <td><p>CPU GPIO4_A3_D, PWM2_CH4_M1, I2C2_SCL_M2, UART5_RTSN_M1, SPI3_CSN0_M2, SAI1_SCLK_M0</p></td>
  </tr>
  <tr>
    <td><p>5V Power, up to 2A EFUSE</p></td>
    <td align="center"><p><strong>5V</strong></p></td>
    <td align="center"><p><strong>GND</strong></p></td>
    <td><p>Ground</p></td>
  </tr>
  <tr>
    <td><p>CPU USB 2.0 Data+</p></td>
    <td align="center"><p><strong>D+</strong></p></td>
    <td align="center"><p><strong>D-</strong></p></td>
    <td><p>CPU USB 2.0 Data-</p></td>
  </tr>
</table>

## Debug port 

![Flipper One Debug Port Pinout](files/pics/flipper_one_debug_port_pinout.png "Flipper One Debug Port Pinout")

Description | PIN | PIN | Description
--- | --- | --- | ---
3V3 ⚠️ MCU POWER? | 1  |  2 |  MCU RESET
MCU SWD CLOCK     | 3  |  4 |  MCU SWD IO
MCU UART TX       | 5  |  6 |  MCU UART RX
MCU GPIO 41       | 7  |  8 |  MCU GPIO 40
CPU RESET         | 9  | 10 |  CPU UART0 TX
CPU UART0 RX      | 11 | 12 |  CPU GPIO0_D2
CPU GPIO0_D3      | 13 | 14 |  GND