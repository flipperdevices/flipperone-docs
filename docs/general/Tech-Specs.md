---
title: Tech Specs
slug: general/tech-specs
docTags: 
createdAt: Wed Apr 08 2026 17:29:37 GMT+0000 (Coordinated Universal Time)
updatedAt: Thu Apr 09 2026 13:11:23 GMT+0000 (Coordinated Universal Time)
---

This page describes the full technical specifications of the Flipper One. Since the device is under active development, specifications may change.

![Flipper One outline](files/pics/flipper_one_outline_no_screen.png)

## Main CPU — RK3576

<table isTableHeaderOn="false" columnWidths="101,560">
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
      <p>8 Cores up to 2.2 GHz
      (4x High-performance ARM Cortex-A72 + 4x Efficiency ARM Cortex-A53)</p>
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
      <p>6 TOPS @INT8
      Supports int4/int8/int16/FP16/BF16/TF32</p>
    </td>
  </tr>
</table>



## Low-Power MCU — RP2350

<table isTableHeaderOn="false" columnWidths="101,560" selectedColumns="" selectedRows="" selectedTable="false">
  <tr>
    <td align="left">
      <p><strong>MCU</strong></p>
    </td>
    <td align="left">
      <p>Raspberry Pi RP2350B</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p><strong>Cores</strong></p>
    </td>
    <td align="left">
      <p>Dual ARM Cortex-M33 @ 150 MHz + Dual RISC-V Hazard3 @ 150 MHz</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p><strong>SRAM</strong></p>
    </td>
    <td align="left">
      <p>520 KB</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p><strong>Flash</strong></p>
    </td>
    <td align="left">
      <p>16 MB</p>
    </td>
  </tr>
</table>



## Memory and Storage

<table isTableHeaderOn="false" columnWidths="101,560" selectedColumns="" selectedRows="" selectedTable="false">
  <tr>
    <td align="left">
      <p><strong>RAM</strong></p>
    </td>
    <td align="left">
      <p>8 GB LPDDR5</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p><strong>Internal Storage</strong></p>
    </td>
    <td align="left">
      <p>64 GB UFS 2.2</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p><strong>MicroSD</strong></p>
    </td>
    <td align="left">
      <p>MicroSD card slot (⚠️UHS-I SDR104???)</p>
    </td>
  </tr>
</table>



## Battery and Power

<table isTableHeaderOn="false" columnWidths="101,560" selectedColumns="" selectedRows="" selectedTable="false">
  <tr>
    <td align="left">
      <p><strong>Battery</strong></p>
    </td>
    <td align="left">
      <p>24000 mWh</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p><strong>Charger IC</strong></p>
    </td>
    <td align="left">
      <p>TI BQ25792, up to 3.32 A</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p><strong>Fuel Gauge</strong></p>
    </td>
    <td align="left">
      <p>TI BQ28Z610</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p><strong>Charging</strong></p>
    </td>
    <td align="left">
      <p>USB-C Power Delivery up to 26 V</p>
    </td>
  </tr>
</table>



## Monochrome LCD Display

<table isTableHeaderOn="false" columnWidths="101,560" selectedColumns="" selectedRows="" selectedTable="false">
  <tr>
    <td align="left">
      <p><strong>Resolution</strong></p>
    </td>
    <td align="left">
      <p>256 x 144 pixels</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p><strong>Grayscale</strong></p>
    </td>
    <td align="left">
      <p>64 levels (6-bit)</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p><strong>Interface</strong></p>
    </td>
    <td align="left">
      <p>QSPI (driven by MCU)</p>
    </td>
  </tr>
</table>



## Wi-Fi & Bluetooth

