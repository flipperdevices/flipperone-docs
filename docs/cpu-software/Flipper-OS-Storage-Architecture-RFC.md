# RFC: Flipper OS storage architecture — atomic A/B base with overlay profiles

| Field | Value |
|---|---|
| **RFC** | (to be assigned) |
| **Title** | Flipper OS storage architecture: atomic A/B base with overlay profiles |
| **Status** | Draft / Proposed |
| **Sub-project** | 🐧 Linux (CPU Software) — Flipper OS |
| **Author** | xbizzybone |
| **Created** | 2026-06-13 |
| **Tracking issue** | (link to the Flipper OS discussion/issue) |
| **Related** | MCU↔CPU Interconnect; RK3576 mainlining; FlipCTL |

> The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** in this document are to be interpreted as described in RFC 2119.

---

## Summary

This RFC proposes a concrete storage architecture for Flipper OS that satisfies all three of its stated goals simultaneously: **atomic A/B updates with rollback**, **cloneable/resettable OS profiles**, and a familiar **Debian (apt-based) userland**. System state is split into three classes — an immutable A/B base (read-only + dm-verity), a per-profile writable overlay (Btrfs subvolume), and a persistent user-data partition that survives both profile resets and base updates. A booted profile is an OverlayFS composition of these layers. The base is kept minimal and stateless so that profile configuration lives exclusively in drop-in directories, and a build-time lint mechanically forbids profiles from shadowing base files — eliminating configuration drift as a class. Atomic updates use RAUC with a Linux health-check and an MCU-watchdog backstop. Profile selection happens at early boot, driven by the MCU, and is handed to U-Boot over the existing Interconnect with a small CRC-checked message.

---

## Motivation

The Flipper OS design notes are explicit that the team is *"not 100% sure how to architect it yet."* The problem Flipper OS sets out to solve is real and well-stated in the Flipper One announcement: a general-purpose SBC running a mutable distro degrades into an unrecoverable mess — packages installed and compiled from source, kernels patched, device trees edited — with no clean rollback short of re-flashing the SD card.

Flipper OS promises a way out via **profiles** (full preconfigured environments, selectable at early boot, cloneable and resettable) and **atomic A/B updates**. These two promises pull in opposite directions on a Debian base:

- Profiles imply many writable environments layered on a shared base.
- Atomic updates imply an immutable, replaceable base.
- Debian/apt assumes a single mutable rootfs.

The central architectural question this RFC answers is: **how do profile overlays remain valid when the base is atomically replaced underneath them?** Without a deliberate answer, the first base update silently corrupts every customized profile.

This RFC also aims to be useful beyond Flipper One — the same model applies to any Raspberry-Pi-class cyberdeck or portable Linux box, which is an explicit project goal.

---

## Guide-level explanation

From a contributor's or user's point of view, Flipper OS has three kinds of "stuff":

1. **The OS itself** — shared, read-only, and updated as one atomic unit. You never edit it directly; you replace it.
2. **A profile** — a named, writable environment built on top of the OS (e.g. *Router*, *Network Multitool*, *TV Media Box*, *Desktop*, *Minimal*). You can boot it, break it, `clone` it, or `reset` it back to pristine.
3. **Your data** — files, keys, captures, credentials. This lives apart from everything else, so it survives both resetting a profile and updating the OS.

The boot experience: power on, the MCU shows the profile menu on the built-in screen (no monitor or keyboard needed), you pick one, and Linux boots into it. Picking *reset* or *clone* performs that action first, then boots.

Updating the OS is atomic: the new version is written to a spare slot, and the device only commits to it after it has proven itself healthy. If a boot fails, the device automatically falls back to the previous version — and because the MCU stays alive independently of Linux, a bad update can never brick the device.

The single rule contributors must follow when building a profile: **never edit a base file directly — only add configuration via drop-in directories.** A CI check enforces this, so it is impossible to merge a profile that would break on the next base update.

---

## Reference-level explanation

### State classes

| Class | Mutability | Home | Reset behavior |
|---|---|---|---|
| OS base | Immutable | `base_a` / `base_b`, read-only + dm-verity | Replaced only by an A/B update |
| Profile | Semi-mutable | Btrfs subvolume (`upperdir`) per profile | `reset` wipes the upper → pristine |
| User data | Persistent | Separate `/data` partition (LUKS optional) | Survives profile reset *and* A/B swap |

A running profile MUST be composed as an OverlayFS:

```
overlay root
├── lowerdir : active base slot (base_a|base_b), read-only + dm-verity
├── upperdir : <profiles>/<profile_id>   (Btrfs subvol, writable)
├── workdir  : <profiles>/.work/<profile_id>
└── bind     : /data → /home, /var/lib/..., /srv, /captures
```

User-relevant paths (`/home`, app state, captures) MUST be bind-mounted from `/data` so they are outside the overlay and therefore survive `reset`. This generalizes the OpenWrt model (read-only base + OverlayFS upper, factory reset = wipe the upper) to N named overlays.

### Partition layout (GPT)

