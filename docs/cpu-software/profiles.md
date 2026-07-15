---
title: OS profiles and snapshots
slug: cpu-software/profiles
docTags: 
createdAt: Mon Jul 14 2026 00:00:00 GMT+0000 (Coordinated Universal Time)
updatedAt: Mon Jul 14 2026 00:00:00 GMT+0000 (Coordinated Universal Time)
---

This guide explains OS profiles and snapshots in Flipper OS: their purpose, how to use, and how to manage them using CLI helper tools.

TL;DR:

- **Profile** is a system you can **boot into and use**. Profiles are mutable: each time you install new packages, change configurations, or add any other files, a profile is updated in the file system.
- **Stock profile** is an initial profile backup, a clean system. Stock profiles are immutable. You can't boot a stock profile, but you can **create a new profile** from it. 
- **Snapshot** is a frozen backup of a profile. Snapshots are immutable. You can't boot a snapshot, but you can **restore a profile** from it.

## Problem overview

When a Linux device is used as a multitool, in roles like a Wi-Fi router, a media box, and a desktop, it gradually accumulates installed packages, modified config files, and saved data. Eventually, the system becomes too messy to use, and the only solution is to reinstall it from scratch. With a multitool, users often need to switch between setups, save a working state before experimenting, and roll back after breaking things.

Flipper OS solves this problem using profiles and snapshots. Profiles allow users to maintain several independent system configurations and switch between them at boot, while snapshots serve as recoverable save points within each profile.

## Profiles and snapshots

### What is an OS profile?

Think of a profile like a separate "computer setup" on your Flipper One. When you turn the device on, you see a boot menu where each boot target represents a profile: Desktop, Router, TV Media Box, No Graphics, and so on.

Each profile:

- **Can be booted** (it shows up in the boot menu).
- **Can be changed**: install apps, tweak settings, break things. It's yours.
- **Remembers your changes** between reboots.

You can have several profiles side by side and switch between them by rebooting.

::embed[]{url="https://www.youtube.com/watch?v=oI6Vl_uoAwI"}

**Which profile am I in right now?** There are two easy ways to check:

1. The welcome banner shown when you log in, on the `Profile:` line:
   ```
   Welcome to FlipperOne
      Board:    one-rev-f0b0c1
      Memory:   7.8 GB
      Profile:  @Minimal
   ```
2. Running `sudo list-profiles`: the current one is tagged `<- booted`.

### What is a stock profile?

Stock (built-in) profiles are clear, factory versions of profiles that are read-only and never changed by the user.
For each starting profile there is a `_stock` version (for example `@Desktop_stock`) that the profile was made from. 
Stock profiles enable users to restore a profile from a clean starting point or create a new profile.

Stock profiles have the following characteristics:

