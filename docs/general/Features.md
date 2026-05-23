---
title: Features
slug: general/features
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Sat May 23 2026 17:45:00 GMT+0000 (Coordinated Universal Time)
---

This page covers high-level product features expressed as user stories. Each feature describes a practical benefit for the user and a real use case.

***

## Network

Features related to IP networking, internet access, sharing, and filtering.

### Classic Wi-Fi router

![Classic Wi-Fi router](/files/pics/feature-classic-wifi-router.png)

A basic Wi-Fi router with NAT and a built-in DHCP server.
Eth0 is used as the WAN port. The remaining interfaces act as LAN interfaces: Wi-Fi access point, Eth1, and USB Ethernet adapters.

:::hint{type="info"}
**User story**

I have an Ethernet cable with internet access and need to share it via Wi-Fi and a second Ethernet port. I want to replace my old, slow Wi-Fi access point with Flipper One and use fast Wi-Fi 6 to distribute my wired internet connection.

Optionally, I want to add traffic filtering, bandwidth shaping, ad blocking, or basic security monitoring.
:::

***

### Multi-PHY Wi-Fi (concurrent STA + AP)

![Multi-PHY Wi-Fi (concurrent STA + AP)](/files/pics/feature-multi-phy-wifi.png)

A single Wi-Fi chipset can operate simultaneously in client (STA) and access point (AP) modes. Ideally, each frequency band (e.g., 2.4 GHz and 5 GHz) works as an independent interface, allowing concurrent uplink and downlink over different PHYs.

:::hint{type="info"}
**User story**

I have paid Wi-Fi access that is limited to a single device (one MAC address), but I want to share the connection with my family. I connect Flipper One to the paid Wi-Fi network as a client on one band (for example, 2.4 GHz) and re-share the internet over another band (for example, 5 GHz) as a local access point.

To pass the captive portal authorization, I connect my phone to Flipper One’s 5 GHz access point and complete the login flow. After that, all devices connected to Flipper One get internet access through the same uplink.
:::

***

### USB Wi-Fi / Ethernet adapter

![USB Wi-Fi / Ethernet adapter](/files/pics/feature-usb-wifi-ethernet-adapter.png)

Flipper One can act as a USB network adapter by bridging either Wi-Fi (STA mode) or Eth0 to a USB Ethernet interface, with MAC address proxying. NAT is disabled in this mode. Wi-Fi STA proxying has limitations because Wi-Fi access points allow only a single client MAC address per connection. For this reason, the user must explicitly select this mode before connecting Flipper One to a Wi-Fi access point as a client.

:::hint{type="info"}
**User story**

My PC has no built-in Wi-Fi or Ethernet interface. I want to use Flipper One as a USB network adapter. I want to transparently bridge all Layer-2 traffic to my PC, so that the upstream router sees my PC as a single device with a single MAC address. This gives me full access to the local network, including LAN devices, printers, mDNS/Bonjour services, and other local discovery protocols.
:::

***

### VPN gateway (leak-proof mode)

![VPN gateway (leak-proof mode)](/files/pics/feature-vpn-gateway_v1.png)

A router mode that tunnels all routed traffic through a VPN, preventing any direct internet access and eliminating traffic leaks. This includes protection against common leakage paths such as DNS and IPv6 traffic.

Flipper One supports popular VPN protocols, including WireGuard, IKEv2, and OpenVPN. Common VPN providers can be configured with one-click profiles for fast setup.

:::hint{type="info"}
**User story**

There is no simple way to guarantee that all traffic from my phone or PC always goes through a VPN. Modern operating systems may leak traffic outside the tunnel (for example, DNS requests or IPv6 routes).

I want a dedicated device that guarantees all internet traffic is forced through a VPN tunnel. When I’m traveling or using untrusted networks, I connect my laptop or phone to Flipper One and let it handle the VPN connection. From the device’s point of view, the network is already “secure,” and it never has to manage VPN configuration itself.
:::

***

### Ethernet MitM sniffer

![Ethernet MitM sniffer](/files/pics/feature-ethernet-mitm-sniffer.png)

Flipper One can be placed inline between two Ethernet devices and operate as a fully transparent bridge. Both Eth0 and Eth1 ports form a pass-through link that is invisible to the monitored devices. The MAC addresses of Flipper One’s Ethernet interfaces are never exposed to the observed traffic.

This mode allows passive inspection and capture of network traffic without modifying the existing network topology or breaking the target device’s connectivity.

:::hint{type="info"}
**User story**

I have an Ethernet device such as an IP camera or a VoIP phone, and I want to analyze and capture its network traffic to understand how it works: which IP addresses it connects to and which DNS names it resolves. I don’t want to disrupt the existing setup or make my own MAC address visible on the network.

To do this, I place Flipper One inline between the device and the wired network and enable transparent sniffing mode. I can view a compact, real-time traffic log on the built-in display (similar to tcpdump -q), save full packet captures as PCAP files to internal storage, or mirror traffic over USB Ethernet to a PC for live analysis in Wireshark or tcpdump.
:::

***

### LAN discovery (passive & active)

![LAN discovery (passive & active)](/files/pics/feature-lan-discovery.png)

An application that gradually enables network layers from L2 to L3 while simultaneously sniffing traffic in promiscuous mode. Both Passive and Active modes are available.

