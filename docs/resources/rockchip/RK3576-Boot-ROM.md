---
title: RK3576 Boot ROM
slug: resources/rockchip/boot-rom
docTags: 
createdAt: Wed Aug 19 2026 00:00:00 GMT+0000 (Coordinated Universal Time)
updatedAt: Wed Aug 19 2026 00:00:00 GMT+0000 (Coordinated Universal Time)
---


The RK3576 SoC uses an on-chip non-modifiable piece of code to initialize key hardware blocks required for early boot and load early stage bootloader code. It is called the boot ROM, and it is always available, impossible to erase without physically damaging the chip, and it defines where and how the RK3576 can grab the first user-provided code to run.

At power up, before anything else runs, the boot ROM gets mapped at the physical memory address 0x0, and it is 43033 bytes long, executing in place. It is AArch64, runs at EL3, SP = 0x3ff81000, VBAR = 0x3ff80xxx-relative vectors at 0xa000. IRAM is 0x3ff80000.

When the boot ROM first executes, it zeroes out the IRAM, selects the boot order mode and tries each available boot source until one works. The boot order mode selection is as follows, in order:

- Check for a boot mode requested before soft-reboot via the `PMU1_GRF_OS_REG0` register (MMIO address 0x26026200). This allows a "reboot to X" action from a running OS:
  - Register value 0xEF08A53C = mode 1 (Maskrom only)
  - Register value 0xEF085A3x = mode x, where x is the number of the boot mode requested, 0x1..0xb
- Check the forced boot mode value in the OTP cell 0x64:
  - bits\[3:0] - selected boot mode, 0x1..0xb
  - bits\[7:4] - one's complement of the selected boot mode (to check validity of the fused value)
  - bits\[17:16] - force boot mode 9
- Check the board strapping of SARADC channel 0 (one-shot single-channel reading, polling for the completion interrupt). The value that has been read is also stored at 0x3ff80008 in the upper 16 bits of the 32-bit value, where it can be read by early stage bootloader code

# Boot modes

| mode | ADC code    | Decimal   | Voltage @1.8 Vref | boot order                                                                   |
| ---- | ----------- | --------- | ----------------- | ---------------------------------------------------------------------------- |
| 1    | 0x000–0x0cf | 0–207     | 0.000–0.091       | USB                                                                          |
| 2    | 0x0d0–0x267 | 208–615   | 0.091–0.271       | SPINOR, SPINAND, USB                                                         |
| 3    | 0x268–0x3fe | 616–1022  | 0.271–0.450       | SPINOR.m1, SPINAND.m1, eMMC, USB                                             |
| 4    | 0x3ff–0x5a3 | 1023–1443 | 0.450–0.635       | SPINOR.m2, SPINAND.m2, eMMC, USB                                             |
| 5    | 0x5a4–0x73c | 1444–1852 | 0.635–0.814       | SPINOR, SPINAND, UFS, USB                                                    |
| 6    | 0x73d–0x8c2 | 1853–2242 | 0.814–0.986       | SPINOR.m1, SPINAND.m1, UFS, USB                                              |
| 7    | 0x8c3–0xa5a | 2243–2650 | 0.986–1.165       | UFS, USB                                                                     |
| 8    | 0xa5b–0xbfe | 2651–3070 | 1.165–1.350       | UFS, SD, USB                                                                 |
| 9    | 0xbff–0xd96 | 3071–3478 | 1.350–1.529       | SPINOR.m2, SPINAND.m2, SPINOR.m1, SPINAND.m1, SPINOR, SPINAND, eMMC, SD, USB |
| 10   | 0xd97–0xf2e | 3479–3886 | 1.529–1.708       | eMMC, SD, USB                                                                |
| 11   | 0xf2f–0xfff | 3887–4095 | 1.708–1.800       | eMMC, USB                                                                    |

## USB boot (Maskrom)

Whenever boot mode 1 is selected, or any of the other modes exhausts all storage based options and falls back, the boot ROM enters the USB download mode which Rockchip tools call Maskrom. In this mode it initializes the USB0 controller and its PHY in a device mode, so that the board can be connected to a host computer with a USB cable, and it shows up as

```linux
ID 2207:350e Fuzhou Rockchip Electronics Company
```

At this point it can be accessed using Rockchip's maskrom protocol, as implemented by various tools such as [rkdeveloptool](https://github.com/rockchip-linux/rkdeveloptool), [rockusb](https://github.com/collabora/rockchiprs/) or the Windows-based closed-source RKDevTool

The Maskrom protocol only uploads binaries to the device, and their processing is fully driven by the boot ROM. Two payload types are envisaged:

