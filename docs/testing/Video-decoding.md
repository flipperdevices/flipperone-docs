---
title: Video Decoding
slug: testing/graphics/video-decoding
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:25:37 GMT+0000 (Coordinated Universal Time)
---

## Hardware video decoding tests

Rockchip RK3576 supports hardware video decoding of popular codecs up to 8K\@30fps for H.265/HEVC.
This section describes how to properly test hardware video decoding.

***

# Rockchip RK3576 Hardware Video decoders

![Rockchip RK3576 Hardware Video decoders](files/pics/rk3576_hardware_video_decoders.png)

***

# Sample video files

<table isTableHeaderOn="true" columnWidths="331,332">
  <tr>
    <td>
      <p>Video File</p>
    </td>
    <td>
      <p>Description</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><a href="https://repo.jellyfin.org/archive/jellyfish/media/jellyfish-250-mbps-4k-uhd-h264.mkv">Jellyfish 4K AVC.mkv 897 MB</a></p>
    </td>
    <td>
      <p><strong>H.264/AVC</strong>, Bitrate: 250 Mbps, 3840x2160, 30 fps, Profile: High 8 bit color, Level: 5.1</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><a href="https://repo.jellyfin.org/test-videos/SDR/HEVC%2010bit/Test%20Jellyfin%208K%20HEVC%2010bit%20150M.mp4">Jellyfin 8K 60FPS HEVC.mp4 528 MB</a></p>
    </td>
    <td>
      <p><strong>H.265/HEVC</strong> Bitrate: 150 Mbps, 7680x4320, 60 fps, 10 bit color</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><a href="https://zhovner.com/tmp/Jellyfin-8K-HEVC-10bit-150M_30fps.mp4">Jellyfin 8K 30FPS HEVC.mp4 130 MB</a></p>
    </td>
    <td>
      <p><strong>H.265/HEVC</strong> 7680x4320, 30 fps, 10 bit color (⚠️ Dirty re-encoding to match 30FPS, Bitrate around 50 Mbps, not trusted sample)</p>
    </td>
  </tr>
</table>

***

# Current status

### H.264/AVC (Jellyfish 4K AVC.mkv)

<table isTableHeaderOn="true" columnWidths="331,332">
  <tr>
    <td>
      <p>H96 Max M9 Android TV</p>
    </td>
    <td>
      <p>Flipper Linux Builds</p>
    </td>
  </tr>
  <tr>
    <td>
      <p>✅ No drops</p>
    </td>
    <td>
      <p>❌ Frame drops</p>
    </td>
  </tr>
</table>

### H.265/HEVC (Jellyfin 8K 60FPS HEVC.mp4)

<table isTableHeaderOn="true" columnWidths="331,332">
  <tr>
    <td>
      <p>H96 Max M9 Android TV</p>
    </td>
    <td>
      <p>Flipper Builds</p>
    </td>
  </tr>
  <tr>
    <td>
      <p>❌ Frame drops</p>
    </td>
    <td>
      <p>❌ Frame drops</p>
    </td>
  </tr>
</table>

### H.265/HEVC (Jellyfin 8K 30FPS HEVC.mp4)

<table isTableHeaderOn="true" columnWidths="331,332">
  <tr>
    <td>
      <p>H96 Max M9 Android TV</p>
    </td>
    <td>
      <p>Flipper Builds</p>
    </td>
  </tr>
  <tr>
    <td>
      <p>✅ No drops</p>
    </td>
    <td>
      <p>❌ Frame drops</p>
    </td>
  </tr>
</table>

