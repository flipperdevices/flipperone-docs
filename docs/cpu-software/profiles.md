---
title: OS profiles and snapshots
slug: cpu-software/profiles
docTags: 
createdAt: Mon Jul 14 2026 00:00:00 GMT+0000 (Coordinated Universal Time)
updatedAt: Mon Jul 14 2026 00:00:00 GMT+0000 (Coordinated Universal Time)
---
# Flipper One: Profiles & Snapshots

## Before you start

The helper tools are installed system-wide, so you can run them from anywhere. There is no folder to change into and no leading `./`: each one is a plain command like `list-profiles` or `create-profile`.

All of them need administrator rights, so start each command with `sudo`. The first time you use `sudo` in a session it asks for your password, which is normal.

Every tool also accepts `-h` (or `--help`) if you want a quick reminder of what it does, for example `create-profile -h`.

---

## The two ideas in one line

- **Profile**: a system you can **boot into and use**. You can change it.
- **Snapshot**: a **frozen backup** of a profile. You can't boot it, but you can restore from it.

That's the whole thing. The rest is just examples.

---

## What is a Profile?

Think of a profile like a separate "computer setup" on your Flipper One. At startup you get a boot menu and pick the one you want: Desktop, Router, TV Media Box, No Graphics, and so on. Each profile:

- **Can be booted** (it shows up in the boot menu).
- **Can be changed**: install apps, tweak settings, break things. It's yours.
- **Remembers your changes** between reboots.

You can have several profiles side by side and switch between them just by rebooting.

**Stock profiles.** Next to each profile there's often a `_stock` version (for example `@Desktop_stock`). That's the **pristine, factory version**: read-only, never touched. It exists so you can always go back to a clean starting point if your working profile gets messed up.

**Which profile am I in right now?** Two easy ways to check:

1. The welcome banner shown when you log in, on the `Profile:` line:
   ```
   Welcome to FlipperOne
      Board:    one-rev-f0b0c1
      Memory:   7.8 GB
      Profile:  @Minimal
   ```
2. Running `sudo list-profiles`: the current one is tagged `<- booted`.

---

## What is a Snapshot?

Think of a snapshot like a **photo** of a profile taken at one moment, or a "save point" in a game. A snapshot:

- **Is frozen (read-only)**: nothing can change it.
- **Cannot be booted directly.** It's a backup, not a system to run.
- **Is your safety net.** Take one before doing something risky. If it goes wrong, you restore from it.

To actually *use* a snapshot, you turn it into a profile (see the examples). Then it becomes bootable again.

---

## How they fit together

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

### Try something new, safely (make a new profile)

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
