---
title: Network
slug: testing/network
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:26:18 GMT+0000 (Coordinated Universal Time)
---

This section covers network connectivity testing and validation for Flipper One.

# Wi-Fi

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/Z4x-_n5NOQw2pOo6ClKGd_image.png "Wi-Fi + Bluetooth module WXT2AM2101. Based Mediatek MT7921AUN")

Built-in WiFi based on Mediatek MT7921AUN chip, Wi-Fi 6E (802.11ax) and Bluetooth 5.2 chipset primarily used in high-performance USB wireless adapters like the ALFA AWUS036AXML. It supports 2.4 GHz, 5 GHz, and 6 GHz bands.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/kCU7UPykJBA9NbkYWlK_L_image.png "Built-in WiFi module should work as AP and STA simultaneously")

### Access point mode

Classic Wi-Fi access point mode used in Wi-Fi routers. *Can we use different bands independently? For example configure 5GHz as AP and 2.4GHz as STA?❓&#x20;*

1. Configure Access Point on each band (2,4 GHz, 5 GHz, 6 GHz)
2. Measure speed with `iperf3` on each band
3. Repeat with different WPA/Open settings

### Client (station) mode

Client (STA) mode, where device connects to Wi-Fi access point. Usally laptops and smartphones are Wi-Fi clients. We need to test simultanious work AP and STA modes on different and same bands

1. Connect to Wi-Fi access point as client&#x20;
2. Mease speed with `iperf3`&#x20;
3. Repeat test on all bands (2,4 GHz, 5 GHz, 6 GHz)
4. Test simultanious work with AP mode

### Monitor mode

Monitor (promiscuous) mode can capture all data on specific channel

1. Switch Wi-Fi card to monitor mode
2. Dump traffic on each bands
3. Try to decode traffic&#x20;

### PMKID Sniff

Perform RSN PMKID sniff from real access point.

# Bluetooth

Our Bleutooth and Bluetooth Low Energy are integrated in Wi-Fi chip.&#x20;

### Bluetooth Speaker (master)&#x20;

Play sound from Flipper One on Bluetooth speaker

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/yCQaODeRXlS4m9UVpeemI_image.png)

1. Connect Bluetooth speaker to Flipper One&#x20;
2. Play sound

### Bluetooth Speaker (slave)&#x20;

Flipper One as Bluetooth speaker.&#x20;

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/ft9D5L7tfQ-pPv4W2PA6Q_image.png "Flipper One as Bluetooth Speaker")

1. Start advertising as Bluetooth speak from Flipper One (using bluez?)
2. Connect Flipper One as Bluetooth speak to smartphone
3. Play music on smartphone, listen on Flipper One via internal speaker, 3,5 Audio, HDMI Out
