---
title: M.2 port
slug: hardware/m2-port
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 12:57:35 GMT+0000 (Coordinated Universal Time)
---

![Flipper One M.2 expansion port](/files/pics/m2-expansion-port.png)

The M.2 port is an internal expansion slot for cellular modems, Wi-Fi, SDR, NVMe SSDs, GNSS modules, AI accelerators, and similar off-the-shelf M.2 modules. It sits at the back of the device, under the Back Plate.

**Tech specs:**

- **M.2 type:** Key B
- **Supported sizes:** 2242, 3042, 3052
- **Supported thickness:** up to D3 (double-sided modules)
- **Interfaces:** PCIe 2.1 ×1 / USB 2.0 / USB 3.1 / SATA3 / Serial Audio / UART / I²C / SIM card + eSIM

***

## M.2 port schematic

:::Iframe{code="<iframe src=&#x22;https://personal-viewer.365.altium.com/client/index.html?feature=embed&source=B61B98C6-CB3B-41BC-955F-FA98C558A671&activeView=SCH&#x22; width=&#x22;1280&#x22; height=&#x22;720&#x22; style=&#x22;overflow:hidden;border:none;width:100%;height:500px;&#x22; scrolling=&#x22;no&#x22; allowfullscreen=&#x22;true&#x22; onload=&#x22;window.top.scrollTo(0,0);&#x22;></iframe>" iframeHeight="500"}

:::

***

## M.2 port pinout

