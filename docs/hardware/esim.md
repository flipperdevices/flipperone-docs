---
title: eSIM & SIM card slot
slug: hardware/esim
docTags: 
createdAt: Wed Nov 18 2026 11:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Wed Nov 18 2026 13:57:35 GMT+0000 (Coordinated Universal Time)
---

Flipper One features a built-in eSIM chip (ST4SIM). The chip comes preloaded with the Flipper eSIM profile, and you can also add your own carrier profiles and switch between them. Flipper One also has a nano-SIM slot for a physical SIM card, which can also be used by the cellular modem.

In addition, the eSIM chip supports cryptographic functions that Flipper One can access via the I²C interface.

***

## SIM/eSIM switching

The cellular modem installed in the M.2 slot can use either the built-in eSIM chip or a physical SIM card inserted into the SIM slot. The corresponding UICC (Universal Integrated Circuit Card) interface pins on the M.2 connector are switched between the physical SIM card and the eSIM chip using a dual-SIM analog switch (FSA2567MPX-TP). The switch is controlled by the RK3576 via the SIM_SEL signal.

The modem also requires a `SIM-DETECT` signal to detect SIM card insertion and removal events. This signal is routed through a separate analog switch (SN74LVC1G3157DCKR), which is controlled by the same `SIM_SEL` signal used to switch the UICC interface.

***

