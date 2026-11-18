---
title: eSIM chip & SIM card slot
slug: hardware/esim
docTags: 
createdAt: Wed Nov 18 2026 11:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Wed Nov 18 2026 13:57:35 GMT+0000 (Coordinated Universal Time)
---

Flipper One features a built-in eSIM chip ([ST4SIM](https://www.st.com/content/st_com/en/ecosystems/st4sim-cellular-connectivity.html) series eSIM). The chip comes preloaded with the Flipper eSIM profile, and you can also add your own carrier profiles and switch between them. Flipper One also has a nano-SIM slot for a physical SIM card, which can also be used by the cellular modem.

In addition, the eSIM chip supports cryptographic functions that Flipper One can access via the I²C interface.

***

## SIM/eSIM switching

The cellular modem installed in the M.2 slot can use either the built-in eSIM chip or a physical SIM card inserted into the SIM slot. The corresponding [UICC (Universal Integrated Circuit Card)](https://en.wikipedia.org/wiki/Universal_integrated_circuit_card) interface pins on the M.2 connector are switched between the physical SIM card and the eSIM chip using a dual-SIM analog switch ([FSA2567MPX-TP](https://www.lcsc.com/product-detail/C52098294.html)). The switch is controlled by the RK3576 via the `SIM_SEL` signal.

The modem also requires a `SIM-DETECT` signal to detect SIM card insertion and removal events. This signal is routed through a separate analog switch ([TI SN74LVC1G3157](https://www.ti.com/product/SN74LVC1G3157)), which is controlled by the same `SIM_SEL` signal used to switch the UICC interface. This allows the modem to detect physical SIM card insertion and removal when the physical SIM is selected, while making it always detect a SIM card as present when the eSIM is selected.

:::Iframe{code="<iframe src=&#x22;https://personal-viewer.365.altium.com/client/index.html?feature=embed&source=27A3D823-6BD6-4B85-B602-1E9F06977056&activeView=SCH&#x22; width=&#x22;1280&#x22; height=&#x22;720&#x22; style=&#x22;overflow:hidden;border:none;width:100%;height:500px;&#x22; scrolling=&#x22;no&#x22; allowfullscreen=&#x22;true&#x22; onload=&#x22;window.top.scrollTo(0,0);&#x22;></iframe>" iframeHeight="500"}

:::

***