In Passive mode, Flipper One only listens and observes existing traffic. In Active mode, it can query the network (for example: request an address, probe services, or enumerate basic network configuration). Users see a list of observed networks and can proceed with the selected one.

:::hint{type="info"}
**User story**

I have access to an unknown LAN and want to understand what’s happening inside it. I want to learn the network configuration (IPv4 DHCP / IPv6), see which hosts are online by observing ARP traffic, and discover what services are present. I also want to know whether the Ethernet port uses VLANs and what IP settings I should configure to connect correctly.

First, I want a fully passive mode that does not generate traffic (for example, no DHCP requests) and only observes broadcasts like ARP and IPv6 neighbor discovery. Then I want to manually step forward, layer by layer, enabling active discovery when I decide it’s safe — such as requesting an IP address, checking VLAN tagging, and probing common services.
:::

***

### 5G cellular uplink

Flipper One can use an M.2 cellular modem to add mobile internet access. This gives the device an independent WAN uplink for router, VPN gateway, and bridge workflows when wired Ethernet or Wi-Fi uplink is unavailable.

Related docs: [M.2 modules](../hardware/M2-Modules.md), [Quectel RM530N-GL testing](../testing/RM530N-GL.md), [Fibocom FM350-GL testing](../testing/FM350-GL.md).

:::hint{type="info"}
**User story**

I am working from a field site, hotel, vehicle, or temporary network and need a trusted internet uplink that is not tied to local Wi-Fi. I install a supported cellular M.2 modem in Flipper One, connect my laptop or other devices through Flipper One, and use it as a portable 5G/LTE gateway with the same routing, VPN, and monitoring tools I use on wired networks.
:::

***

### Satellite NTN modem

Flipper One is planned to support M.2 NTN (Non-Terrestrial Network) modems for low-speed IP connectivity over satellite networks. NTN uses the regular cellular stack, including SIM/eSIM authentication and roaming, and is standardized by 3GPP as part of 5G and LTE specifications.

Related docs: [Satellite modem](../hardware/M2-satellite-modem.md) and [M.2 modules](../hardware/M2-Modules.md).

:::hint{type="info"}
**User story**

I am outside terrestrial cellular coverage and need a low-bandwidth data link for telemetry, status messages, or basic IP connectivity. I install a supported NTN M.2 module and use Flipper One to send small amounts of data through satellite infrastructure without relying on a phone network.
:::

***

### SDR radio platform

Flipper One can be extended with M.2 SDR radio modules, turning it into a portable platform for radio signal analysis, capture, and experimentation. SDR modules connect through the hardware expansion system and can use Flipper One's local compute and storage for signal-processing workflows.

Related docs: [M.2 modules](../hardware/M2-Modules.md).

:::hint{type="info"}
**User story**

I want a portable radio analysis setup that does not require carrying a laptop for every task. I install an SDR module, capture RF data to internal storage, and use Flipper One's Linux tools to inspect, process, or forward the signal data for deeper analysis.
:::

***

## Hardware expansion

Features related to external modules, GPIO, and custom hardware.

### GPIO modules

The GPIO expansion port exposes power rails, USB 2.0, and configurable MCU/CPU pins for protocols such as I²C, UART, SPI, CAN, PWM, I²S, SPDIF, ADC, and PIO. GPIO modules mount on top of the back plate and can be built around the documented connector and mechanical system.

Related docs: [GPIO port](../hardware/GPIO-port.md) and [GPIO modules](../hardware/GPIO-Modules.md).

:::hint{type="info"}
**User story**

I want to build a custom hardware add-on for Flipper One without designing a full internal M.2 module. I use the GPIO port and module mounting system to attach a small board, such as a walkie-talkie radio module or a camera module, and control it from the device's Linux or MCU-side software.
:::

***

## Compute and desktop

Features related to local compute, display output, and on-device assistance.

### Offline Flipper LLM

Flipper One is planned to support a small on-device assistant model for offline help. The goal is to help users operate the device, generate configuration snippets, and get useful tips even when there is no internet connection. The NPU is not yet supported in the mainline kernel, so this feature depends on future mainline NPU work.

:::hint{type="info"}
**User story**

I am configuring networking or device services in the field without internet access. I ask the local Flipper assistant for a short explanation or a configuration starting point, then review and apply the result myself.
:::

***

### Survival desktop

Flipper One can act as a portable Linux desktop or thin client. With USB-C DisplayPort Alt Mode, one cable can provide monitor output, charging, and USB peripherals when the connected monitor or dock supports it.

Desktop mode still has open engineering work, including DisplayPort Alt Mode stability, mainline kernel support, hardware video decoding, and choosing a desktop environment that fits the device.

Related docs: [Graphics testing](../testing/Graphics.md).

:::hint{type="info"}
**User story**

I need a small computer I can carry every day. I plug Flipper One into a USB-C monitor or dock, connect a keyboard and mouse, and use it for web browsing, light development, diagnostics, or emergency access to a Linux desktop.
:::

***

### Hacker's TV media box

Flipper One includes a full-size HDMI 2.1 port with CEC support. This makes it possible to use the device as a portable media box that connects directly to a TV and can be controlled from the TV's own remote through HDMI CEC.

Related docs: [Tech specs](Tech-Specs.md).

:::hint{type="info"}
**User story**

I am traveling and want a media setup I control instead of relying on a hotel or rental TV interface. I plug Flipper One into the TV with a normal full-size HDMI cable and use the TV remote to control the media interface through CEC.
:::
