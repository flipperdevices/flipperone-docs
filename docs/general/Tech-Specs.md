---
title: Tech specs
slug: general/tech-specs
docTags: 
createdAt: Wed Apr 22 2026 13:04:54 GMT+0000 (Coordinated Universal Time)
updatedAt: Wed Apr 22 2026 13:16:25 GMT+0000 (Coordinated Universal Time)
---

This page describes the full technical specifications of the Flipper One. Since the device is under active development, specifications may change.

![Flipper One outline](/files/pics/flipper_one_outline_no_screen.png)

***

## Size and weight

⚠️ Final dimensions and weight are pending — values below are placeholders.

![Flipper One — front view with dimensions](/files/pics/placeholder-size-front.png "Front view with height and width")

- **Height:** TBD mm (TBD inches)
- **Width:** TBD mm (TBD inches)
- **Depth:** TBD mm (TBD inches)
- **Weight:** TBD grams (TBD ounces)

***

## Materials

⚠️ Final material specifications are pending — values below are placeholders.

- **Body:** TBD
- **Back Plate:** TBD
- **Antenna Rail:** TBD
- **Radiator:** TBD
- **Loop:** TBD
- **Buttons:** TBD
- **Display lens:** TBD

***

## Monochrome LCD Display

- **Resolution:** 256 × 144 pixels
- **Grayscale:** 64 levels (6-bit)
- **Interface:** QSPI (driven by MCU)

***

## Ports

![Flipper One ports — top](/files/pics/flipper_one_ports_top.png "Flipper One ports — top")

![Flipper One ports — bottom](/files/pics/flipper_one_ports_bottom.png "Flipper One ports — bottom")

- **USB-C1:** USB 3.1 (5 Gbps), DisplayPort Alt Mode, USB Power Delivery charging
- **USB-C2:** USB 3.1 (5 Gbps), host only, power out
- **USB-A:** USB 3.1 (5 Gbps), host only, power out
- **HDMI:** full-size, v2.1
- **Ethernet:** 2× RJ45, Gigabit
- **3.5 mm jack:** stereo out + microphone input (TRRS)
- **MicroSD:** card slot
- **SIM card slot:** Nano SIM (4FF), passively connected to M.2 port

***

## Controls

⚠️ Final control specifications are pending — values below are placeholders.

- **Buttons:** TBD
- **Touch pad:** TBD

***

## Main CPU — RK3576

- **CPU:** Rockchip RK3576
- **Cores:** 8 — 4× high-performance ARM Cortex-A72 + 4× efficiency ARM Cortex-A53, up to 2.2 GHz
- **GPU:** ARM Mali G52 MC3 — OpenGL ES 1.1/2.0/3.2, OpenCL 2.1, Vulkan 1.2
- **NPU:** 6 TOPS @INT8 — supports int4, int8, int16, FP16, BF16, TF32

***

## Low-Power MCU — RP2350

- **MCU:** Raspberry Pi RP2350B
- **Cores:** Dual ARM Cortex-M33 @ 150 MHz + Dual RISC-V Hazard3 @ 150 MHz
- **SRAM:** 520 KB
- **Flash:** 16 MB

***

## Memory and Storage

- **RAM:** 8 GB LPDDR5
- **Internal storage:** 64 GB UFS 2.2
- **MicroSD card slot:** ⚠️ (UHS-I SDR104 — needs verification)

***

## Battery and Power

- **Battery energy:** 24000 mWh
- **Battery capacity:** 7000 mAh ⚠️ (not final)
- **Charger IC:** TI BQ25792, up to 3.32 A
- **Fuel Gauge:** TI BQ28Z610
- **Charging:** USB-C Power Delivery, up to 26 V

***

## Wi-Fi & Bluetooth

- **Module:** WXT2AM2101
- **Wi-Fi Chipset:** MediaTek MT7921AUN
- **Wi-Fi Modes:** Wi-Fi 6 (802.11ax), 2.4 / 5 / 6 GHz bands, 2×2 MIMO
- **Bluetooth:** 5.2 (integrated in MT7921U)

***

## Gigabit Ethernet

- **Ports:** 2× Ethernet (1 Gbit/s)
- **PHY IC:** Realtek RTL8211F-CG

***

## Video Output

- **HDMI:** v2.1, Full-size connector (Type-A), CEC support, up to 4K@120 Hz
- **DisplayPort:** v1.4 Alt Mode via USB-C1, up to 4K@120 Hz

***

## Audio

- **Codec:** Nuvoton NAU8822
- **Speaker:** ⚠️ needs clarification
- **3.5 mm jack:** stereo out + microphone input (TRRS)

***

## M.2 expansion port

