---
title: GPIO port
slug: hardware/gpio-port
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 12:58:00 GMT+0000 (Coordinated Universal Time)
---

![GPIO port](/files/pics/gpio-port-main.png)

The GPIO port is an expansion connector for external hardware modules. It exposes 3.3 V and 5 V power rails (both EFUSE-protected up to 2 A), USB 2.0 data lines, and a mix of MCU and CPU GPIO pins, which can be configured as pins for I²C, UART, SPI, CAN, PWM, I²S, SPDIF, and ADC inputs, as well as PIO (Programmable I/O) pins.

***

## GPIO port schematic

:::Iframe{code="<iframe src=&#x22;https://personal-viewer.365.altium.com/client/index.html?feature=embed&source=B379A8A7-9847-4DC4-887F-D328E3CC3FC8&activeView=SCH&#x22; width=&#x22;1280&#x22; height=&#x22;720&#x22; style=&#x22;overflow:hidden;border:none;width:100%;height:500px;&#x22; scrolling=&#x22;no&#x22; allowfullscreen=&#x22;true&#x22; onload=&#x22;window.top.scrollTo(0,0);&#x22;></iframe>" iframeHeight="500"}

:::

***

## GPIO port pinout

![Flipper One GPIO port pinout](/files/pics/gpio-port-pinout.jpg)

<table isTableHeaderOn="true" columnWidths="246,69,66,279">
  <tr>
    <td align="center">
      <p><strong>Description</strong></p>
    </td>
    <td align="center">
      <p><strong>PIN</strong></p>
    </td>
    <td align="center">
      <p><strong>PIN</strong></p>
    </td>
    <td align="center">
      <p><strong>Description</strong></p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>3.3 V Power, up to 2A EFUSE</p>
    </td>
    <td align="center">
      <p><strong>3V3</strong></p>
    </td>
    <td align="center">
      <p><strong>GND</strong></p>
    </td>
    <td align="center">
      <p>Ground</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>MCU GPIO 40</strong></p>
      <p>PIO</p>
      <p>ADC0</p>
      <p>PWM8_A</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center" colSpan="1" rowSpan="1">
      <p><strong>M40</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center" colSpan="1" rowSpan="1">
      <p><strong>M41</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>MCU GPIO 41</strong></p>
      <p>PWM8_B</p>
      <p>ADC1</p>
      <p>PIO</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><strong>CPU GPIO4_B4_D</strong></p>
      <p>SPDIF_RX0_M0</p>
      <p>I2C3_SDA_M0</p>
      <p>UART2_RX_M1</p>
      <p>CAN1_RX_M2</p>
    </td>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>B4</strong></p>
    </td>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>B5</strong></p>
    </td>
    <td align="center">
      <p><strong>CPU GPIO4_B5_D</strong></p>
      <p>CAN1_TX_M2</p>
      <p>UART2_TX_M1</p>
      <p>I2C3_SCL_M0</p>
      <p>SPDIF_TX0_M0</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>CPU GPIO4_B2_D</strong></p>
      <p>SAI1_SDO3_M0</p>
      <p>SAI1_SDI1_M0</p>
      <p>PDM1_SDI1_M1</p>
      <p>SPI4_MISO_M2</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center" colSpan="1" rowSpan="1">
      <p><strong>B2</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center" colSpan="1" rowSpan="1">
      <p><strong>B3</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>CPU GPIO4_B3_D</strong></p>
      <p>PWM2_CH7_M0</p>
      <p>SPI3_CSN1_M2</p>
      <p>SPI4_CSN0_M2</p>
      <p>PDM1_SDI0_M1</p>
      <p>SAI4_SDO_M0</p>
      <p>SAI1_SDI0_M0</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><strong>CPU GPIO4_B0_D</strong></p>
      <p>SAI1_SDO1_M0</p>
      <p>SAI1_SDI3_M0</p>
      <p>PDM1_CLK1_M1</p>
      <p>SPI4_CLK_M2</p>
      <p>UART5_TX_M1</p>
      <p>UART6_RTSN_M0</p>
      <p>UART2_RTSN_M1</p>
    </td>
    <td align="center">
      <p><strong>B0</strong></p>
    </td>
    <td align="center">
      <p><strong>B1</strong></p>
    </td>
    <td align="center">
      <p><strong>CPU GPIO4_B1_D</strong></p>
      <p>UART2_CTSN_M1</p>
      <p>UART6_CTSN_M0</p>
      <p>UART5_RX_M1</p>
      <p>SPI4_MOSI_M2</p>
      <p>PDM1_SDI2_M1</p>
      <p>SAI1_SDI2_M0</p>
      <p>SAI1_SDO2_M0</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>CPU GPIO4_A6_D</strong></p>
      <p>SAI4_LRCK_M0</p>
      <p>PDM1_CLK0_M1</p>
      <p>SPI3_MISO_M2</p>
      <p>I2C4_SDA_M1</p>
      <p>UART6_RX_M0</p>
      <p>CAN0_RX_M2</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>A6</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>A7</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>CPU GPIO4_A7_D</strong></p>
      <p>PWM2_CH6_M0</p>
      <p>SPI3_CLK_M2</p>
      <p>SAI4_SDI_M0</p>
      <p>SAI1_SDO0_M0</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><strong>CPU GPIO4_A4_D</strong></p>
      <p>SAI4_SCLK_M0</p>
      <p>PDM1_SDI3_M1</p>
      <p>SPI3_MOSI_M2</p>
      <p>I2C4_SCL_M1</p>
      <p>UART6_TX_M0</p>
      <p>CAN0_TX_M2</p>
    </td>
    <td align="center">
      <p><strong>A4</strong></p>
    </td>
    <td align="center">
      <p><strong>A5</strong></p>
    </td>
    <td align="center">
      <p><strong>CPU GPIO4_A5_D</strong></p>
      <p>I2C2_SDA_M2</p>
      <p>UART5_CTSN_M1</p>
      <p>SPI4_CSN1_M2</p>
      <p>SAI1_LRCK_M0</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center" colSpan="1" rowSpan="1">
      <p><strong>CPU GPIO4_A2_D</strong></p>
      <p>SAI1_MCLK_M0</p>
      <p>SAI4_MCLK_M0</p>
      <p>PWM2_CH5_M0</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center" colSpan="1" rowSpan="1">
      <p><strong>A2</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center" colSpan="1" rowSpan="1">
      <p><strong>A3</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center" colSpan="1" rowSpan="1">
      <p><strong>CPU GPIO4_A3_D</strong></p>
      <p>PWM2_CH4_M1</p>
      <p>I2C2_SCL_M2</p>
      <p>UART5_RTSN_M1</p>
      <p>SPI3_CSN0_M2</p>
      <p>SAI1_SCLK_M0</p>
    </td>
  </tr>
  <tr>
    <td align="center" colSpan="1" rowSpan="1">
      <p>5V Power, up to 2A EFUSE</p>
    </td>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>5V</strong></p>
    </td>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>GND</strong></p>
    </td>
    <td align="center" colSpan="1" rowSpan="1">
      <p>Ground</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center" colSpan="1" rowSpan="1">
      <p>CPU USB 2.0 Data+</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center" colSpan="1" rowSpan="1">
      <p><strong>D+</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center" colSpan="1" rowSpan="1">
      <p><strong>D-</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center" colSpan="1" rowSpan="1">
      <p>CPU USB 2.0 Data-</p>
    </td>
  </tr>
</table>