- **Can't be booted directly.** Instead, users can boot into regular profiles created from stock profiles.
- **Immutable (can't be changed).** Stock profiles are written at production time and updated as device firmware.
- **Should not be modified by the user.** Stock profiles are the base of system recovery, so users should not interact with them directly.

Flipper One has the following stock profiles (to be continued):

- `@Minimal_stock` — the parent of all other stock profiles.
- `@No_Graphics_stock`
- `@Router_stock`
- `@TV-Media-Box_stock`
- `@Desktop_stock`

### What is a snapshot?

A snapshot is a copy of a profile taken at a moment of time. Snapshots allow users to save successful configurations to reuse them later, split into multiple profiles, or run experiments with an option for an easy recovery.

Snapshots have the following characteristics:

- **Can't be booted directly.** Instead, users can restore a profile from a snapshot.
- **Immutable (can't be changed).** A snapshot keeps the filesystem state from a moment it was created.
- **Can be freely created, renamed, and deleted**. Users have full control over snapshots.
- **Can be created automatically.** Certain OS mechanisms can create snapshots before dangerous user actions.

---

### Profiles and snapshots lifecycle

```
   stock  (pristine, read-only)
     |
     |  copy
     v
   profile  (bootable, editable)   <-- this is what you use
     |
     |  take a snapshot
     v
   snapshot  (frozen backup, read-only, can't boot)
     |
     |  restore: make a new profile from it
     v
   new profile  (bootable again)
```

- **Snapshot** = save your current state, just in case.
- **New profile from a snapshot** = go back to a saved state.
- **New profile from `_stock`** = go all the way back to factory-clean.

---


### Profiles and snapshots as file system volumes

Flipper OS uses the [Btrfs file system](https://btrfs.readthedocs.io/en/latest/). Profiles, stock profiles, and snapshots are **Btrfs subvolumes**.

:::::ExpandableHeading
See the list of Btrfs subvolumes using `btrfs subvol list`

```bash
user@flipperone-a9438e:~$ sudo btrfs subvol list /
ID 256 gen 97 top level 5 path @Minimal_stock
ID 257 gen 132 top level 5 path boot
ID 258 gen 137 top level 5 path @home
ID 259 gen 115 top level 5 path @snapshots
ID 260 gen 150 top level 5 path @var-log
ID 261 gen 121 top level 5 path @var-cache
ID 262 gen 145 top level 5 path @Minimal
ID 263 gen 86 top level 5 path @Desktop_stock
ID 265 gen 93 top level 5 path @TV-Media-Box_stock
ID 266 gen 146 top level 5 path @TV-Media-Box
ID 267 gen 96 top level 5 path @Router_stock
ID 268 gen 146 top level 5 path @Router
ID 269 gen 99 top level 5 path @No-Graphics_stock
ID 270 gen 145 top level 5 path @No-Graphics
ID 271 gen 112 top level 259 path @snapshots/@Desktop_2026-07-14_10-15-16
ID 272 gen 114 top level 259 path @snapshots/@Desktop_2026-07-14_10-16-37_Desktop-before-changes
ID 273 gen 150 top level 5 path @Desktop
```
:::::

Btrfs uses copy-on-write (CoW): when a profile is created from a stock profile, or a snapshot is made from a profile, no data is duplicated on disk. Only the blocks changed later are written anew, and everything else is shared between the original and the copy. This means you can keep many profiles and snapshots without using proportionally more disk space. 

:::::ExpandableHeading
See the actual space usage with `btrfs-show-space`

The `btrfs-show-space` command shows the real footprint: the **UNIQUE** column tells you how much exclusive data each entry holds, and the **REFERENCED** column shows its total logical size including shared blocks.

```
user@flipperone-a9438e:~$ sudo btrfs-show-space
== filesystem ==
Overall:
    Device size:		  59.50GiB
    Device allocated:		   3.49GiB
    Device unallocated:		  56.01GiB
    Device missing:		     0.00B
    Device slack:		     0.00B
    Used:			   2.42GiB
    Free (estimated):		  56.86GiB	(min: 28.85GiB)
    Free (statfs, df):		  56.86GiB
    Data ratio:			      1.00
    Metadata ratio:		      2.00
    Global reserve:		   7.75MiB	(used: 0.00B)
    Multiple profiles:		        no

             Data    Metadata  System
Id Path      single  DUP       DUP      Unallocated Total    Slack
-- --------- ------- --------- -------- ----------- -------- -----
 1 /dev/sda2 2.98GiB 512.00MiB 16.00MiB    56.01GiB 59.50GiB     -
-- --------- ------- --------- -------- ----------- -------- -----
   Total     2.98GiB 256.00MiB  8.00MiB    56.01GiB 59.50GiB 0.00B
   Used      2.12GiB 153.33MiB 16.00KiB

Measuring 12 subvolume(s) (du + compsize), please wait...
== root subvolumes & snapshots ==
NAME                                                                 UNIQUE  REFERENCED       TOTAL
@snapshots/@Desktop_2026-07-14_10-15-16                                0.0B      2.0GiB      3.4GiB
@snapshots/@Desktop_2026-07-14_10-16-37_Desktop-before-changes         0.0B      2.0GiB      3.4GiB
@Desktop                                                             4.0KiB      2.0GiB      3.4GiB  <- booted
@Desktop_stock                                                      76.0KiB      2.0GiB      3.4GiB
@Minimal                                                               0.0B      1.4GiB      2.4GiB
@Minimal_stock                                                         0.0B      1.4GiB      2.4GiB
@No-Graphics                                                           0.0B      1.4GiB      2.4GiB
@No-Graphics_stock                                                     0.0B      1.4GiB      2.4GiB
@Router                                                                0.0B      1.4GiB      2.4GiB
@Router_stock                                                          0.0B      1.4GiB      2.4GiB
@TV-Media-Box                                                          0.0B      1.5GiB      2.5GiB
@TV-Media-Box_stock                                                    0.0B      1.5GiB      2.5GiB

UNIQUE     = freed if you delete that subvolume alone (uncompressed).
REFERENCED = real on-disk size, compressed; counts shared extents, so NOT additive.
TOTAL      = apparent (uncompressed).
```
:::::

### Profile-specific and shared directories

The active profile is mounted to the filesystem root (`/`). Several directories are intentionally kept outside of profiles and shared between all profiles:

- `/` — current profile (unique)
- `/boot` — bootloader data (shared)
- `/home` — user home directories (shared)
- `/var/log` — logs (shared)
- `/var/cache` — application cache (shared)

This architecture allows users to share data and preserve logs between profiles. For example, a user can reboot Flipper One to desktop mode to study logs, produced in router mode.

Switching profiles changes how the system behaves without touching `/home`, and a deleted or broken profile cannot affect any of the shared volumes.

:::::ExpandableHeading
See the mounted subvolume details using `/etc/fstab`

```bash
UUID=…  /            btrfs  defaults,compress=zstd,noatime,ssd,discard=async,x-systemd.growfs  0  0
UUID=…  /boot        btrfs  compress=zstd,noatime,ssd,discard=async,subvol=boot        0  0
UUID=…  /home        btrfs  compress=zstd,noatime,ssd,discard=async,subvol=@home       0  0
UUID=…  /var/log     btrfs  compress=zstd,noatime,ssd,discard=async,subvol=@var-log    0  0
UUID=…  /var/cache   btrfs  compress=zstd,noatime,ssd,discard=async,subvol=@var-cache  0  0
```
:::::


## CLI helper tools

Flipper OS includes profile and snapshot CLI helper tools such as `list-profiles` or `create-profile`. This guide uses them to demonstrate different scenarios with profiles and snapshots.

CLI tools are preinstalled system-wide, and you can run them from any directory. These tools need administrator rights, so you need to start each command with `sudo`. The first time you use `sudo` in a session, it asks for your password, which is normal.

Every CLI tool accepts the `-h` (`--help`) flag for a quick reminder of what it does; for example, `create-profile -h`.

---

## Usage examples

Reminder: run these with `sudo` from anywhere. Profile and snapshot names start with `@`.

### See what you have

```
sudo list-profiles

booted profile: @Desktop (id 265)

NAME                 KIND     ID   CREATED              RO  PARENT
@Desktop             profile  265  2026-07-03 12:14:21  rw  @Desktop_stock (264)       <- booted
@Desktop_stock       stock    264  2026-07-03 12:10:22  ro  @Minimal_stock (262)
@Minimal             profile  263  2026-07-03 12:10:22  rw  @Minimal_stock (262)
@Minimal_stock       stock    262  2026-07-03 12:10:22  ro  -
@Router              profile  269  2026-07-03 12:14:55  rw  @Router_stock (268)
@Router_stock        stock    268  2026-07-03 12:14:54  ro  @Minimal_stock (262)
@TV-Media-Box        profile  267  2026-07-03 12:14:54  rw  @TV-Media-Box_stock (266)
@TV-Media-Box_stock  stock    266  2026-07-03 12:14:21  ro  @Minimal_stock (262)
```
Shows every profile, which one is currently booted, and which are `stock` (pristine).

```
sudo list-snapshots

NAME                                            ID   CREATED              PARENT
@snapshots/@Desktop_2026-07-03_14-02-22_Test    272  2026-07-03 14:02:22  @Desktop (265)
@snapshots/@Desktop_2026-07-03_14-02-25         273  2026-07-03 14:02:25  @Desktop (265)
```
Shows every saved snapshot and which profile it came from.

### Check how much space things use

```
sudo btrfs-show-space

Filesystem  28.00GiB, used 6.42GiB (22%)

NAME            UNIQUE    REFERENCED  TOTAL
@Desktop        412.0MiB  3.10GiB     4.85GiB   <- booted
@Desktop_stock  0.0B      2.98GiB     4.61GiB
@Minimal        8.0MiB    1.42GiB     1.90GiB
@Minimal_stock  0.0B      1.41GiB     1.88GiB
```
Profiles and snapshots share most of their data, so they take far less room than the sizes suggest. The columns:

- **UNIQUE**: data only this one holds. This is roughly what you get back if you delete **just this one** and keep the rest.
- **REFERENCED**: its real on-disk size (compressed). Because data is shared, these don't add up across rows.
- **TOTAL**: the apparent, uncompressed size.

Add `-q` (`sudo btrfs-show-space -q`) for a faster run that skips the REFERENCED column.

### Make a save point (snapshot) before changing something

```
sudo create-snapshot Test

created @snapshots/@Desktop_2026-07-03_14-02-22_Test (read-only)
```
Freezes your current profile and labels it `Test`. Do this **before** risky changes.

```
sudo create-snapshot

created @snapshots/@Desktop_2026-07-03_14-02-25 (read-only)
```
Same thing, but auto-named with the date and time if you don't care about a label.

### Make a new profile to experiment with something new

From the **factory-clean** version:
```
sudo create-profile @Desktop_stock @DesktopTest

Create bootable profile "@DesktopTest" with a writable copy of @Desktop_stock on /dev/sda2? [y/N] y
flipper-bls: wrote entry for @DesktopTest (kernel 7.1.0-g5f8b21274ff4, slot 92)
profile '@DesktopTest' created from '@Desktop_stock' (writable, boot entry added)
reboot and pick '@DesktopTest' from the boot menu to use it
```
Creates a fresh, bootable `@DesktopTest` from the pristine Desktop. Reboot and pick it from the menu.

From your **current** Desktop (with all your changes):
```
sudo create-profile @Desktop @DesktopTest2

Create bootable profile "@DesktopTest2" with a writable copy of @Desktop on /dev/sda2? [y/N] y
flipper-bls: wrote entry for @DesktopTest2 (kernel 7.1.0-g5f8b21274ff4, slot 92)
profile '@DesktopTest2' created from '@Desktop' (writable, boot entry added)
reboot and pick '@DesktopTest2' from the boot menu to use it
```
Creates `@DesktopTest2` as a copy of Desktop as it is right now.

### Recover: make a bootable profile from a snapshot

```
sudo create-profile @snapshots/@Desktop_2026-07-03_14-02-22_Test @MyDesktop

Create bootable profile "@MyDesktop" with a writable copy of @snapshots/@Desktop_2026-07-03_14-02-22_Test on /dev/sda2? [y/N] y
flipper-bls: wrote entry for @MyDesktop (kernel 7.1.0-g5f8b21274ff4, slot 92)
profile '@MyDesktop' created from '@snapshots/@Desktop_2026-07-03_14-02-22_Test' (writable, boot entry added)
reboot and pick '@MyDesktop' from the boot menu to use it
```
Takes the frozen `Test` snapshot and turns it into a bootable profile called `@MyDesktop`. This is how you "go back" to a saved state.

### Rename a profile

```
sudo rename-profile @DesktopTest @Playground

renamed @DesktopTest -> @Playground
flipper-bls: reissued boot entry for @Playground
```
Renames the profile and updates its boot menu entry. The contents stay the same. You cannot rename the profile you are currently booted into, so boot into another one first.

### Clean up

Delete a profile you no longer need (also removes its boot menu entry):
```
sudo delete-profile @DesktopTest2

Delete profile '@DesktopTest2'? [y/N] y
deleted @DesktopTest2
removed boot entry /boot/loader/entries/92-DesktopTest2-flipperos-DesktopTest2-7.1.0-g5f8b21274ff4.conf
```

Delete a snapshot you no longer need:
```
sudo delete-snapshot @snapshots/@Desktop_2026-07-03_14-08-44_Minimal-DeleteMe

Delete restore-point snapshot '@snapshots/@Desktop_2026-07-03_14-08-44_Minimal-DeleteMe'? [y/N] y
deleted @snapshots/@Desktop_2026-07-03_14-08-44_Minimal-DeleteMe
```

Every command asks for a `y/N` confirmation first, so a typo won't wipe anything by accident. `delete-profile` asks again if the target is read-only, and a third time for a `_stock` factory base.

---

## Keep the disk healthy

`btrfs-maintenance` runs housekeeping across all your profiles and snapshots. For everyday use, `all` is the one to remember:

```
sudo btrfs-maintenance all
```
It does three things in order:

- **check**: a read-only scrub that verifies every checksum (finds silent corruption, changes nothing).
- **dedup**: reclaims space by sharing identical data between profiles and snapshots.
- **balance**: tidies partly-empty storage chunks so free space is usable again.

You can also run any one on its own: `sudo btrfs-maintenance check`, `dedup`, or `balance`. There is also `fix`, a scrub that repairs damage where a good copy exists. A full `all` can take a while on a busy disk, so run it when you don't need the device urgently.

---

## Advanced: "move" a snapshot into a profile

```
sudo create-profile -m @snapshots/@Desktop_2026-07-03_14-02-22_Test @MyDesktop2

Create bootable profile "@MyDesktop2" by MOVING @snapshots/@Desktop_2026-07-03_14-02-22_Test into it (source consumed, parent preserved) on /dev/sda2? [y/N] y
flipper-bls: wrote entry for @MyDesktop2 (kernel 7.1.0-g5f8b21274ff4, slot 92)
profile '@MyDesktop2' moved from '@snapshots/@Desktop_2026-07-03_14-02-22_Test' (writable, boot entry added)
reboot and pick '@MyDesktop2' from the boot menu to use it
(source consumed; parent_uuid preserved)
```
The `-m` flag **moves** the snapshot into the new profile instead of copying it: the snapshot is consumed (gone afterward), but its parent link is kept. Most people don't need this. It's mainly useful for incremental backup transfers (see below). If in doubt, use the normal copy above.

---

## Advanced: back up and restore to a file or USB

`send-snapshot` writes a profile or snapshot out to a file (or a folder, or straight over `ssh`); `receive-snapshot` reads it back in. This is how you keep a backup off the device.

Back up a profile to a USB stick (a read-write profile is snapshotted read-only for you first, and that restore point is kept):
```
sudo send-snapshot @Desktop /mnt/usb/
```
Restore it later, on this or another Flipper One:
```
sudo receive-snapshot /mnt/usb/Desktop_2026-07-03_14-02-22_pack.zst
```
The restored copy lands under `@snapshots` as read-only; turn it into a bootable profile with `create-profile`.

For backup chains you can send only what changed since a previous backup with `-i` (against the profile's `_stock` base) or `-p PARENT` (against a specific earlier snapshot). Incremental restores need that parent to already exist on the receiving device.

---

## Quick reference

| I want to...                       | Command                                       |
|------------------------------------|-----------------------------------------------|
| List my profiles                   | `sudo list-profiles`                          |
| List my snapshots                  | `sudo list-snapshots`                         |
| See space used per profile/snapshot| `sudo btrfs-show-space`                       |
| Save a restore point               | `sudo create-snapshot [name]`                 |
| New profile from factory-clean     | `sudo create-profile @X_stock @New`           |
| New profile from current one       | `sudo create-profile @X @New`                 |
| Restore from a snapshot            | `sudo create-profile @snapshots/... @New`     |
| Rename a profile                   | `sudo rename-profile @Old @New`               |
| Delete a profile                   | `sudo delete-profile @Name`                   |
| Delete a snapshot                  | `sudo delete-snapshot @snapshots/...`         |
| Back up to a file or USB           | `sudo send-snapshot @X /path/or/dir`          |
| Restore a backup file             | `sudo receive-snapshot <file>`                |
| Keep the disk healthy              | `sudo btrfs-maintenance all`                  |

**Rule of thumb:** snapshot before you experiment, and keep a `_stock` around as your always-safe fallback. Every tool has `-h` if you forget the arguments.