<table isTableHeaderOn="false" columnWidths="101,560" selectedColumns="" selectedRows="" selectedTable="false">
  <tr>
    <td align="left">
      <p><strong>Module</strong></p>
    </td>
    <td align="left">
      <p>WXT2AM2101</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p><strong>Wi-Fi Chipset</strong></p>
    </td>
    <td align="left">
      <p>MediaTek MT7921U</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p><strong>Wi-Fi Modes</strong></p>
    </td>
    <td align="left">
      <p>WiFi 6 (802.11ax), Bands 2.4 GHz / 5 GHz / 6 GHz, 2x2 MIMO</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p><strong>Bluetooth</strong></p>
    </td>
    <td align="left">
      <p>Bluetooth 5.2 (integrated in MT7921U)</p>
    </td>
  </tr>
</table>



## Gigabit Ethernet

<table isTableHeaderOn="false" columnWidths="101,560" selectedColumns="" selectedRows="" selectedTable="false">
  <tr>
    <td align="left">
      <p><strong>Ports</strong></p>
    </td>
    <td align="left">
      <p>2x Ethernet (1 Gbit/s)</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p><strong>PHY IC</strong></p>
    </td>
    <td align="left">
      <p>Realtek RTL8211F-CG</p>
    </td>
  </tr>
</table>



## Video Output

<table isTableHeaderOn="false" columnWidths="114,547" selectedColumns="" selectedRows="" selectedTable="false">
  <tr>
    <td align="left">
      <p><strong>HDMI</strong></p>
    </td>
    <td align="left">
      <p>HDMI v2.1, Full-size connector (Type-A), CEC support, up to 4K@120 Hz</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p><strong>Display Port</strong></p>
    </td>
    <td align="left">
      <p>DisplayPort v1.4 Alt Mode via USB-C1, up to 4K@120 Hz</p>
    </td>
  </tr>
</table>



## Audio

<table isTableHeaderOn="false" columnWidths="101,560" selectedColumns="" selectedRows="" selectedTable="false">
  <tr>
    <td align="left">
      <p><strong>Codec</strong></p>
    </td>
    <td align="left">
      <p>Nuvoton NAU8822</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p><strong>Speaker</strong></p>
    </td>
    <td align="left">
      <p>⚠️ NEEDS CLARIFICATION</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p><strong>3.5 Audio</strong></p>
    </td>
    <td align="left">
      <p>3.5 mm Audio Jack, Stereo Out + Microphone Input (TRRS)</p>
    </td>
  </tr>
</table>



## Ports

![Flipper One ports — top](files/pics/flipper_one_ports_top.png "Flipper One ports — top")

![Flipper One ports — bottom](files/pics/flipper_one_ports_bottom.png "Flipper One ports — bottom")

<table isTableHeaderOn="false" columnWidths="131,530">
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
    <td colSpan="1" rowSpan="1">
      <p><strong>Ethernet</strong></p>
    </td>
    <td colSpan="1" rowSpan="1">
      <p>2x RJ45 Gigabit Ethernet</p>
    </td>
  </tr>
  <tr>
    <td colSpan="1" rowSpan="1">
      <p><strong>3.5 Audio Out</strong></p>
    </td>
    <td colSpan="1" rowSpan="1">
      <p>3.5 mm Audio Jack</p>
    </td>
  </tr>
  <tr>
    <td colSpan="1" rowSpan="1">
      <p><strong>MicroSD</strong></p>
    </td>
    <td colSpan="1" rowSpan="1">
      <p>MicroSD card slot</p>
    </td>
  </tr>
  <tr>
    <td colSpan="1" rowSpan="1">
      <p><strong>SIM Card Slot</strong></p>
    </td>
    <td colSpan="1" rowSpan="1">
      <p>Nano SIM (4FF), passively connected to M.2 port</p>
    </td>
  </tr>
</table>



## M.2 expansion port

\<add image>

<table isTableHeaderOn="false" columnWidths="178,483">
  <tr>
    <td>
      <p><strong>M.2 type</strong></p>
    </td>
    <td>
      <p>Key B</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Supported sizes</strong></p>
    </td>
    <td>
      <p>2242, 3042, 3052 mm</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Supported thickness</strong></p>
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



### M.2 pinout

TODO: replace to better picture