- Code 0x471. This is meant for small early-stage binaries which the boot ROM places in SRAM and executes. More than one can be submitted, and they normally return control to the boot ROM upon completion. This is what is used for boost.bin and the DDR initialization blob. The binaries here are raw AArch64 executable code, normally with only pc-relative addresses, and the execution starts at the beginning address of the binary
- Code 0x472. This is meant for the code which relies on normal system RAM already up and running, such as the U-Boot SPL binary. The binary here is&#x20;

Note that the boot ROM enters the 0x471 phase with MMU and caches off and with a single CPU "little" core running. This makes both instruction and data fetches very slow.

Any payload gets verified against a CRC16-CCITT checksum which all maskrom tools append after the binary body itself. RK3576 uses an extremely slow bitwise implementation of the checksum routine with a throughput of about 124 kB/s. This makes uploading larger payloads (such as a full SPL+U-Boot image, or an SPL+Falcon Linux image) as 0x472 unbearably slow. There are two tricks to make it more reasonable:

- Skip the CRC check. RK3576 first checks if both CRC bytes are zero, and if they are it silently accepts the binary without calculating its checksum at all. This can be achieved either by patching the host-side maskrom tool to send zeros where it would have normally written the checksum, or by appending a checksum to the uploaded binary itself, in which case the CRC the maskrom tool calculates cancels out arithmetically and becomes all-zero, due to the way how the algorithm works.
- Enable I-cache from a tiny custom 0x471 payload before loading anything larger. One major factor for the slow performance of the RK3576 CRC routine is having to fetch \~100 instructions per byte from slow uncached ROM storage - this is even slower than fetching payload data from uncached RAM byte by byte. With the I-cache on, the whole code of the CRC routine stays in the CPU's L1 instruction cache, which increases throughput from 124 kB/s to about 2 MB/s

```с
       /*
        * Enable the EL3 instruction cache before returning to the BootROM
        */
       asm volatile("mrs %0, sctlr_el3" : "=r"(sctlr));
       sctlr |= (1UL << 12);
       asm volatile("msr sctlr_el3, %0; isb" :: "r"(sctlr) : "memory");
```

## Normal boot from persistent storage

When the boot ROM tries to boot from persistent storage (as prescribed by the active boot mode), it is looking for a valid loadable image at fixed offsets from the start of the storage device being considered.

A valid loadable image can be either an RKNS (for non-secure boot) or an RKSS one (for secure boot), and the boot ROM checks that the RKNS/RKSS header is valid AND that all image components match the digest recorded in the header for each.

For each storage device, the boot ROM starts searching for the RKNS/RKSS header at the 512-byte sector 64 (or equivalently at the 4096-byte sector 8 in case of UFS). If not found, it proceeds to look for the same header at further locations on the same device in 512 kB strides for up to 16 copies in case of SPI flash, or up to 5 copies in case of UFS and SD/MMC. If none of those addresses hold a valid RKNS/RKSS header with matching data, the next storage device is tried according to the active boot mode. If no storage device contains a valid image, the boot ROM falls back to maskrom.

Loop `n = 0 .. copy_count-1`:
- Check magic `RKNS` (0xa7f8) or `RKSS` (0xa7fc) at the buffer start.
- Publish to IRAM: `0x3ff80010 = bootsource_id` (`BROM_BOOTSOURCE_ID_ADDR`) and `0x3ff80014 = lba512` of the copy that was accepted.
- Copy the header to `0x3ff80400`
- Secure path (IRAM+0xc != 0): requires `RKSS` image and does RSA verification
- Non-secure path (IRAM+0xc == 0 and IRAM+0x8c == 0xffffffff, a redundant anti-glitch check): `RKNS` accepted without an RSA signature but each component is still digest-checked.
- Digest verification:
  - For each component, its 32-byte digest is stored at `component entry + 0x18` in the image
  - Digest algorithm is controlled by `hdr+0x0c`: bit 14 set disables verification entirely; otherwise `bits[3:0]` select the algorithm (0 or 1 → SHA-256, 3 → SM3, anything else rejected)
  - The boot ROM uses the hardware crypto engine at 0x2a430000 (`CRYPTO_HASH_CTL` 0x24 / 0x64) to calculate the digest over the sector-aligned length of the component payload (sector count is taken from the component header). A torn or partial payload write is therefore caught by the ROM even without secure boot.
- Component table: `hdr[0x0a] & 0xf` entries (≤ 4) at `hdr+0x78`, stride 0x58:

  ```
  +0x00 u16 sector_offset   # 512-byte units, relative to the ID-block LBA
  +0x02 u16 sector_count    # 512-byte units
  +0x04 u32 load_addr       # 0xffffffff => 0x3ff81000 for entry 0, else 0x40000000
  +0x08 u8  flags           # if bits[3:0] are 0x3, then the component is rejected unless PMU1_GRF_OS_REG8 bits[3:0] are 0xf
  ```
  Validation: `load_addr >= 0x3ff81000`, and end must be `< 0x40000001` (SRAM) or `<= 0x50000000` (DRAM window).
