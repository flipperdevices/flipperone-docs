---
title: Profiles CLI
slug: cpu-software/profiles
docTags: 
createdAt: Mon Jul 14 2026 00:00:00 GMT+0000 (Coordinated Universal Time)
updatedAt: Thu Aug 13 2026 12:00:00 GMT+0000 (Coordinated Universal Time)
---

This page is a command-line reference for managing OS profiles in Flipper OS. For what OS profiles are, and why Flipper OS uses them, see [Flipper OS](Flipper-OS.md).

## Concepts

An OS profile is an isolated system you can boot into and use: install new packages with `apt`, change config files, and do whatever you want with it. A profile contains a Linux kernel and a `/` root directory, including the desktop environment, installed packages, and configuration files. Every profile is fully writable and bootable — there's no separate read-only or non-bootable state.

Internally, Flipper OS uses [Btrfs](https://btrfs.readthedocs.io/en/latest/) to implement OS profiles and the common boot menu.

### System profiles

System profiles are the official, preinstalled profiles, such as `Desktop`, `Router`, `TV-Media-Box`, `Minimal`, and `No-Graphics`. You can reset a system profile to its original default state at any time, discarding any modifications you've made to it.

### User profiles

A user profile is a profile you create by cloning a system profile or another user profile. In the boot menu, user profiles are shown with their name in square brackets, e.g. `[MyTravelRouter]`, to distinguish them from system profiles — at the command-line level, they're referenced by their plain `@Name`, same as system profiles. See [Cloning and sharing profiles](Flipper-OS.md#cloning-and-sharing-profiles) for the concept.

### Disk space usage

Flipper OS uses [Btrfs](https://btrfs.readthedocs.io/en/latest/), which is a copy-on-write (CoW) file system. When you clone a profile, no data is duplicated on disk, so no extra space is consumed. When you make changes in a profile, only the changed blocks are written anew, and everything else is shared between the original and the copy. This means you can keep multiple profiles without using proportionally more disk space.

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

Measuring 6 subvolume(s) (du + compsize), please wait...
== root subvolumes ==
NAME                 UNIQUE   REFERENCED  TOTAL
@Desktop              4.0KiB  2.0GiB      3.4GiB  <- booted
@Minimal                0.0B  1.4GiB      2.4GiB
@No-Graphics             0.0B  1.4GiB      2.4GiB
@Router                  0.0B  1.4GiB      2.4GiB
@TV-Media-Box            0.0B  1.5GiB      2.5GiB
@MyTravelRouter      120.0KiB  1.5GiB      2.5GiB

UNIQUE     = freed if you delete that subvolume alone (uncompressed).
REFERENCED = real on-disk size, compressed; counts shared extents, so NOT additive.
TOTAL      = apparent (uncompressed).
```
:::::

## Profile CLI

You can create, clone, reset, and manage profiles using the command line interface (CLI) from any Flipper OS profile.
The CLI commands are included in the Flipper OS distribution and instantly available on Flipper One.

CLI commands are preinstalled system-wide, and you can run them from any directory. All commands need administrator rights, so you need to start each with `sudo`. The first time you use `sudo` in a session, it asks for your password, which is normal.

### CLI command quick reference

| I want to...                                | Command                          |
|----------------------------------------------|-----------------------------------|
| List existing profiles                       | `sudo list-profiles`             |
| See space used per profile                   | `sudo btrfs-show-space`          |
| Create a user profile from a system profile   | `sudo create-profile @X @New`    |
| Create a user profile from the booted profile | `sudo create-profile @X @New`    |
| Reset a system profile to its default state   | `sudo reset-profile @Name`       |
| Rename a user profile                         | `sudo rename-profile @Old @New`  |
| Delete a user profile                         | `sudo delete-profile @Name`      |
| Back up a profile to a file or USB            | `sudo send-profile @X /path/or/dir` |
| Restore a profile from a backup file          | `sudo receive-profile <file> @New` |
| Maintain the disk health                      | `sudo btrfs-maintenance all`     |

Rule of thumb: clone a system profile into a user profile before you experiment, and use `reset-profile` any time you want a system profile back to its factory state.

Each CLI command accepts the `-h` (`--help`) flag for a quick reminder of what it does; for example, `create-profile -h`.

### List existing profiles

Use `list-profiles` to view existing OS profiles, the currently booted profile, and which profile each user profile was cloned from:

```bash
$ sudo list-profiles

booted profile: @Desktop (id 265)

NAME              KIND    ID   CREATED              PARENT
@Desktop          system  265  2026-07-03 12:14:21  -              <- booted
@Minimal          system  262  2026-07-03 12:10:22  -
@Router           system  268  2026-07-03 12:14:55  -
@TV-Media-Box     system  266  2026-07-03 12:14:54  -
@MyTravelRouter   user    271  2026-07-03 14:20:10  @Router (268)
```

Shows the profile list, which one is currently booted, and which are built-in system profiles versus user profiles.

### Make a new user profile from a system profile

You can make a new user profile from a system profile using `create-profile`:

```bash
$ sudo create-profile @Router @MyTravelRouter

Create profile "@MyTravelRouter" as a writable copy of @Router? [y/N] y
flipper-bls: wrote entry for @MyTravelRouter (kernel 7.1.0-g5f8b21274ff4, slot 92)
profile '@MyTravelRouter' created from '@Router' (boot entry added)
reboot and pick '[MyTravelRouter]' from the boot menu to use it
```

The command above creates a fresh, bootable `@MyTravelRouter` from the `@Router` system profile. In the boot menu, it appears as `[MyTravelRouter]`.

### Make a new user profile from the booted profile

You can also make a new user profile straight from your **currently booted** profile (including all your changes):

```bash
$ sudo create-profile @Desktop @DesktopTest

Create profile "@DesktopTest" as a writable copy of @Desktop? [y/N] y
flipper-bls: wrote entry for @DesktopTest (kernel 7.1.0-g5f8b21274ff4, slot 92)
profile '@DesktopTest' created from '@Desktop' (boot entry added)
reboot and pick '[DesktopTest]' from the boot menu to use it
```
Creates `@DesktopTest` as a copy of Desktop as it is right now.

### Reset a profile to its default state

Use `reset-profile` to discard all modifications made to a system profile and return it to its original, preconfigured state. Only system profiles can be reset this way — a user profile has no separate default state, so if you want a clean slate, clone a fresh one from a system profile instead.

```bash
$ sudo reset-profile @Router

Reset profile "@Router" to its default state? All modifications will be lost. [y/N] y
flipper-bls: reissued boot entry for @Router (kernel 7.1.0-g5f8b21274ff4, slot 92)
profile '@Router' reset to its default state
```

### Rename a profile

The `rename-profile` command renames a user profile and updates its boot menu entry. Profile content stays unchanged. You cannot rename a system profile, or the profile you are currently booted into — boot into another one first.

```bash
$ sudo rename-profile @MyTravelRouter @Playground

renamed @MyTravelRouter -> @Playground
flipper-bls: reissued boot entry for @Playground
```

### View disk space used by profiles

```bash
$ sudo btrfs-show-space

Filesystem  28.00GiB, used 6.42GiB (22%)

NAME              UNIQUE    REFERENCED  TOTAL
@Desktop          412.0MiB  3.10GiB     4.85GiB   <- booted
@Router           8.0MiB    1.42GiB     1.90GiB
@MyTravelRouter   120.0MiB  1.50GiB     1.95GiB
```
Profiles share most of their data, so they take far less room than the sizes suggest. The columns:

- **UNIQUE**: data only this one holds. This is roughly what you get back if you delete **just this one** and keep the rest.
- **REFERENCED**: its real on-disk size (compressed). Because data is shared, these don't add up across rows.
- **TOTAL**: the apparent, uncompressed size.

Add `-q` (`sudo btrfs-show-space -q`) for a faster run that skips the REFERENCED column.


### Delete a profile

Use `delete-profile` to delete a user profile and remove it from the boot menu. System profiles cannot be deleted, only reset.

```bash
# sudo delete-profile @DesktopTest

Delete profile '@DesktopTest'? [y/N] y
deleted @DesktopTest
removed boot entry /boot/loader/entries/92-DesktopTest-flipperos-DesktopTest-7.1.0-g5f8b21274ff4.conf
```

Each command asks for a `y/N` confirmation first, so a typo won't wipe anything by accident.

---

### Maintain the disk health

`btrfs-maintenance` runs housekeeping across all your profiles. For everyday maintenance, use the `all` parameter:

```bash
sudo btrfs-maintenance all
```

This command does three actions in the following order:

- **check**: a read-only scrub that verifies every checksum (finds silent corruption, changes nothing).
- **dedup**: reclaims space by sharing identical data between profiles.
- **balance**: tidies partly-empty storage chunks so free space is usable again.

You can also run any action on its own: `sudo btrfs-maintenance check`, `dedup`, or `balance`. There is also the `fix` action, a scrub that repairs damage where a good copy exists. The full `btrfs-maintenance all` call can take a while on a busy disk, so it's best to run it when you don't need the device urgently.

---

### Advanced: back up and restore a profile to a file or USB

You can keep your profiles backed up off the device:

- The `send-profile` command writes a profile out to a file (or a folder, or straight over `ssh`).
- The `receive-profile` command reads a profile back in as a new profile.

Back up a profile to a USB stick:

```bash
sudo send-profile @Desktop /mnt/usb/
```

Restore it later, on this or another Flipper One, as a new profile:

```bash
sudo receive-profile /mnt/usb/Desktop_2026-07-03_14-02-22_pack.zst @DesktopRestored
```

The restored profile is immediately bootable — pick it from the boot menu.

## Explanation

### Subvolume mounting

Each profile's root is a separate subvolume mounted to the filesystem root (`/`). A special `boot` subvolume mounted to `/boot` contains Linux kernels and boot configuration for all profiles. The `/boot` directory is also shared; however, there is an isolated kernel for each OS profile.

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

:::::ExpandableHeading

See the list of Btrfs subvolumes using `btrfs subvol list`

```bash
$ sudo btrfs subvol list /
ID 256 gen 97 top level 5 path @Minimal
ID 257 gen 132 top level 5 path boot
ID 258 gen 137 top level 5 path @home
ID 259 gen 150 top level 5 path @var-log
ID 260 gen 121 top level 5 path @var-cache
ID 263 gen 86 top level 5 path @Desktop
ID 265 gen 93 top level 5 path @TV-Media-Box
ID 267 gen 96 top level 5 path @Router
ID 269 gen 99 top level 5 path @No-Graphics
ID 271 gen 150 top level 5 path @MyTravelRouter
```
:::::