```
boot_a     U-Boot + FIT (kernel/dtb/initramfs) slot A   ~64 MB
boot_b     idem, slot B                                 ~64 MB
base_a     rootfs base (squashfs + appended verity)     ~2 GB
base_b     idem, slot B                                 ~2 GB
profiles   Btrfs pool: one subvol (upperdir) per profile  flexible
data       persistent user data (LUKS optional)         remainder
```

- The dm-verity hash tree SHOULD be appended to the base image (standard RAUC + verity pattern); no separate hash partitions are required.
- Slot status and boot counters SHOULD live in the redundant U-Boot environment.
- `boot_a/boot_b` are A/B so bootloader + kernel update atomically alongside the rootfs.

### Filesystem choices

- The profiles pool and `/data` SHOULD be **Btrfs**: reflink yields instant, cheap profile `clone`; subvolumes give a clean per-profile boundary; snapshots make `reset` trivial. `clone` = reflink-copy the subvol; `reset` = drop and recreate from the pristine snapshot. Both are O(metadata).
- The base A/B slots SHOULD remain **outside Btrfs** (plain squashfs + dm-verity) to keep early boot simple and verity-friendly.

### Atomic updates and rollback

The atomic engine SHOULD be **RAUC** (alternatively swupdate): signed bundles, slot selection, U-Boot integration, boot-counter rollback.

```
1. RAUC writes the update to the inactive slot,
   sets bootcount=0 and marks the new slot "try".
2. U-Boot increments bootcount per attempt;
   if it exceeds the limit → boot the other slot.
3. After Linux boots, flipper-health.service validates
   (network up? FlipCTL up? MCU interconnect alive?):
     success → `rauc status mark-good` (commit slot, reset bootcount)
     failure → next reboot rolls back automatically
4. Hardware backstop: if the CPU does not signal "Linux healthy"
   within T seconds, the MCU watchdog forces a reboot into the
   other slot.
```

Step 4 deliberately uses the co-processor architecture: the MCU remains alive when Linux wedges, providing a rollback path that does not depend on Linux being functional.

### Profile manifest

Each profile subvolume MUST carry a manifest:

```toml
[profile]
id   = "network-multitool"
name = "Network Multitool"
base_min_version = "1.4.0"   # refuses to mount on an incompatible base
icon = "net"

[packages]                   # baked at profile build time
include = ["nmap", "tcpdump", "tshark", "iperf3", "netcat-openbsd"]

[overlay]
writable = true
```

`base_min_version` is the anti-corruption guard: after a base update, an incompatible profile MUST refuse to mount and offer a rebuild rather than corrupting silently.

Package layering on Debian (without content-addressing) is handled in two tiers:
- **Blessed profiles** — packages baked at build time → reproducible, rollback-safe.
- **Runtime scratch** — the user MAY `apt install` into the overlay, explicitly accepting that this layer is non-atomic and non-reproducible.

### Configuration discipline (drift elimination)

The base MUST be stateless: `/usr` is the OS; `/etc` defaults are regenerated via `systemd-tmpfiles` and `systemd-sysusers`. A profile's only writable configuration surface is drop-in directories (`*.d/` unit overrides, `/etc/systemd/network/NN-*.network`, `/etc/sysctl.d/`, `/etc/modprobe.d/`, `udev/rules.d/`, `tmpfiles.d/`, `sysusers.d/`).

Enforcement is a **build-time lint**: the profile build MUST fail if the `upperdir` contains any path that also exists in the base image (a shadow/override), unless that path is under a whitelisted drop-in directory. For an application that only reads a monolithic config file, the profile ships the whole file and the base MUST NOT ship that path, so there is no collision on update. A 3-way merge (`base_version` / `original_default` / `profile_modified`) is a rare fallback, not the primary mechanism.

### Boot-time profile selection (MCU ↔ U-Boot)

Selection happens before the rootfs mounts, on the MCU display. The MCU owns the menu; Linux consumes the result. Early in boot, U-Boot reads a latched `BOOT_SELECTION` register from the MCU over I²C:

```c
struct boot_selection {
  u8   magic;        // 0xF1
  u8   version;
  u8   action;       // 0=BOOT 1=CLONE+BOOT 2=RESET+BOOT 3=RECOVERY
  char profile_id[16];
  u8   slot;         // 0=A 1=B 0xFF=auto (RAUC decides)
  u8   flags;
  u16  crc;
};
```

U-Boot translates this into kernel args (`flipper.profile=<id> flipper.action=<a>`), selects the FIT/slot, and boots. The initramfs reads `/proc/cmdline`, performs the action (clone/reset the Btrfs subvol via reflink), assembles the OverlayFS, bind-mounts `/data`, and `switch_root`s. A CRC suffices for integrity; both chips are on-device, so cryptographic authentication is not required here.

MCU-side state machine:

```
IDLE → MENU → SELECTED (latched, exposed to U-Boot) → BOOTING
  ▲                                                     │
  └──────────── "Linux up" signal from CPU ◄────────────┘
```

### Security boundary