- Any failure (bad magic, bad header, failed read, failed signature) falls through to the next copy `n+1`.
- After all copies fail, `0x1c2c` returns and the ROM moves to the next entry of the boot-order list (eventually USB maskrom)

### UFS boot specifics

UFS devices can be provisioned with multiple logical units (LUs), and the boot ROM can boot from different LUs depending on its configuration:
- By default, the JEDEC Boot Well-Known LUN is used, as configured in the UFS descriptors on the device itself
- Can be overriden by setting bit 14 in the OTP configuration word 0x65 and selecting an arbitrary LUN in bits[23:16] there:

<table isTableHeaderOn="true" columnWidths="85,85,365,155">
  <tr>
    <td align="left">
      <p>bits</p>
    </td>
    <td align="left">
      <p>coding</p>
    </td>
    <td align="left">
      <p>effect when set</p>
    </td>
    <td align="left">
      <p>default (unfused)</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>[1:0]</code></p>
    </td>
    <td>
      <p>pair, both=1</p>
    </td>
    <td>
      <p><code>IRAM+0x54 = 0x1a</code> (26): XIN is 26 MHz</p>
    </td>
    <td>
      <p><code>IRAM+0x54 = 0x18</code> (24 MHz)</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>[3:2]</code></p>
    </td>
    <td>
      <p>—</p>
    </td>
    <td>
      <p>unused</p>
    </td>
    <td>
      <p>—</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>[5:4]</code></p>
    </td>
    <td>
      <p>pair, both=1</p>
    </td>
    <td>
      <p><code>IRAM+0xb8 = 1</code> → <code>usb2phy_grf+0xe008 = 0x4000_0000</code> (USB2 PHY, not related to UFS)</p>
    </td>
    <td>
      <p>0</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>[7:6]</code></p>
    </td>
    <td>
      <p>pair, both=1</p>
    </td>
    <td>
      <p>extra pad config</p>
    </td>
    <td>
      <p>skipped</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>[11:8]</code></p>
    </td>
    <td>
      <p>4-bit index</p>
    </td>
    <td>
      <p>copied into <code>IRAM+0xb4[3:0]</code>; indexes a 15-entry × 4-byte MPHY RX trim table. Entry bytes program, for both lanes: <code>b0</code>→MPHY <code>0x134</code>/<code>0x274</code> (TRSV_REG15), <code>b1</code>→<code>0xe0</code>/<code>0x220</code> (REG08), <code>b2</code>→<code>0x164</code>/<code>0x2a4</code> (REG29), <code>b3</code>→<code>0x178</code>/<code>0x2b8</code> (REG2E)</p>
    </td>
    <td>
      <p>index 0 → <code>&#123;03,38,50,80&#125;</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>[12]</code></p>
    </td>
    <td>
      <p>single bit</p>
    </td>
    <td>
      <p><code>IRAM+0xb4</code> bit 4 → run <code>vops[1]</code> = <code>0x620c</code> after link startup: PA_TxGear=3, PA_HSSeries=2 (Rate B), PA_PWRMode=0x44 → HS-G3 Rate-B, 2 lanes</p>
    </td>
    <td>
      <p>off → link stays at PWM-G1</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>[13]</code></p>
    </td>
    <td>
      <p>single bit</p>
    </td>
    <td>
      <p><code>IRAM+0xb4</code> bit 5 → issue <code>SET FLAG fDeviceInit</code> (IDN 0x01) and poll <code>READ FLAG fDeviceInit</code> up to 15001 × 100 µs (<code>0x9280..0x92dc</code>)</p>
    </td>
    <td>
      <p>off → no device-init handshake</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>[14]</code></p>
    </td>
    <td>
      <p>single bit</p>
    </td>
    <td>
      <p><strong>enables the LUN override</strong>: <code>IRAM+0xb0 = bits[23:16]</code></p>
    </td>
    <td>
      <p>off → <code>IRAM+0xb0 = 0xB0</code> (<code>UFS_UPIU_BOOT_WLUN</code>)</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>[23:16]</code></p>
    </td>
    <td>
      <p>u8</p>
    </td>
    <td>
      <p>the LUN used for every UFS command, when bit 14 is set</p>
    </td>
    <td>
      <p>n/a</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>[31:24]</code></p>
    </td>
    <td>
      <p>—</p>
    </td>
    <td>
      <p>unused on this path</p>
    </td>
    <td>
      <p>—</p>
    </td>
  </tr>
</table>