The M.2 expansion port is at the back of the device, under the Back Plate.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/kBEYmNJI2QKW3dVel7tuQ-20260410-180703.png )

- **M.2 type:** Key B
- **Supported sizes:** 2242, 3042, 3052 mm
- **Supported thickness:** up to S3 (double-sided modules)
- **Interfaces:** PCIe 2.1 ×1 / USB 2.0 / USB 3.1 / SATA3 / Serial Audio / UART / I2C / SIM card

### M.2 pinout

TODO: replace to better picture

![Flipper One M.2 port pinout](files/pics/flipper_one_m2_port_pinout.png "Flipper One M.2 port pinout")

<table isTableHeaderOn="true" columnWidths="271,57,61,270">
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
      <p>CONFIG_2</p>
    </td>
    <td align="center">
      <p><strong>75</strong></p>
    </td>
    <td align="center">
      <p><strong>74</strong></p>
    </td>
    <td align="center">
      <p>3.3 V/VBAT</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>VIO_CFG (I) or GND</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>73</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>72</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>3.3 V/VBAT</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>GND</p>
    </td>
    <td align="center">
      <p><strong>71</strong></p>
    </td>
    <td align="center">
      <p><strong>70</strong></p>
    </td>
    <td align="center">
      <p>3.3 V/VBAT</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>CONFIG_1</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>69</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>68</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>SUSCLK (O)(0/1.8V/3.3V)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>RESET# (O)(0/1.8V)</p>
    </td>
    <td align="center">
      <p><strong>67</strong></p>
    </td>
    <td align="center">
      <p><strong>66</strong></p>
    </td>
    <td align="center">
      <p>SIM DETECT (O)</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>ANTCTL3 (I)(0/1.8V)</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>65</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>64</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>COEX_RXD (I)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>ANTCTL2 (I)(0/1.8V)</p>
    </td>
    <td align="center">
      <p><strong>63</strong></p>
    </td>
    <td align="center">
      <p><strong>62</strong></p>
    </td>
    <td align="center">
      <p>COEX_TXD (O)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>ANTCTL1 (I)(0/1.8V)</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>61</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>60</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>COEX3 (I/O)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>ANTCTL0 (I)(0/1.8V)</p>
    </td>
    <td align="center">
      <p><strong>59</strong></p>
    </td>
    <td align="center">
      <p><strong>58</strong></p>
    </td>
    <td align="center">
      <p>NC</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GND</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>57</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>56</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>NC</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>REFCLKp</p>
    </td>
    <td align="center">
      <p><strong>55</strong></p>
    </td>
    <td align="center">
      <p><strong>54</strong></p>
    </td>
    <td align="center">
      <p>PEWAKE# (I/O)(0/1.8V/3.3V)</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>REFCLKn</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>53</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>52</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>CLKREQ# (I/O)(0/1.8V/3.3V)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>GND</p>
    </td>
    <td align="center">
      <p><strong>51</strong></p>
    </td>
    <td align="center">
      <p><strong>50</strong></p>
    </td>
    <td align="center">
      <p>PERST# (O)(0/1.8V/3.3V)</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>PETp0/SATA-A+</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>49</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>48</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GPIO_4 (I/O)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>PETn0/SATA-A-</p>
    </td>
    <td align="center">
      <p><strong>47</strong></p>
    </td>
    <td align="center">
      <p><strong>46</strong></p>
    </td>
    <td align="center">
      <p>GPIO_3 (I/O)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GND</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>45</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>44</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GPIO_2 (I/O)/ALERT# (I)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>PERp0/SATA-B-</p>
    </td>
    <td align="center">
      <p><strong>43</strong></p>
    </td>
    <td align="center">
      <p><strong>42</strong></p>
    </td>
    <td align="center">
      <p>GPIO_1 (I/O)/SMB_DATA (I/O)/(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>PERn0/SATA-B+</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>41</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>40</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GPIO_0 (I/O)/SMB_CLK (I/O)/(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>GND</p>
    </td>
    <td align="center">
      <p><strong>39</strong></p>
    </td>
    <td align="center">
      <p><strong>38</strong></p>
    </td>
    <td align="center">
      <p>DEVSLP (O)</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>PETp1/USB3.1-Tx+/SSIC-TxP</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>37</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>36</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>UIM_PWR (I)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>PETn1/USB3.1-Tx-/SSIC-TxN</p>
    </td>
    <td align="center">
      <p><strong>35</strong></p>
    </td>
    <td align="center">
      <p><strong>34</strong></p>
    </td>
    <td align="center">
      <p>UIM_DATA (I/O)</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GND</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>33</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>32</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>UIM_CLK (I)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>PERp1/USB3.1-Rx+/SSIC-RxP</p>
    </td>
    <td align="center">
      <p><strong>31</strong></p>
    </td>
    <td align="center">
      <p><strong>30</strong></p>
    </td>
    <td align="center">
      <p>UIM_RESET (I)</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>PERn1/USB3.1-Rx-/SSIC-RxN</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>29</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>28</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>PLA_S2# (I)/GPIO_8 (I/O)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>GND</p>
    </td>
    <td align="center">
      <p><strong>27</strong></p>
    </td>
    <td align="center">
      <p><strong>26</strong></p>
    </td>
    <td align="center">
      <p>GPIO_10 (I/O)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>DPR (O)(0/1.8V)</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>25</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>24</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GPIO_7 (I/O)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>GPIO_11 (I/O)(0/1.8V)</p>
    </td>
    <td align="center">
      <p><strong>23</strong></p>
    </td>
    <td align="center">
      <p><strong>22</strong></p>
    </td>
    <td align="center">
      <p>GPIO_6 (I/O)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>CONFIG_0</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>21</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>20</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GPIO_5 (I/O)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>CONNECTOR KEY B</p>
    </td>
    <td align="center">
      <p><strong>—</strong></p>
    </td>
    <td align="center">
      <p><strong>—</strong></p>
    </td>
    <td align="center">
      <p>CONNECTOR KEY B</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GND</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>11</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>10</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GPIO_9/DAS/DSS (I/O)/LED_1# (I)(0/3.3V)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>USB_D-</p>
    </td>
    <td align="center">
      <p><strong>9</strong></p>
    </td>
    <td align="center">
      <p><strong>8</strong></p>
    </td>
    <td align="center">
      <p>W_DISABLE1# (O)(0/1.8V/3.3V)</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>USB_D+</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>7</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>6</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>FULL_CARD_POWER_OFF# (O)(0/1.8V or 3.3V)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>GND</p>
    </td>
    <td align="center">
      <p><strong>5</strong></p>
    </td>
    <td align="center">
      <p><strong>4</strong></p>
    </td>
    <td align="center">
      <p>3.3V</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GND</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>3</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>2</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>3.3V</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>CONFIG_3</p>
    </td>
    <td align="center">
      <p><strong>1</strong></p>
    </td>
    <td align="center">
      <p><strong>—</strong></p>
    </td>
    <td align="center">
      <p>—</p>
    </td>
  </tr>
</table>

***

## GPIO pinout

![Flipper One GPIO port pinout](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/IcHiPLMeaz2eQlQW1JkUw_flipperonegpioportpinout.jpg "Flipper One GPIO pinout")

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
      <p>ADC0</p>
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
      <p>SAI4_SD0_M0</p>
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
      <p>SAI4_SDI1_M0</p>
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

***

## Debug port

![Flipper One Debug Port Pinout](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/z2c8tayOgivlIyou_2bod_flipperonedebugportpinout.png "Flipper One Debug Port Pinout")

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
      <p>3V3 ⚠️ MCU POWER?</p>
    </td>
    <td align="center">
      <p><strong>1</strong></p>
    </td>
    <td align="center">
      <p><strong>2</strong></p>
    </td>
    <td align="center">
      <p>MCU RESET</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>MCU SWD CLOCK</p>
    </td>
    <td align="center">
      <p><strong>3</strong></p>
    </td>
    <td align="center">
      <p><strong>4</strong></p>
    </td>
    <td align="center">
      <p>MCU SWD IO</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>MCU UART TX</p>
    </td>
    <td align="center">
      <p><strong>5</strong></p>
    </td>
    <td align="center">
      <p><strong>6</strong></p>
    </td>
    <td align="center">
      <p>MCU UART RX</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>MCU GPIO 41</p>
    </td>
    <td align="center">
      <p><strong>7</strong></p>
    </td>
    <td align="center">
      <p><strong>8</strong></p>
    </td>
    <td align="center">
      <p>MCU GPIO 40</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>CPU RESET</p>
    </td>
    <td align="center">
      <p><strong>9</strong></p>
    </td>
    <td align="center">
      <p><strong>10</strong></p>
    </td>
    <td align="center">
      <p>CPU UART0 TX</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>CPU UART0 RX</p>
    </td>
    <td align="center">
      <p><strong>11</strong></p>
    </td>
    <td align="center">
      <p><strong>12</strong></p>
    </td>
    <td align="center">
      <p>CPU GPIO0_D2</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>CPU GPIO0_D3</p>
    </td>
    <td align="center">
      <p><strong>13</strong></p>
    </td>
    <td align="center">
      <p><strong>14</strong></p>
    </td>
    <td align="center">
      <p>GND</p>
    </td>
  </tr>
</table>

Will this affect the URL?
