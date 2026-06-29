---
title: Wi-Fi
slug: testing/network/wifi
---

Built-in Wi-Fi based on the MediaTek MT7921AUN chip — a Wi-Fi 6E (802.11ax) and Bluetooth 5.2 combo, also used in high-performance USB wireless adapters like the ALFA AWUS036AXML. It supports the 2.4 GHz, 5 GHz, and 6 GHz bands.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/Z4x-_n5NOQw2pOo6ClKGd_image.png "Wi-Fi + Bluetooth module WXT2AM2101, based on the MediaTek MT7921AUN")

## Tests

- **[Access Point (AP)](./WiFi-Access-Point.md)** — single AP mode across all channels, bands, output power, and encryption modes.
- **[Client (STA)](./WiFi-Client-STA.md)** — station mode, connecting to an access point.
- **[AP+STA SCC](./WiFi-AP-STA-SCC.md)** — simultaneous client and hotspot on the same band and channel.
  - [✅ Test log: AP+STA same-channel (SCC)](./WiFi-AP-STA-SCC.md#test-log-apsta-same-channel-scc)
- **[DBDC](./WiFi-DBDC.md)** — dual-band dual-concurrent operation.
  - [❌ Test log: AP+STA dual-band](./WiFi-DBDC.md#test-log-apsta-dual-band)
  - [❌ Test log: AP+AP dual-band](./WiFi-DBDC.md#test-log-apap-dual-band)
- **[Monitor mode](./WiFi-Monitor.md)** — promiscuous capture and PMKID sniffing.
  - [✅ Test log: Monitor mode](./WiFi-Monitor.md#test-log-monitor-mode)

## MT7921AUN chipset info

###  Valid interface combinations

```console
$ iw phy phy0 info | sed -n '/valid interface combinations/,/HT Capability/p'

valid interface combinations:
 * #{ managed, P2P-client } <= 2, #{ P2P-GO } <= 1, #{ P2P-device } <= 1,
   total <= 3, #channels <= 2
 * #{ managed, P2P-client } <= 2, #{ AP } <= 1, #{ P2P-device } <= 1,
   total <= 3, #channels <= 1
HT Capability overrides:
```

:::::ExpandableHeading
### `ethtool -i wlxb06b11673ade`
```bash
$ ethtool -i wlxb06b11673ade
driver: mt7921u
version: 7.1.0-g7fd25013c28b
firmware-version: ____010000-20260224110949
expansion-rom-version:
bus-info: 2-1.1:1.3
supports-statistics: yes
supports-test: no
supports-eeprom-access: no
supports-register-dump: no
supports-priv-flags: no
```
:::::

:::::ExpandableHeading
### `iw phy phy0 info`

```bash
$ sudo iw phy phy0 info
Wiphy phy0
	wiphy index: 0
	max # scan SSIDs: 4
	max scan IEs length: 482 bytes
	max # sched scan SSIDs: 10
	max # match sets: 16
	Retry short limit: 7
	Retry long limit: 4
	Coverage class: 0 (up to 0m)
	Device supports AP-side u-APSD.
	Device supports T-DLS.
	Supported Ciphers:
		* WEP40 (00-0f-ac:1)
		* WEP104 (00-0f-ac:5)
		* TKIP (00-0f-ac:2)
		* CCMP-128 (00-0f-ac:4)
		* CCMP-256 (00-0f-ac:10)
		* GCMP-128 (00-0f-ac:8)
		* GCMP-256 (00-0f-ac:9)
		* CMAC (00-0f-ac:6)
		* CMAC-256 (00-0f-ac:13)
		* GMAC-128 (00-0f-ac:11)
		* GMAC-256 (00-0f-ac:12)
	Available Antennas: TX 0x3 RX 0x3
	Configured Antennas: TX 0x3 RX 0x3
	Supported interface modes:
		 * managed
		 * AP
		 * AP/VLAN
		 * monitor
		 * P2P-client
		 * P2P-GO
		 * P2P-device
	Band 1:
		Capabilities: 0x9ff
			RX LDPC
			HT20/HT40
			SM Power Save disabled
			RX Greenfield
			RX HT20 SGI
			RX HT40 SGI
			TX STBC
			RX STBC 1-stream
			Max AMSDU length: 7935 bytes
			No DSSS/CCK HT40
		Maximum RX AMPDU length 65535 bytes (exponent: 0x003)
		Minimum RX AMPDU time spacing: No restriction (0x00)
		HT TX/RX MCS rate indexes supported: 0-15
		HE Iftypes: managed
			HE MAC Capabilities (0x08011a000040):
				+HTC HE Supported
				Trigger Frame MAC Padding Duration: 2
				OM Control
				Maximum A-MPDU Length Exponent: 3
				A-MSDU in A-MPDU
			HE PHY Capabilities: (0x2270ce120dc0b306423f00):
				HE40/2.4GHz
				242 tone RUs/2.4GHz
				Device Class: 1
				LDPC Coding in Payload
				HE SU PPDU with 1x HE-LTF and 0.8us GI
				NDP with 4x HE-LTF and 3.2us GI
				STBC Tx <= 80MHz
				STBC Rx <= 80MHz
				Full Bandwidth UL MU-MIMO
				Partial Bandwidth UL MU-MIMO
				DCM Max Constellation: 2
				DCM Max Constellation Rx: 2
				SU Beamformee
				Beamformee STS <= 80Mhz: 3
				Ng = 16 SU Feedback
				Ng = 16 MU Feedback
				Codebook Size SU Feedback
				Codebook Size MU Feedback
				Triggered CQI Feedback
				Partial Bandwidth Extended Range
				PPE Threshold Present
				Power Boost Factor ar
				HE SU PPDU & HE PPDU 4x HE-LTF 0.8us GI
				20MHz in 40MHz HE PPDU 2.4GHz
				DCM Max BW: 1
				Longer Than 16HE SIG-B OFDM Symbols
				Non-Triggered CQI Feedback
				TX 1024-QAM
				RX 1024-QAM
				RX Full BW SU Using HE MU PPDU with Compression SIGB
				RX Full BW SU Using HE MU PPDU with Non-Compression SIGB
			HE RX MCS and NSS set <= 80 MHz
				1 streams: MCS 0-11
				2 streams: MCS 0-11
				3 streams: not supported
				4 streams: not supported
				5 streams: not supported
				6 streams: not supported
				7 streams: not supported
				8 streams: not supported
			HE TX MCS and NSS set <= 80 MHz
				1 streams: MCS 0-11
				2 streams: MCS 0-11
				3 streams: not supported
				4 streams: not supported
				5 streams: not supported
				6 streams: not supported
				7 streams: not supported
				8 streams: not supported
			PPE Threshold 0x19 0x1c 0xc7 0x71
		HE Iftypes: AP
			HE MAC Capabilities (0x00011a081044):
				+HTC HE Supported
				BSR
				OM Control
				Maximum A-MPDU Length Exponent: 3
				BQR
				A-MSDU in A-MPDU
				OM Control UL MU Data Disable RX
			HE PHY Capabilities: (0x0220ce120000a000000c00):
				HE40/2.4GHz
				LDPC Coding in Payload
				NDP with 4x HE-LTF and 3.2us GI
				STBC Tx <= 80MHz
				STBC Rx <= 80MHz
				Full Bandwidth UL MU-MIMO
				Partial Bandwidth UL MU-MIMO
				DCM Max Constellation: 2
				DCM Max Constellation Rx: 2
				Partial Bandwidth Extended Range
				PPE Threshold Present
				TX 1024-QAM
				RX 1024-QAM
			HE RX MCS and NSS set <= 80 MHz
				1 streams: MCS 0-11
				2 streams: MCS 0-11
				3 streams: not supported
				4 streams: not supported
				5 streams: not supported
				6 streams: not supported
				7 streams: not supported
				8 streams: not supported
			HE TX MCS and NSS set <= 80 MHz
				1 streams: MCS 0-11
				2 streams: MCS 0-11
				3 streams: not supported
				4 streams: not supported
				5 streams: not supported
				6 streams: not supported
				7 streams: not supported
				8 streams: not supported
			PPE Threshold 0x19 0x1c 0xc7 0x71
		Bitrates (non-HT):
			* 1.0 Mbps (short preamble supported)
			* 2.0 Mbps (short preamble supported)
			* 5.5 Mbps (short preamble supported)
			* 11.0 Mbps (short preamble supported)
			* 6.0 Mbps
			* 9.0 Mbps
			* 12.0 Mbps
			* 18.0 Mbps
			* 24.0 Mbps
			* 36.0 Mbps
			* 48.0 Mbps
			* 54.0 Mbps
		Frequencies:
			* 2412.0 MHz [1] (20.0 dBm)
			* 2417.0 MHz [2] (20.0 dBm)
			* 2422.0 MHz [3] (20.0 dBm)
			* 2427.0 MHz [4] (20.0 dBm)
			* 2432.0 MHz [5] (20.0 dBm)
			* 2437.0 MHz [6] (20.0 dBm)
			* 2442.0 MHz [7] (20.0 dBm)
			* 2447.0 MHz [8] (20.0 dBm)
			* 2452.0 MHz [9] (20.0 dBm)
			* 2457.0 MHz [10] (20.0 dBm)
			* 2462.0 MHz [11] (20.0 dBm)
			* 2467.0 MHz [12] (20.0 dBm) (no IR)
			* 2472.0 MHz [13] (20.0 dBm) (no IR)
			* 2484.0 MHz [14] (20.0 dBm) (no IR)
	Band 2:
		Capabilities: 0x9ff
			RX LDPC
			HT20/HT40
			SM Power Save disabled
			RX Greenfield
			RX HT20 SGI
			RX HT40 SGI
			TX STBC
			RX STBC 1-stream
			Max AMSDU length: 7935 bytes
			No DSSS/CCK HT40
		Maximum RX AMPDU length 65535 bytes (exponent: 0x003)
		Minimum RX AMPDU time spacing: No restriction (0x00)
		HT TX/RX MCS rate indexes supported: 0-15
		VHT Capabilities (0x339071b2):
			Max MPDU length: 11454
			Supported Channel Width: neither 160 nor 80+80
			RX LDPC
			short GI (80 MHz)
			TX STBC
			SU Beamformee
			MU Beamformee
			RX antenna pattern consistency
			TX antenna pattern consistency
		VHT RX MCS set:
			1 streams: MCS 0-9
			2 streams: MCS 0-9
			3 streams: not supported
			4 streams: not supported
			5 streams: not supported
			6 streams: not supported
			7 streams: not supported
			8 streams: not supported
		VHT RX highest supported: 0 Mbps
		VHT TX MCS set:
			1 streams: MCS 0-9
			2 streams: MCS 0-9
			3 streams: not supported
			4 streams: not supported
			5 streams: not supported
			6 streams: not supported
			7 streams: not supported
			8 streams: not supported
		VHT TX highest supported: 0 Mbps
		VHT extended NSS: supported
		HE Iftypes: managed
			HE MAC Capabilities (0x08011a000040):
				+HTC HE Supported
				Trigger Frame MAC Padding Duration: 2
				OM Control
				Maximum A-MPDU Length Exponent: 3
				A-MSDU in A-MPDU
			HE PHY Capabilities: (0x4470ce120dc0b306423f00):
				HE40/HE80/5GHz
				242 tone RUs/5GHz
				Device Class: 1
				LDPC Coding in Payload
				HE SU PPDU with 1x HE-LTF and 0.8us GI
				NDP with 4x HE-LTF and 3.2us GI
				STBC Tx <= 80MHz
				STBC Rx <= 80MHz
				Full Bandwidth UL MU-MIMO
				Partial Bandwidth UL MU-MIMO
				DCM Max Constellation: 2
				DCM Max Constellation Rx: 2
				SU Beamformee
				Beamformee STS <= 80Mhz: 3
				Ng = 16 SU Feedback
				Ng = 16 MU Feedback
				Codebook Size SU Feedback
				Codebook Size MU Feedback
				Triggered CQI Feedback
				Partial Bandwidth Extended Range
				PPE Threshold Present
				Power Boost Factor ar
				HE SU PPDU & HE PPDU 4x HE-LTF 0.8us GI
				20MHz in 40MHz HE PPDU 2.4GHz
				DCM Max BW: 1
				Longer Than 16HE SIG-B OFDM Symbols
				Non-Triggered CQI Feedback
				TX 1024-QAM
				RX 1024-QAM
				RX Full BW SU Using HE MU PPDU with Compression SIGB
				RX Full BW SU Using HE MU PPDU with Non-Compression SIGB
			HE RX MCS and NSS set <= 80 MHz
				1 streams: MCS 0-11
				2 streams: MCS 0-11
				3 streams: not supported
				4 streams: not supported
				5 streams: not supported
				6 streams: not supported
				7 streams: not supported
				8 streams: not supported
			HE TX MCS and NSS set <= 80 MHz
				1 streams: MCS 0-11
				2 streams: MCS 0-11
				3 streams: not supported
				4 streams: not supported
				5 streams: not supported
				6 streams: not supported
				7 streams: not supported
				8 streams: not supported
			PPE Threshold 0x79 0x1c 0xc7 0x71 0x1c 0xc7 0x71
		HE Iftypes: AP
			HE MAC Capabilities (0x00011a081044):
				+HTC HE Supported
				BSR
				OM Control
				Maximum A-MPDU Length Exponent: 3
				BQR
				A-MSDU in A-MPDU
				OM Control UL MU Data Disable RX
			HE PHY Capabilities: (0x0420ce120000a000000c00):
				HE40/HE80/5GHz
				LDPC Coding in Payload
				NDP with 4x HE-LTF and 3.2us GI
				STBC Tx <= 80MHz
				STBC Rx <= 80MHz
				Full Bandwidth UL MU-MIMO
				Partial Bandwidth UL MU-MIMO
				DCM Max Constellation: 2
				DCM Max Constellation Rx: 2
				Partial Bandwidth Extended Range
				PPE Threshold Present
				TX 1024-QAM
				RX 1024-QAM
			HE RX MCS and NSS set <= 80 MHz
				1 streams: MCS 0-11
				2 streams: MCS 0-11
				3 streams: not supported
				4 streams: not supported
				5 streams: not supported
				6 streams: not supported
				7 streams: not supported
				8 streams: not supported
			HE TX MCS and NSS set <= 80 MHz
				1 streams: MCS 0-11
				2 streams: MCS 0-11
				3 streams: not supported
				4 streams: not supported
				5 streams: not supported
				6 streams: not supported
				7 streams: not supported
				8 streams: not supported
			PPE Threshold 0x79 0x1c 0xc7 0x71 0x1c 0xc7 0x71
		Bitrates (non-HT):
			* 6.0 Mbps
			* 9.0 Mbps
			* 12.0 Mbps
			* 18.0 Mbps
			* 24.0 Mbps
			* 36.0 Mbps
			* 48.0 Mbps
			* 54.0 Mbps
		Frequencies:
			* 5180.0 MHz [36] (20.0 dBm) (no IR)
			* 5200.0 MHz [40] (20.0 dBm)
			* 5220.0 MHz [44] (20.0 dBm) (no IR)
			* 5240.0 MHz [48] (20.0 dBm)
			* 5260.0 MHz [52] (20.0 dBm) (no IR, radar detection)
			* 5280.0 MHz [56] (20.0 dBm) (no IR, radar detection)
			* 5300.0 MHz [60] (20.0 dBm) (no IR, radar detection)
			* 5320.0 MHz [64] (20.0 dBm) (no IR, radar detection)
			* 5500.0 MHz [100] (20.0 dBm) (no IR, radar detection)
			* 5520.0 MHz [104] (20.0 dBm) (no IR, radar detection)
			* 5540.0 MHz [108] (20.0 dBm) (no IR, radar detection)
			* 5560.0 MHz [112] (20.0 dBm) (no IR, radar detection)
			* 5580.0 MHz [116] (20.0 dBm) (no IR, radar detection)
			* 5600.0 MHz [120] (20.0 dBm) (no IR, radar detection)
			* 5620.0 MHz [124] (20.0 dBm) (no IR, radar detection)
			* 5640.0 MHz [128] (20.0 dBm) (no IR, radar detection)
			* 5660.0 MHz [132] (20.0 dBm) (no IR, radar detection)
			* 5680.0 MHz [136] (20.0 dBm) (no IR, radar detection)
			* 5700.0 MHz [140] (20.0 dBm) (no IR, radar detection)
			* 5720.0 MHz [144] (20.0 dBm) (no IR, radar detection)
			* 5745.0 MHz [149] (20.0 dBm) (no IR)
			* 5765.0 MHz [153] (20.0 dBm)
			* 5785.0 MHz [157] (20.0 dBm) (no IR)
			* 5805.0 MHz [161] (20.0 dBm) (no IR)
			* 5825.0 MHz [165] (20.0 dBm) (no IR)
			* 5845.0 MHz [169] (disabled)
			* 5865.0 MHz [173] (disabled)
			* 5885.0 MHz [177] (disabled)
	Band 4:
		HE Iftypes: managed
			HE MAC Capabilities (0x08011a000040):
				+HTC HE Supported
				Trigger Frame MAC Padding Duration: 2
				OM Control
				Maximum A-MPDU Length Exponent: 3
				A-MSDU in A-MPDU
			HE PHY Capabilities: (0x4470ce120dc0b306423f00):
				HE40/HE80/5GHz
				242 tone RUs/5GHz
				Device Class: 1
				LDPC Coding in Payload
				HE SU PPDU with 1x HE-LTF and 0.8us GI
				NDP with 4x HE-LTF and 3.2us GI
				STBC Tx <= 80MHz
				STBC Rx <= 80MHz
				Full Bandwidth UL MU-MIMO
				Partial Bandwidth UL MU-MIMO
				DCM Max Constellation: 2
				DCM Max Constellation Rx: 2
				SU Beamformee
				Beamformee STS <= 80Mhz: 3
				Ng = 16 SU Feedback
				Ng = 16 MU Feedback
				Codebook Size SU Feedback
				Codebook Size MU Feedback
				Triggered CQI Feedback
				Partial Bandwidth Extended Range
				PPE Threshold Present
				Power Boost Factor ar
				HE SU PPDU & HE PPDU 4x HE-LTF 0.8us GI
				20MHz in 40MHz HE PPDU 2.4GHz
				DCM Max BW: 1
				Longer Than 16HE SIG-B OFDM Symbols
				Non-Triggered CQI Feedback
				TX 1024-QAM
				RX 1024-QAM
				RX Full BW SU Using HE MU PPDU with Compression SIGB
				RX Full BW SU Using HE MU PPDU with Non-Compression SIGB
			HE RX MCS and NSS set <= 80 MHz
				1 streams: MCS 0-11
				2 streams: MCS 0-11
				3 streams: not supported
				4 streams: not supported
				5 streams: not supported
				6 streams: not supported
				7 streams: not supported
				8 streams: not supported
			HE TX MCS and NSS set <= 80 MHz
				1 streams: MCS 0-11
				2 streams: MCS 0-11
				3 streams: not supported
				4 streams: not supported
				5 streams: not supported
				6 streams: not supported
				7 streams: not supported
				8 streams: not supported
			PPE Threshold 0x79 0x1c 0xc7 0x71 0x1c 0xc7 0x71
		HE Iftypes: AP
			HE MAC Capabilities (0x00011a081044):
				+HTC HE Supported
				BSR
				OM Control
				Maximum A-MPDU Length Exponent: 3
				BQR
				A-MSDU in A-MPDU
				OM Control UL MU Data Disable RX
			HE PHY Capabilities: (0x0420ce120000a000000c00):
				HE40/HE80/5GHz
				LDPC Coding in Payload
				NDP with 4x HE-LTF and 3.2us GI
				STBC Tx <= 80MHz
				STBC Rx <= 80MHz
				Full Bandwidth UL MU-MIMO
				Partial Bandwidth UL MU-MIMO
				DCM Max Constellation: 2
				DCM Max Constellation Rx: 2
				Partial Bandwidth Extended Range
				PPE Threshold Present
				TX 1024-QAM
				RX 1024-QAM
			HE RX MCS and NSS set <= 80 MHz
				1 streams: MCS 0-11
				2 streams: MCS 0-11
				3 streams: not supported
				4 streams: not supported
				5 streams: not supported
				6 streams: not supported
				7 streams: not supported
				8 streams: not supported
			HE TX MCS and NSS set <= 80 MHz
				1 streams: MCS 0-11
				2 streams: MCS 0-11
				3 streams: not supported
				4 streams: not supported
				5 streams: not supported
				6 streams: not supported
				7 streams: not supported
				8 streams: not supported
			PPE Threshold 0x79 0x1c 0xc7 0x71 0x1c 0xc7 0x71
		Bitrates (non-HT):
			* 6.0 Mbps
			* 9.0 Mbps
			* 12.0 Mbps
			* 18.0 Mbps
			* 24.0 Mbps
			* 36.0 Mbps
			* 48.0 Mbps
			* 54.0 Mbps
		Frequencies:
			* 5955.0 MHz [1] (disabled)
			* 5975.0 MHz [5] (disabled)
			* 5995.0 MHz [9] (disabled)
			* 6015.0 MHz [13] (disabled)
			* 6035.0 MHz [17] (disabled)
			* 6055.0 MHz [21] (disabled)
			* 6075.0 MHz [25] (disabled)
			* 6095.0 MHz [29] (disabled)
			* 6115.0 MHz [33] (disabled)
			* 6135.0 MHz [37] (disabled)
			* 6155.0 MHz [41] (disabled)
			* 6175.0 MHz [45] (disabled)
			* 6195.0 MHz [49] (disabled)
			* 6215.0 MHz [53] (disabled)
			* 6235.0 MHz [57] (disabled)
			* 6255.0 MHz [61] (disabled)
			* 6275.0 MHz [65] (disabled)
			* 6295.0 MHz [69] (disabled)
			* 6315.0 MHz [73] (disabled)
			* 6335.0 MHz [77] (disabled)
			* 6355.0 MHz [81] (disabled)
			* 6375.0 MHz [85] (disabled)
			* 6395.0 MHz [89] (disabled)
			* 6415.0 MHz [93] (disabled)
			* 6435.0 MHz [97] (disabled)
			* 6455.0 MHz [101] (disabled)
			* 6475.0 MHz [105] (disabled)
			* 6495.0 MHz [109] (disabled)
			* 6515.0 MHz [113] (disabled)
			* 6535.0 MHz [117] (disabled)
			* 6555.0 MHz [121] (disabled)
			* 6575.0 MHz [125] (disabled)
			* 6595.0 MHz [129] (disabled)
			* 6615.0 MHz [133] (disabled)
			* 6635.0 MHz [137] (disabled)
			* 6655.0 MHz [141] (disabled)
			* 6675.0 MHz [145] (disabled)
			* 6695.0 MHz [149] (disabled)
			* 6715.0 MHz [153] (disabled)
			* 6735.0 MHz [157] (disabled)
			* 6755.0 MHz [161] (disabled)
			* 6775.0 MHz [165] (disabled)
			* 6795.0 MHz [169] (disabled)
			* 6815.0 MHz [173] (disabled)
			* 6835.0 MHz [177] (disabled)
			* 6855.0 MHz [181] (disabled)
			* 6875.0 MHz [185] (disabled)
			* 6895.0 MHz [189] (disabled)
			* 6915.0 MHz [193] (disabled)
			* 6935.0 MHz [197] (disabled)
			* 6955.0 MHz [201] (disabled)
			* 6975.0 MHz [205] (disabled)
			* 6995.0 MHz [209] (disabled)
			* 7015.0 MHz [213] (disabled)
			* 7035.0 MHz [217] (disabled)
			* 7055.0 MHz [221] (disabled)
			* 7075.0 MHz [225] (disabled)
			* 7095.0 MHz [229] (disabled)
			* 7115.0 MHz [233] (disabled)
	Supported commands:
		 * new_interface
		 * set_interface
		 * new_key
		 * start_ap
		 * new_station
		 * set_bss
		 * authenticate
		 * associate
		 * deauthenticate
		 * disassociate
		 * join_ibss
		 * remain_on_channel
		 * set_tx_bitrate_mask
		 * frame
		 * frame_wait_cancel
		 * set_wiphy_netns
		 * set_channel
		 * tdls_mgmt
		 * tdls_oper
		 * start_sched_scan
		 * probe_client
		 * set_noack_map
		 * register_beacons
		 * start_p2p_device
		 * set_mcast_rate
		 * connect
		 * disconnect
		 * channel_switch
		 * set_qos_map
		 * set_multicast_to_unicast
		 * set_sar_specs
		 * Unknown command (156)
	WoWLAN support:
		 * wake up on disconnect
		 * wake up on magic packet
		 * wake up on pattern match, up to 1 patterns of 1-128 bytes,
		   maximum packet offset 0 bytes
		 * can do GTK rekeying
		 * wake up on network detection, up to 10 match sets
	software interface modes (can always be added):
		 * AP/VLAN
		 * monitor
	valid interface combinations:
		 * #{ managed, P2P-client } <= 2, #{ P2P-GO } <= 1, #{ P2P-device } <= 1,
		   total <= 3, #channels <= 2
		 * #{ managed, P2P-client } <= 2, #{ AP } <= 1, #{ P2P-device } <= 1,
		   total <= 3, #channels <= 1
	HT Capability overrides:
		 * MCS: ff ff ff ff ff ff ff ff ff ff
		 * maximum A-MSDU length
		 * supported channel width
		 * short GI for 40 MHz
		 * max A-MPDU length exponent
		 * min MPDU start spacing
	Device supports TX status socket option.
	Device supports HT-IBSS.
	Device supports SAE with AUTHENTICATE command
	Device supports scan flush.
	Device supports per-vif TX power setting
	P2P GO supports CT window setting
	P2P GO supports opportunistic powersave setting
	Driver supports full state transitions for AP/GO clients
	Driver supports a userspace MPM
	Device supports active monitor (which will ACK incoming frames)
	Driver/device bandwidth changes during BSS lifetime (AP/GO mode)
	Device supports configuring vdev MAC-addr on create.
	Device supports randomizing MAC-addr in scans.
	Device supports randomizing MAC-addr in sched scans.
	max # scan plans: 1
	max scan plan interval: 65535
	max scan plan iterations: 0
	Supported TX frame types:
		 * IBSS: 0x00 0x10 0x20 0x30 0x40 0x50 0x60 0x70 0x80 0x90 0xa0 0xb0 0xc0 0xd0 0xe0 0xf0
		 * managed: 0x00 0x10 0x20 0x30 0x40 0x50 0x60 0x70 0x80 0x90 0xa0 0xb0 0xc0 0xd0 0xe0 0xf0
		 * AP: 0x00 0x10 0x20 0x30 0x40 0x50 0x60 0x70 0x80 0x90 0xa0 0xb0 0xc0 0xd0 0xe0 0xf0
		 * AP/VLAN: 0x00 0x10 0x20 0x30 0x40 0x50 0x60 0x70 0x80 0x90 0xa0 0xb0 0xc0 0xd0 0xe0 0xf0
		 * mesh point: 0x00 0x10 0x20 0x30 0x40 0x50 0x60 0x70 0x80 0x90 0xa0 0xb0 0xc0 0xd0 0xe0 0xf0
		 * P2P-client: 0x00 0x10 0x20 0x30 0x40 0x50 0x60 0x70 0x80 0x90 0xa0 0xb0 0xc0 0xd0 0xe0 0xf0
		 * P2P-GO: 0x00 0x10 0x20 0x30 0x40 0x50 0x60 0x70 0x80 0x90 0xa0 0xb0 0xc0 0xd0 0xe0 0xf0
		 * P2P-device: 0x00 0x10 0x20 0x30 0x40 0x50 0x60 0x70 0x80 0x90 0xa0 0xb0 0xc0 0xd0 0xe0 0xf0
		 * NAN: 0x00 0x10 0x20 0x30 0x40 0x50 0x60 0x70 0x80 0x90 0xa0 0xb0 0xc0 0xd0 0xe0 0xf0
	Supported RX frame types:
		 * IBSS: 0x40 0xb0 0xc0 0xd0
		 * managed: 0x40 0xb0 0xd0
		 * AP: 0x00 0x20 0x40 0xa0 0xb0 0xc0 0xd0
		 * AP/VLAN: 0x00 0x20 0x40 0xa0 0xb0 0xc0 0xd0
		 * mesh point: 0xb0 0xc0 0xd0
		 * P2P-client: 0x40 0xd0
		 * P2P-GO: 0x00 0x20 0x40 0xa0 0xb0 0xc0 0xd0
		 * P2P-device: 0x40 0xb0 0xd0
		 * NAN: 0xb0 0xd0
	Supported extended features:
		* [ RRM ]: RRM
		* [ SET_SCAN_DWELL ]: scan dwell setting
		* [ BEACON_RATE_LEGACY ]: legacy beacon rate setting
		* [ BEACON_RATE_HT ]: HT beacon rate setting
		* [ BEACON_RATE_VHT ]: VHT beacon rate setting
		* [ FILS_STA ]: STA FILS (Fast Initial Link Setup)
		* [ CQM_RSSI_LIST ]: multiple CQM_RSSI_THOLD records
		* [ CONTROL_PORT_OVER_NL80211 ]: control port over nl80211
		* [ ACK_SIGNAL_SUPPORT ]: ack signal level support
		* [ TXQS ]: FQ-CoDel-enabled intermediate TXQs
		* [ CAN_REPLACE_PTK0 ]: can safely replace PTK 0 when rekeying
		* [ AIRTIME_FAIRNESS ]: airtime fairness scheduling
		* [ AQL ]: Airtime Queue Limits (AQL)
		* [ CONTROL_PORT_NO_PREAUTH ]: disable pre-auth over nl80211 control port support
		* [ SCAN_FREQ_KHZ ]: scan on kHz frequency support
		* [ CONTROL_PORT_OVER_NL80211_TX_STATUS ]: tx status for nl80211 control port support
		* [ BEACON_RATE_HE ]: HE beacon rate support (AP/mesh)
		* [ POWERED_ADDR_CHANGE ]: can change MAC address while up
```
:::::


:::::ExpandableHeading
### `lsusb -v -d 0e8d:7961`
```bash
$ sudo lsusb -v -d 0e8d:7961

Bus 002 Device 003: ID 0e8d:7961 MediaTek Inc. Wireless_Device
Negotiated speed: SuperSpeed (5Gbps)
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               3.20
  bDeviceClass          239 Miscellaneous Device
  bDeviceSubClass         2 [unknown]
  bDeviceProtocol         1 Interface Association
  bMaxPacketSize0         9
  idVendor           0x0e8d MediaTek Inc.
  idProduct          0x7961 Wireless_Device
  bcdDevice            1.00
  iManufacturer           6 MediaTek Inc.
  iProduct                7 Wireless_Device
  iSerial                 8 000000000
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength       0x0214
    bNumInterfaces          4
    bConfigurationValue     1
    iConfiguration          9 Config_01
    bmAttributes         0xa0
      (Bus Powered)
      Remote Wakeup
    MaxPower              160mA
    Interface Association:
      bLength                 8
      bDescriptorType        11
      bFirstInterface         0
      bInterfaceCount         3
      bFunctionClass        224 Wireless
      bFunctionSubClass       1 Radio Frequency
      bFunctionProtocol       1 Bluetooth
      iFunction               5 BT_FUNCTION
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           5
      bInterfaceClass       224 Wireless
      bInterfaceSubClass      1 Radio Frequency
      bInterfaceProtocol      1 Bluetooth
      iInterface              1 BT_ACL_If
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x81  EP 1 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0040  1x 64 bytes
        bInterval               1
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x01  EP 1 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0400  1x 1024 bytes
        bInterval               0
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x82  EP 2 IN
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0400  1x 1024 bytes
        bInterval               0
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x02  EP 2 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0400  1x 1024 bytes
        bInterval               0
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x8f  EP 15 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0002  1x 2 bytes
        bInterval               1
        bMaxBurst               0
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        1
      bAlternateSetting       0
      bNumEndpoints           2
      bInterfaceClass       224 Wireless
      bInterfaceSubClass      1 Radio Frequency
      bInterfaceProtocol      1 Bluetooth
      iInterface              2 BT_SCO_If
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x83  EP 3 IN
        bmAttributes            1
          Transfer Type            Isochronous
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0000  1x 0 bytes
        bInterval               4
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x03  EP 3 OUT
        bmAttributes            1
          Transfer Type            Isochronous
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0000  1x 0 bytes
        bInterval               4
        bMaxBurst               0
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        1
      bAlternateSetting       1
      bNumEndpoints           2
      bInterfaceClass       224 Wireless
      bInterfaceSubClass      1 Radio Frequency
      bInterfaceProtocol      1 Bluetooth
      iInterface              2 BT_SCO_If
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x83  EP 3 IN
        bmAttributes            1
          Transfer Type            Isochronous
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0009  1x 9 bytes
        bInterval               4
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x03  EP 3 OUT
        bmAttributes            1
          Transfer Type            Isochronous
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0009  1x 9 bytes
        bInterval               4
        bMaxBurst               0
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        1
      bAlternateSetting       2
      bNumEndpoints           2
      bInterfaceClass       224 Wireless
      bInterfaceSubClass      1 Radio Frequency
      bInterfaceProtocol      1 Bluetooth
      iInterface              2 BT_SCO_If
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x83  EP 3 IN
        bmAttributes            1
          Transfer Type            Isochronous
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0011  1x 17 bytes
        bInterval               4
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x03  EP 3 OUT
        bmAttributes            1
          Transfer Type            Isochronous
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0011  1x 17 bytes
        bInterval               4
        bMaxBurst               0
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        1
      bAlternateSetting       3
      bNumEndpoints           2
      bInterfaceClass       224 Wireless
      bInterfaceSubClass      1 Radio Frequency
      bInterfaceProtocol      1 Bluetooth
      iInterface              2 BT_SCO_If
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x83  EP 3 IN
        bmAttributes            1
          Transfer Type            Isochronous
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0019  1x 25 bytes
        bInterval               4
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x03  EP 3 OUT
        bmAttributes            1
          Transfer Type            Isochronous
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0019  1x 25 bytes
        bInterval               4
        bMaxBurst               0
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        1
      bAlternateSetting       4
      bNumEndpoints           2
      bInterfaceClass       224 Wireless
      bInterfaceSubClass      1 Radio Frequency
      bInterfaceProtocol      1 Bluetooth
      iInterface              2 BT_SCO_If
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x83  EP 3 IN
        bmAttributes            1
          Transfer Type            Isochronous
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0021  1x 33 bytes
        bInterval               4
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x03  EP 3 OUT
        bmAttributes            1
          Transfer Type            Isochronous
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0021  1x 33 bytes
        bInterval               4
        bMaxBurst               0
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        1
      bAlternateSetting       5
      bNumEndpoints           2
      bInterfaceClass       224 Wireless
      bInterfaceSubClass      1 Radio Frequency
      bInterfaceProtocol      1 Bluetooth
      iInterface              2 BT_SCO_If
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x83  EP 3 IN
        bmAttributes            1
          Transfer Type            Isochronous
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0031  1x 49 bytes
        bInterval               4
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x03  EP 3 OUT
        bmAttributes            1
          Transfer Type            Isochronous
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0031  1x 49 bytes
        bInterval               4
        bMaxBurst               0
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        1
      bAlternateSetting       6
      bNumEndpoints           2
      bInterfaceClass       224 Wireless
      bInterfaceSubClass      1 Radio Frequency
      bInterfaceProtocol      1 Bluetooth
      iInterface              2 BT_SCO_If
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x83  EP 3 IN
        bmAttributes            1
          Transfer Type            Isochronous
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x003f  1x 63 bytes
        bInterval               4
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x03  EP 3 OUT
        bmAttributes            1
          Transfer Type            Isochronous
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x003f  1x 63 bytes
        bInterval               4
        bMaxBurst               0
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        2
      bAlternateSetting       0
      bNumEndpoints           2
      bInterfaceClass       224 Wireless
      bInterfaceSubClass      1 Radio Frequency
      bInterfaceProtocol      1 Bluetooth
      iInterface              3 BT_ISO_If
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x8a  EP 10 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0040  1x 64 bytes
        bInterval               1
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x0a  EP 10 OUT
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0040  1x 64 bytes
        bInterval               1
        bMaxBurst               0
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        2
      bAlternateSetting       1
      bNumEndpoints           2
      bInterfaceClass       224 Wireless
      bInterfaceSubClass      1 Radio Frequency
      bInterfaceProtocol      1 Bluetooth
      iInterface              3 BT_ISO_If
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x8a  EP 10 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0200  1x 512 bytes
        bInterval               1
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x0a  EP 10 OUT
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0200  1x 512 bytes
        bInterval               1
        bMaxBurst               0
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        3
      bAlternateSetting       0
      bNumEndpoints           9
      bInterfaceClass       255 Vendor Specific Class
      bInterfaceSubClass    255 Vendor Specific Subclass
      bInterfaceProtocol    255 Vendor Specific Protocol
      iInterface              4 WiFi_If
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x84  EP 4 IN
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0400  1x 1024 bytes
        bInterval               0
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x85  EP 5 IN
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0400  1x 1024 bytes
        bInterval               0
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x08  EP 8 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0400  1x 1024 bytes
        bInterval               0
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x04  EP 4 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0400  1x 1024 bytes
        bInterval               0
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x05  EP 5 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0400  1x 1024 bytes
        bInterval               0
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x06  EP 6 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0400  1x 1024 bytes
        bInterval               0
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x07  EP 7 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0400  1x 1024 bytes
        bInterval               0
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x09  EP 9 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0400  1x 1024 bytes
        bInterval               0
        bMaxBurst               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x86  EP 6 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0002  1x 2 bytes
        bInterval               1
        bMaxBurst               0
Binary Object Store Descriptor:
  bLength                 5
  bDescriptorType        15
  wTotalLength       0x0016
  bNumDeviceCaps          2
  USB 2.0 Extension Device Capability:
    bLength                 7
    bDescriptorType        16
    bDevCapabilityType      2
    bmAttributes   0x0000f11e
      BESL Link Power Management (LPM) Supported
    BESL value      256 us
    Deep BESL value    61440 us
  SuperSpeed USB Device Capability:
    bLength                10
    bDescriptorType        16
    bDevCapabilityType      3
    bmAttributes         0x00
    wSpeedsSupported   0x000e
      Device can operate at Full Speed (12Mbps)
      Device can operate at High Speed (480Mbps)
      Device can operate at SuperSpeed (5Gbps)
    bFunctionalitySupport   1
      Lowest fully-functional device speed is Full Speed (12Mbps)
    bU1DevExitLat          10 micro seconds
    bU2DevExitLat         180 micro seconds
Device Status:     0x0000
  (Bus Powered)
```
:::::

:::::ExpandableHeading
### `dmesg`

```bash
$ dmesg | grep mt7
[   12.972161] usbcore: registered new interface driver mt7921u
[   12.975915] mt7921u 2-1.1:1.3: HW/SW Version: 0x8a108a10, Build Time: 20260224110909a
[   13.233001] mt7921u 2-1.1:1.3: WM Firmware Version: ____010000, Build Time: 20260224110949
[   14.869033] mt7921u 2-1.1:1.3 wlxb06b11673ade: renamed from wlan0
[   43.432790] mt7921u 2-1.1:1.3 wlxb06b11673ade: entered allmulticast mode
[   43.433616] mt7921u 2-1.1:1.3 wlxb06b11673ade: entered promiscuous mode
```
:::::
