---
title: OS profiles and snapshots
slug: cpu-software/profiles
docTags: 
createdAt: Mon Jul 14 2026 00:00:00 GMT+0000 (Coordinated Universal Time)
updatedAt: Mon Jul 14 2026 00:00:00 GMT+0000 (Coordinated Universal Time)
---

This page explains OS profiles and snapshots in Flipper OS, how to use, and how to manage them using CLI helper tools.

## Problem overview

When a Linux device is used as a multitool, in roles like a Wi-Fi router, a media box, and a desktop, it gradually accumulates installed packages, modified config files, and saved data. Eventually, the system becomes too messy to use, and the only solution is to reinstall it from scratch. With a multitool, users often need to switch between setups, save a working state before experimenting, and roll back after breaking things.

## Profiles and snapshots

Flipper OS solves the problem of a messy system using OS profiles and snapshots:

- **OS profile** is a system you can boot into and use. Profiles are changeable: each time you install new packages, change configurations, or add any other files, a profile is updated in the file system.
- **Stock snapshot** is an initial profile backup, a clean system. Stock snapshots are read-only. You can't boot a stock snapshot, but you can create a new profile from it.
- **Live snapshot** is a frozen backup of a profile. Like stock snapshot, it is read-only and not bootable.

Currently, Flipper OS uses Btrfs file system to implement the profile and snapshot functionality.

### OS profiles

Flipper OS profiles are independent Linux setups for different roles and usage scenarios. Each OS profile is a complete operating system, from kernel to desktop environment and installed apps.

You can choose an OS profile in the boot menu:

::embed[]{url="https://www.youtube.com/watch?v=oI6Vl_uoAwI"}
 
### Stock snapshots

Stock snapshots are clear Linux setups, used to initialize OS profiles. Stock snapshots act as full recovery points. You can use them to switch to a new clean profile at any time, with no need to use an external SD card or wait for the system to install.

Stock snapshots are:

- **Preloaded on the device.** Stock snapshots are instantly available on a new Flipper One.
- **Updated from a server.** New versions of stock snapshots can be downloaded from an update server.
- **Read-only.** Users can't change stock snapshot content, but can copy or delete snapshots.
- **Not bootable.** Snapshots are not shown in the boot menu and can't be booted into. Instead, a user can create a new profile from a snapshot and boot into that profile.

Flipper One has the following stock snapshots and corresponding profiles in factory configuration:

- `@Desktop_stock` → `@Desktop`
- `@Router_stock` → `@Router`
- `@TV-Media-Box_stock` → `@TV-Media-Box`
- `@Minimal_stock` → `@Minimal`
- `@No_Graphics_stock` → `@No_Graphics`

### Live snapshots

Live snapshot is a read-only OS profile copy. You can make a snapshot as a save point before a risky change. If something goes wrong, you can always return a profile to a working state. You can also save a successful configuration in a snapshot, and then create new profiles from it.

Snapshots are:

- **Created by the user.** Users can create live snapshots whenever they need a save point.
- **Read-only.** Users can't change snapshot content, but can rename, copy, or delete snapshots.
- **Not bootable.** Snapshots are not shown in the boot menu and can't be booted into. Instead, a user can create a new profile from a snapshot and boot into that profile.


### How profiles and snapshots work together

The following scheme shows a basic profile and snapshot lifecycle:

```none
   stock_profile # read-only, updated as firmware
     |
     |  copy
     v
   profile # bootable, editable  <-- this is what you use
     |
     |  take a snapshot
     v
   snapshot_at_timestamp  # read-only backup
     |
     |  restore: make a new profile from it
     v
   profile_new # again bootable and editable 
```

### Using Btrfs file system for profiles and snapshots