![Flipper One M.2 port pinout](files/pics/flipper_one_m2_port_pinout.png "Flipper One M.2 port pinout")

<table isTableHeaderOn="true" columnWidths="271,57.85231000546746,61.52111037241076,270.62657962212177">
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
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p>VIO_CFG (I) or GND</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>73</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>72</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
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
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p>CONFIG_1</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>69</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>68</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
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
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p>ANTCTL3 (I)(0/1.8V)</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>65</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>64</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
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
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p>ANTCTL1 (I)(0/1.8V)</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>61</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>60</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
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
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p>GND</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>57</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>56</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
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
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p>REFCLKn</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>53</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>52</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
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
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p>PETp0/SATA-A+</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>49</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>48</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
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
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p>GND</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>45</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>44</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
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
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p>PERn0/SATA-B+</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>41</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>40</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
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
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p>PETp1/USB3.1-Tx+/SSIC-TxP</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>37</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>36</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
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
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p>GND</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>33</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>32</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
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
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p>PERn1/USB3.1-Rx-/SSIC-RxN</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>29</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>28</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
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
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p>DPR (O)(0/1.8V)</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>25</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>24</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
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
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p>CONFIG_0</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>21</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>20</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
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
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p>GND</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>11</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>10</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
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
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p>USB_D+</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>7</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>6</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
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
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p>GND</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>3</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>2</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
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



## GPIO pinout

![Flipper One GPIO port pinout](files/pics/flipper_one_gpio_port_pinout.jpg "Flipper One GPIO pinout")