- **Base** — signed (RAUC bundle signature) + dm-verity ⇒ integrity guaranteed and tamper-evident.
- **Overlay** — writable, **not** verity-protected, explicitly user-trusted. Modifying a profile breaks that profile's userspace integrity guarantee **by design**.
- **Data** — optional LUKS at rest on `/data`; key handling MAY later move into OP-TEE, or use a passphrase entered via FlipCTL.
- **Boot menu** — the MCU is on-device and trusted; the I²C message carries a CRC for integrity only.

---

## Drawbacks

- Imposing immutability and drop-in-only configuration on a Debian base is a behavioral change from a stock Debian/Raspberry Pi OS workflow; some upstream packages assume a writable monolithic `/etc`.
- Maintaining multiple overlay uppers costs storage versus a single rootfs, and OverlayFS has known edge cases (rename semantics, whiteouts) that the team will need to validate against the chosen workloads.
- Baking packages at build time limits runtime flexibility; the "runtime scratch" escape hatch reintroduces a non-atomic layer that must be clearly delimited to users.
- dm-verity protects only the base; the overlay is inherently unverified. The trust boundary must be communicated clearly so users understand what guarantees survive their own changes.

---

## Rationale and alternatives

Three base-layer models were considered:

- **A — Overlay-only with a minimal, stateless base (proposed).** Profile-specific packages and config live in the overlay; the base stays small and rarely changes. Minimal conflict surface; cheap clone/reset; keeps apt familiarity. *Chosen.*
- **B — One full image per profile.** No overlay/base coupling, but storage scales as N × image × 2 (for A/B) and the cheap clone/reset semantics are lost. Not viable on embedded eMMC. *Rejected.*
- **C — Content-addressed base (ostree).** Solves atomicity and dedup elegantly and is production-proven, but Debian's deb-ostree tooling is far less mature than the RPM side, and it diverges from the apt-based direction. Highest robustness, highest cost. *Deferred — see Future possibilities.*

The proposal deliberately borrows ostree's *mental model* (immutable base, deployments, atomic switch) while implementing it with A/B image slots, so a later migration to Option C remains open if Debian-ostree tooling matures.

A "do nothing special" alternative — plain mutable Debian plus `etckeeper`/snapshots — was rejected because it provides neither atomic updates nor a reliable factory-reset, which are the two defining features of Flipper OS.

---

## Prior art

- **OpenWrt** — read-only squashfs base + OverlayFS upper, with "factory reset" = wipe the upper. This is the direct ancestor of the profile model here, and notably its primary use case (Router) is one of Flipper OS's profiles.
- **Android A/B (seamless) updates** — two slots, boot-time selection, automatic rollback via a bootloader boot-counter. The basis for the A/B + health-check flow.
- **RAUC / Mender / SWUpdate** — the established embedded-Linux OTA frameworks for signed, atomic A/B updates with U-Boot integration. RAUC is proposed as the engine rather than reinventing transaction logic.
- **Fedora Silverblue / Endless OS (ostree)** — content-addressed immutable base with git-like deployments and rollback; the reference for the immutable-base mental model (Option C).
- **NixOS generations** — declarative, atomic, rollback-able system generations; conceptual kin to "profiles you can switch between and revert."

---

## Unresolved questions

1. **Monolithic-config drift.** The drop-in discipline + lint covers the common case; the residual is applications that only read a single config file. Is a 3-way merge acceptable for those, or should they be hard-required to use drop-in-capable configuration?
2. **Runtime layering vs. atomicity.** How visible should the non-atomic "runtime scratch" boundary be, and should runtime-installed packages be promotable into a blessed (reproducible) profile?
3. **OverlayFS workload validation.** Which profile workloads stress OverlayFS edge cases (e.g. databases, heavy rename activity) enough to warrant a per-profile escape to a plain subvolume root instead of an overlay?

---

## Future possibilities

- **OP-TEE-backed disk encryption** for `/data`, tying into the in-progress RK3576 TEE work.
- **Profile manager in FlipCTL** — browse, clone, reset, import/export profiles directly from the built-in UI.
- **Profile sharing** — export a profile subvolume as a portable artifact so the community can distribute ready-made profiles (a "profile store").
- **Promotion workflow** — turn a proven runtime-scratch layer into a reproducible, baked profile.
- **Migration to ostree (Option C)** if/when Debian's content-addressed tooling matures, reusing the immutable-base model adopted here.

---

## Implementation plan (phased)

| Phase | Scope | Demonstrable outcome |
|---|---|---|
| 0 | Single base (squashfs + dm-verity), 2–3 overlay profiles on Btrfs, `/data` partition, selection via kernel cmdline | Clone/reset/boot profiles on an RK3576 SBC |
| 1 | MCU boot menu + `BOOT_SELECTION` Interconnect handshake | Pick/clone/reset a profile from the built-in screen |
| 2 | RAUC A/B for base + boot slots, `flipper-health.service`, MCU-watchdog backstop | Atomic update with automatic rollback |
| 3 | Build-time `/etc`-shadow lint, profile manifest + `base_min_version` guard, optional LUKS on `/data` | Drift-proof, corruption-guarded, optionally encrypted |

Each phase is independently demonstrable, keeping risk bounded and giving contributors self-contained pieces to pick up.