Flipper OS uses the [Btrfs file system](https://btrfs.readthedocs.io/en/latest/). Profiles and snapshots are **Btrfs subvolumes** mounted on the device storage.

:::::ExpandableHeading
See the list of Btrfs subvolumes using `btrfs subvol list`

```bash
$ sudo btrfs subvol list /
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

Btrfs uses copy-on-write (CoW): when a profile is created from a stock snapshot, or a snapshot is created from a profile, no data is duplicated on disk. Only the blocks changed later are written anew, and everything else is shared between the original and the copy. This means you can keep multiple profiles and snapshots without using proportionally more disk space.

:::::ExpandableHeading
See the actual space usage with `btrfs-show-space`

The `btrfs-show-space` command shows the real footprint: the **UNIQUE** column tells you how much exclusive data each entry holds, and the **REFERENCED** column shows its total logical size including shared blocks.

```bash
$ sudo btrfs-show-space
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

The active OS profile is mounted to the filesystem root (`/`). Several directories are intentionally excluded from individual profiles and shared between all profiles:

- `/` — current profile (unique)
- `/boot` — bootloader data (shared)
- `/home` — user home directories (shared)
- `/var/log` — logs (shared)
- `/var/cache` — application cache (shared)

This architecture allows users to share data and preserve logs between profiles. For example, a user can reboot Flipper One to desktop mode to study logs, produced in router mode. Switching profiles changes how the system behaves without touching `/home`, and a deleted or broken profile cannot affect any of the shared volumes.

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

## Profile and snapshot command line interface

Flipper OS includes CLI commands for OS profile and snapshot management such as `list-profiles` or `create-profile`. This page shows how to use these commands to manage profiles and snapshots. 

CLI commands are preinstalled system-wide, and you can run them from any directory. All commands need administrator rights, so you need to start each with `sudo`. The first time you use `sudo` in a session, it asks for your password, which is normal.

### CLI command quick reference

Rule of thumb: always make a snapshot before you experiment, and keep a `_stock` around as your always-safe fallback.

| I want to...                              | Command                                   |
|-------------------------------------------|-------------------------------------------|
| List existing profiles                    | `sudo list-profiles`                      |
| List existing snapshots                   | `sudo list-snapshots`                     |
| See space used per profile/snapshot       | `sudo btrfs-show-space`                   |
| Save a restore point                      | `sudo create-snapshot [name]`             |
| Create a profile from a stock snapshot    | `sudo create-profile @X_stock @New`       |
| Create a profile from the current profile | `sudo create-profile @X @New`             |
| Restore a profile from a snapshot         | `sudo create-profile @snapshots/... @New` |
| Rename a profile                          | `sudo rename-profile @Old @New`           |
| Delete a profile                          | `sudo delete-profile @Name`               |
| Delete a snapshot                         | `sudo delete-snapshot @snapshots/...`     |
| Back up to a file or USB                  | `sudo send-snapshot @X /path/or/dir`      |
| Restore a backup file                     | `sudo receive-snapshot <file>`            |
| Maintain the disk health                  | `sudo btrfs-maintenance all`              |

Each CLI command accepts the `-h` (`--help`) flag for a quick reminder of what it does; for example, `create-profile -h`.

### List existing profiles

Use `list-profiles` to view existing OS profiles, the currently booted profile, and the profile inheritance:

```bash
$ sudo list-profiles

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

Shows the profile list, which one is currently booted, and which are built-in (stock).

### Make a snapshot as a save point

You can make a snapshot as a recovery point **before** making an important change or a risky action.
The `create-snapshot` command demonstrated below creates a snapshot based on your currently booted profile:

```bash
$ sudo create-snapshot

created @snapshots/@Desktop_2026-07-03_14-02-25 (read-only)
```

You can specify the snapshot label:

```bash
$ sudo create-snapshot Test

created @snapshots/@Desktop_2026-07-03_14-02-22_Test (read-only)
```

### Recover a profile from a snapshot

The `create-profile` command takes a snapshot and turns it into a bootable profile `@MyDesktop`. This is how you "go back" to a saved state.

```bash
$ sudo create-profile @snapshots/@Desktop_2026-07-03_14-02-22_Test @MyDesktop

Create bootable profile "@MyDesktop" with a writable copy of @snapshots/@Desktop_2026-07-03_14-02-22_Test on /dev/sda2? [y/N] y
flipper-bls: wrote entry for @MyDesktop (kernel 7.1.0-g5f8b21274ff4, slot 92)
profile '@MyDesktop' created from '@snapshots/@Desktop_2026-07-03_14-02-22_Test' (writable, boot entry added)
reboot and pick '@MyDesktop' from the boot menu to use it
```

### List existing snapshots

```bash
$ sudo list-snapshots

NAME                                            ID   CREATED              PARENT
@snapshots/@Desktop_2026-07-03_14-02-22_Test    272  2026-07-03 14:02:22  @Desktop (265)
@snapshots/@Desktop_2026-07-03_14-02-25         273  2026-07-03 14:02:25  @Desktop (265)
```
Shows every saved snapshot and which profile it came from.

### Make a new profile from a stock snapshot

You can make a new profile from a stock profile using `create-profile`:

```bash
$ sudo create-profile @Desktop_stock @DesktopTest

Create bootable profile "@DesktopTest" with a writable copy of @Desktop_stock on /dev/sda2? [y/N] y
flipper-bls: wrote entry for @DesktopTest (kernel 7.1.0-g5f8b21274ff4, slot 92)
profile '@DesktopTest' created from '@Desktop_stock' (writable, boot entry added)
reboot and pick '@DesktopTest' from the boot menu to use it
```

The command above creates a fresh, bootable `@DesktopTest` from the `@Desktop_stock` profile. You can now reboot and pick `@DesktopTest` from the boot menu.

### Make a new profile from the booted profile

You can also make a new profile straight from your **currently booted** profile (keeping with all your changes):

```bash
$ sudo create-profile @Desktop @DesktopTest2

Create bootable profile "@DesktopTest2" with a writable copy of @Desktop on /dev/sda2? [y/N] y
flipper-bls: wrote entry for @DesktopTest2 (kernel 7.1.0-g5f8b21274ff4, slot 92)
profile '@DesktopTest2' created from '@Desktop' (writable, boot entry added)
reboot and pick '@DesktopTest2' from the boot menu to use it
```
Creates `@DesktopTest2` as a copy of Desktop as it is right now.

### Rename a profile

The `rename-profile` command renames the profile and updates its boot menu entry. Profile content stays unchanged. You cannot rename the profile you are currently booted into, so boot into another one first.

```bash
$ sudo rename-profile @DesktopTest @Playground

renamed @DesktopTest -> @Playground
flipper-bls: reissued boot entry for @Playground
```

### View disk space used by profiles and snapshots

```bash
$ sudo btrfs-show-space

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


### Delete a profile or snapshot

Use `delete-profile` to delete a profile and remove it from the boot menu:

```bash
# sudo delete-profile @DesktopTest2

Delete profile '@DesktopTest2'? [y/N] y
deleted @DesktopTest2
removed boot entry /boot/loader/entries/92-DesktopTest2-flipperos-DesktopTest2-7.1.0-g5f8b21274ff4.conf
```

Use `delete-snapshot` to delete a snapshot you no longer need:

```bash
$ sudo delete-snapshot @snapshots/@Desktop_2026-07-03_14-08-44_Minimal-DeleteMe

Delete restore-point snapshot '@snapshots/@Desktop_2026-07-03_14-08-44_Minimal-DeleteMe'? [y/N] y
deleted @snapshots/@Desktop_2026-07-03_14-08-44_Minimal-DeleteMe
```

Each command asks for a `y/N` confirmation first, so a typo won't wipe anything by accident. You will need to confirm twice to delete a read-only target, and three times to delete a stock snapshot.

---

### Maintain the disk health

`btrfs-maintenance` runs housekeeping across all your profiles and snapshots. For everyday maintenance, use the `all` parameter:

```bash
sudo btrfs-maintenance all
```

This command does three actions in the following order:

- **check**: a read-only scrub that verifies every checksum (finds silent corruption, changes nothing).
- **dedup**: reclaims space by sharing identical data between profiles and snapshots.
- **balance**: tidies partly-empty storage chunks so free space is usable again.

You can also run any action on its own: `sudo btrfs-maintenance check`, `dedup`, or `balance`. There is also the `fix` action, a scrub that repairs damage where a good copy exists. The full `btrfs-maintenance all` call can take a while on a busy disk, so it's best to run it when you don't need the device urgently.

---

### Advanced: "move" a snapshot into a profile

The `create-profile -m` command **moves** the snapshot into the new profile instead of copying it: the snapshot is consumed (gone afterward), but its parent link is kept. Most people don't need this. It's mainly useful for incremental backup transfers (see below). If in doubt, use the normal copy above.

```bash
$ sudo create-profile -m @snapshots/@Desktop_2026-07-03_14-02-22_Test @MyDesktop2

Create bootable profile "@MyDesktop2" by MOVING @snapshots/@Desktop_2026-07-03_14-02-22_Test into it (source consumed, parent preserved) on /dev/sda2? [y/N] y
flipper-bls: wrote entry for @MyDesktop2 (kernel 7.1.0-g5f8b21274ff4, slot 92)
profile '@MyDesktop2' moved from '@snapshots/@Desktop_2026-07-03_14-02-22_Test' (writable, boot entry added)
reboot and pick '@MyDesktop2' from the boot menu to use it
(source consumed; parent_uuid preserved)
```
---

### Advanced: back up and restore profile to a file or USB

You can keep your profiles and snapshots backed up off the device:

- The `send-snapshot` command writes a profile or snapshot out to a file (or a folder, or straight over `ssh`).
- The `receive-snapshot` command reads a profile or snapshot back in.

Back up a profile to a USB stick (a read-write profile is snapshotted read-only for you first, and that restore point is kept):

```bash
sudo send-snapshot @Desktop /mnt/usb/
```

Restore it later, on this or another Flipper One:

```bash
sudo receive-snapshot /mnt/usb/Desktop_2026-07-03_14-02-22_pack.zst
```

The restored copy lands under `@snapshots` as read-only; turn it into a bootable profile with `create-profile`.

For backup chains you can send only what changed since a previous backup with `-i` (against the profile's `_stock` base) or `-p PARENT` (against a specific earlier snapshot). Incremental restores need that parent to already exist on the receiving device.