![Flipper One M.2 port pinout](/files/pics/m2-port-pinout.jpg)

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
      <p>—</p>
    </td>
    <td align="center">
      <p><strong>—</strong></p>
    </td>
    <td align="center">
      <p><strong>1</strong></p>
    </td>
    <td align="center">
      <p>CONFIG_3</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>3.3V</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>2</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>3</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GND</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>3.3V</p>
    </td>
    <td align="center">
      <p><strong>4</strong></p>
    </td>
    <td align="center">
      <p><strong>5</strong></p>
    </td>
    <td align="center">
      <p>GND</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>FULL_CARD_POWER_OFF# (O)(0/1.8V or 3.3V)</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>6</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>7</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>USB_D+</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>W_DISABLE1# (O)(0/1.8V/3.3V)</p>
    </td>
    <td align="center">
      <p><strong>8</strong></p>
    </td>
    <td align="center">
      <p><strong>9</strong></p>
    </td>
    <td align="center">
      <p>USB_D-</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GPIO_9/DAS/DSS (I/O)/LED_1# (I)(0/3.3V)</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>10</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>11</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GND</p>
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
      <p>GPIO_5 (I/O)(0/1.8V)</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>20</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>21</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>CONFIG_0</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>GPIO_6 (I/O)(0/1.8V)</p>
    </td>
    <td align="center">
      <p><strong>22</strong></p>
    </td>
    <td align="center">
      <p><strong>23</strong></p>
    </td>
    <td align="center">
      <p>GPIO_11 (I/O)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GPIO_7 (I/O)(0/1.8V)</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>24</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>25</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>DPR (O)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>GPIO_10 (I/O)(0/1.8V)</p>
    </td>
    <td align="center">
      <p><strong>26</strong></p>
    </td>
    <td align="center">
      <p><strong>27</strong></p>
    </td>
    <td align="center">
      <p>GND</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>PLA_S2# (I)/GPIO_8 (I/O)(0/1.8V)</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>28</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>29</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>PERn1/USB3.1-Rx-/SSIC-RxN</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>UIM_RESET (I)</p>
    </td>
    <td align="center">
      <p><strong>30</strong></p>
    </td>
    <td align="center">
      <p><strong>31</strong></p>
    </td>
    <td align="center">
      <p>PERp1/USB3.1-Rx+/SSIC-RxP</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>UIM_CLK (I)</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>32</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>33</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GND</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>UIM_DATA (I/O)</p>
    </td>
    <td align="center">
      <p><strong>34</strong></p>
    </td>
    <td align="center">
      <p><strong>35</strong></p>
    </td>
    <td align="center">
      <p>PETn1/USB3.1-Tx-/SSIC-TxN</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>UIM_PWR (I)</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>36</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>37</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>PETp1/USB3.1-Tx+/SSIC-TxP</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>DEVSLP (O)</p>
    </td>
    <td align="center">
      <p><strong>38</strong></p>
    </td>
    <td align="center">
      <p><strong>39</strong></p>
    </td>
    <td align="center">
      <p>GND</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GPIO_0 (I/O)/SMB_CLK (I/O)/(0/1.8V)</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>40</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>41</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>PERn0/SATA-B+</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>GPIO_1 (I/O)/SMB_DATA (I/O)/(0/1.8V)</p>
    </td>
    <td align="center">
      <p><strong>42</strong></p>
    </td>
    <td align="center">
      <p><strong>43</strong></p>
    </td>
    <td align="center">
      <p>PERp0/SATA-B-</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GPIO_2 (I/O)/ALERT# (I)(0/1.8V)</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>44</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>45</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GND</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>GPIO_3 (I/O)(0/1.8V)</p>
    </td>
    <td align="center">
      <p><strong>46</strong></p>
    </td>
    <td align="center">
      <p><strong>47</strong></p>
    </td>
    <td align="center">
      <p>PETn0/SATA-A-</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GPIO_4 (I/O)(0/1.8V)</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>48</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>49</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>PETp0/SATA-A+</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>PERST# (O)(0/1.8V/3.3V)</p>
    </td>
    <td align="center">
      <p><strong>50</strong></p>
    </td>
    <td align="center">
      <p><strong>51</strong></p>
    </td>
    <td align="center">
      <p>GND</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>CLKREQ# (I/O)(0/1.8V/3.3V)</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>52</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>53</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>REFCLKn</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>PEWAKE# (I/O)(0/1.8V/3.3V)</p>
    </td>
    <td align="center">
      <p><strong>54</strong></p>
    </td>
    <td align="center">
      <p><strong>55</strong></p>
    </td>
    <td align="center">
      <p>REFCLKp</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>NC</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>56</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>57</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>GND</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>NC</p>
    </td>
    <td align="center">
      <p><strong>58</strong></p>
    </td>
    <td align="center">
      <p><strong>59</strong></p>
    </td>
    <td align="center">
      <p>ANTCTL0 (I)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>COEX3 (I/O)(0/1.8V)</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>60</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>61</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>ANTCTL1 (I)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>COEX_TXD (O)(0/1.8V)</p>
    </td>
    <td align="center">
      <p><strong>62</strong></p>
    </td>
    <td align="center">
      <p><strong>63</strong></p>
    </td>
    <td align="center">
      <p>ANTCTL2 (I)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>COEX_RXD (I)(0/1.8V)</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>64</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>65</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>ANTCTL3 (I)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>SIM DETECT (O)</p>
    </td>
    <td align="center">
      <p><strong>66</strong></p>
    </td>
    <td align="center">
      <p><strong>67</strong></p>
    </td>
    <td align="center">
      <p>RESET# (O)(0/1.8V)</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>SUSCLK (O)(0/1.8V/3.3V)</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>68</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>69</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>CONFIG_1</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>3.3 V/VBAT</p>
    </td>
    <td align="center">
      <p><strong>70</strong></p>
    </td>
    <td align="center">
      <p><strong>71</strong></p>
    </td>
    <td align="center">
      <p>GND</p>
    </td>
  </tr>
  <tr>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>3.3 V/VBAT</p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>72</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p><strong>73</strong></p>
    </td>
    <td lightBackgroundColor="#f0f7ff" align="center">
      <p>VIO_CFG (I) or GND</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p>3.3 V/VBAT</p>
    </td>
    <td align="center">
      <p><strong>74</strong></p>
    </td>
    <td align="center">
      <p><strong>75</strong></p>
    </td>
    <td align="center">
      <p>CONFIG_2</p>
    </td>
  </tr>
</table>