<table isTableHeaderOn="true" columnWidths="246,69.06742249685797,66.7895362847853,279.14304121835676" selectedColumns="" selectedRows="" selectedTable="false">
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
      <p>3.3 V Power, up to 2A EFUSE </p>
    </td>
    <td align="center">
      <p><strong>3V3</strong></p>
    </td>
    <td align="center">
      <p><strong>GND</strong></p>
    </td>
    <td align="center">
      <p>Ground </p>
    </td>
  </tr>
  <tr>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>MCU GPIO 40 </strong></p>
      <p>PIO </p>
      <p>ADC0 </p>
      <p>PWM8_A </p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff" colSpan="1" rowSpan="1">
      <p><strong>M40</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff" colSpan="1" rowSpan="1">
      <p><strong>M41</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>MCU GPIO 41 </strong></p>
      <p>PWM8_B </p>
      <p>ADC0 </p>
      <p>PIO </p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><strong>CPU GPIO4_B4_D </strong></p>
      <p>SPDIF_RX0_M0 </p>
      <p>I2C3_SDA_M0 </p>
      <p>UART2_RX_M1 </p>
      <p>CAN1_RX_M2 </p>
    </td>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>B4</strong></p>
    </td>
    <td align="center" colSpan="1" rowSpan="1">
      <p><strong>B5</strong></p>
    </td>
    <td align="center">
      <p><strong>CPU GPIO4_B5_D </strong></p>
      <p>CAN1_TX_M2 </p>
      <p>UART2_TX_M1 </p>
      <p>I2C3_SCL_M0 </p>
      <p>SPDIF_TX0_M0 </p>
    </td>
  </tr>
  <tr>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>CPU GPIO4_B2_D </strong></p>
      <p>SAI1_SDO3_M0 </p>
      <p>SAI1_SDI1_M0 </p>
      <p>PDM1_SDI1_M1 </p>
      <p>SPI4_MISO_M2 </p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff" colSpan="1" rowSpan="1">
      <p><strong>B2</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff" colSpan="1" rowSpan="1">
      <p><strong>B3</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>CPU GPIO4_B3_D </strong></p>
      <p>PWM2_CH7_M0 </p>
      <p>SPI3_CSN1_M2 </p>
      <p>SPI4_CSN0_M2 </p>
      <p>PDM1_SDI0_M1 </p>
      <p>SAI4_SD0_M0 </p>
      <p>SAI1_SDI0_M0 </p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><strong>CPU GPIO4_B0_D</strong> SAI1_SDO1_M0 </p>
      <p>SAI1_SDI3_M0 </p>
      <p>PDM1_CLK1_M1 </p>
      <p>SPI4_CLK_M2 </p>
      <p>UART5_TX_M1 UART6_RTSN_M0 </p>
      <p>UART2_RTSN_M1 </p>
    </td>
    <td align="center">
      <p><strong>B0</strong></p>
    </td>
    <td align="center">
      <p><strong>B1</strong></p>
    </td>
    <td align="center">
      <p><strong>CPU GPIO4_B1_D </strong>UART2_CTSN_M1 UART6_CTSN_M0 </p>
      <p>UART5_RX_M1 </p>
      <p>SPI4_MOSI_M2 </p>
      <p>PDM1_SDI2_M1 </p>
      <p>SAI1_SDI2_M0 </p>
      <p>SAI1_SDO2_M0 </p>
    </td>
  </tr>
  <tr>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>CPU GPIO4_A6_D</strong> SAI4_LRCK_M0 PDM1_CLK0_M1 SPI3_MISO_M2</p>
      <p> I2C4_SDA_M1 </p>
      <p>UART6_RX_M0 </p>
      <p>CAN0_RX_M2</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>A6</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>A7</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff">
      <p><strong>CPU GPIO4_A7_D</strong></p>
      <p>PWM2_CH6_M0 </p>
      <p>SPI3_CLK_M2 </p>
      <p>SAI4_SDI1_M0 </p>
      <p>SAI1_SDO0_M0</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><strong>CPU GPIO4_A4_D</strong> SAI4_SCLK_M0 PDM1_SDI3_M1 SPI3_MOSI_M2</p>
      <p> I2C4_SCL_M1</p>
      <p> UART6_TX_M0</p>
      <p> CAN0_TX_M2</p>
    </td>
    <td align="center">
      <p><strong>A4</strong></p>
    </td>
    <td align="center">
      <p><strong>A5</strong></p>
    </td>
    <td align="center">
      <p><strong>CPU GPIO4_A5_D</strong></p>
      <p> I2C2_SDA_M2</p>
      <p> UART5_CTSN_M1</p>
      <p> SPI4_CSN1_M2</p>
      <p> SAI1_LRCK_M0</p>
    </td>
  </tr>
  <tr>
    <td align="center" lightBackgroundColor="#f0f7ff" colSpan="1" rowSpan="1">
      <p><strong>CPU GPIO4_A2_D </strong> SAI1_MCLK_M0 </p>
      <p>SAI4_MCLK_M0 </p>
      <p>PWM2_CH5_M0 </p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff" colSpan="1" rowSpan="1">
      <p><strong>A2</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff" colSpan="1" rowSpan="1">
      <p><strong>A3</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff" colSpan="1" rowSpan="1">
      <p><strong>CPU GPIO4_A3_D</strong> </p>
      <p>PWM2_CH4_M1 </p>
      <p>I2C2_SCL_M2 </p>
      <p>UART5_RTSN_M1 </p>
      <p>SPI3_CSN0_M2 </p>
      <p>SAI1_SCLK_M0 </p>
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
    <td align="center" lightBackgroundColor="#f0f7ff" colSpan="1" rowSpan="1">
      <p>CPU USB 2.0 Data+</p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff" colSpan="1" rowSpan="1">
      <p><strong>D+</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff" colSpan="1" rowSpan="1">
      <p><strong>D-</strong></p>
    </td>
    <td align="center" lightBackgroundColor="#f0f7ff" colSpan="1" rowSpan="1">
      <p>CPU USB 2.0 Data-</p>
    </td>
  </tr>
</table>



## Debug port

![Flipper One Debug Port Pinout](files/pics/flipper_one_debug_port_pinout.png "Flipper One Debug Port Pinout")

<table isTableHeaderOn="true" columnWidths="246,69.06742249685797,66.7895362847853,279.14304121835676">
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

