# Video Decoding

## Hardware video decoding tests

Rockchip RK3576 supports hardware video decoding of popular codecs up to 8K@30fps for H.265/HEVC.
This sections describes how to properly test hardware video decoding.

# Rockchip RK3576 Hardware Video decoders

![Rockchip RK3576 Hardware Video decoders](files/pics/rk3576_hardware_video_decoders.png)

# Sample video files

| Video File     | Description | 
| -------- | ------- |
| [Jellyfish 4K AVC.mkv 897 MB](https://repo.jellyfin.org/archive/jellyfish/media/jellyfish-250-mbps-4k-uhd-h264.mkv)  | **H.264/AVC**, Bitrate: 250 Mbps, 3840x2160, 30 fps, Profile: High 8 bit color, Level: 5.1 |
| [Jellyfin 8K 60FPS HEVC.mp4 528 MB](https://repo.jellyfin.org/test-videos/SDR/HEVC%2010bit/Test%20Jellyfin%208K%20HEVC%2010bit%20150M.mp4) | **H.265/HEVC** Bitrate: 150 Mbps, 7680x4320, 60 fps, 10 bit color |
| [Jellyfin 8K 30FPS HEVC.mp4 130 MB](https://zhovner.com/tmp/Jellyfin-8K-HEVC-10bit-150M_30fps.mp4) | **H.265/HEVC** 7680x4320, 30 fps, 10 bit color (⚠️ Dirty re-encoding to match 30FPS, Bitrate around 50 Mbps, not trusted sample)|

# Current status

### H.264/AVC (Jellyfish 4K AVC.mkv)
| H96 Max M9 Android TV | Flipper Linux Builds | 
| -------- | ------- |
| ✅ No drops | ❌ Frame drops |

### H.265/HEVC (Jellyfin 8K 60FPS HEVC.mp4)
| H96 Max M9 Android TV | Flipper Builds | 
| -------- | ------- |
|❌ Frame drops | ❌ Frame drops |

### H.265/HEVC (Jellyfin 8K 30FPS HEVC.mp4)
| H96 Max M9 Android TV | Flipper Builds | 
| -------- | ------- |
|✅ No drops | ❌ Frame drops |
