---
title: About Linux (CPU Software)
slug: cpu-software/about
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:34:10 GMT+0000 (Coordinated Universal Time)
---

This page explains the structure of the CPU Software sub-project, provides links to all the repositories and explains how they uses to build the official Flipper One's Linux operating system.

The CPU Software sub-project consists of:

- ✅ [Task tracker](https://github.com/orgs/flipperdevices/projects/11)
- 🏭 [OS images build server](https://linux-images.flipp.dev/)
- 📁 GitHub repositories:
  - [Linux build scripts](https://github.com/flipperdevices/flipperone-linux-build-scripts)
  - [Rkbin](https://github.com/flipperdevices/rkbin)
  - [U-Boot](https://github.com/flipperdevices/flipperone-linux-build-scripts)
  - [Linux kernel](https://github.com/flipperdevices/flipper-linux-kernel)
  - [rkloader](https://github.com/flipperdevices/rkloader) & [gofastboot](https://github.com/flipperdevices/gofastboot)

We'd love your feedback — look for tasks tagged **help wanted** in the task tracker, or contribute directly to the GitHub repositories via pull requests.

![CPU software subproject structure](/files/pics/cpu-software-subproject-structure.jpg)

***

## ✅  Tasks tracker

All Linux (CPU Software) team tasks are tracked in the GitHub project [Flipper One — Linux (CPU Software)](https://github.com/orgs/flipperdevices/projects/11/). There, you can see what the engineering team is working on and follow progress and discussions.

**\<TODO: Task tracker screenshot with collouts)>**

**Some tasks are open** to the community and marked with a **help wanted** label. You’re welcome to join the discussion on these tasks or submit your design proposals — just make sure to read the [Contribution guide]() first.

***

## 🏭 OS images build server

Our official OS image build server automatically builds a new OS image whenever changes are made to any of the GitHub repositories included in the build process. You can monitor the build status in the [server’s web interface](https://linux-images.flipp.dev/).

![](/files/pics/os-buildbot.png)

Once the build succeeds, full-disk images for all supported RK3576-based boards listed under [supported boards](Supported-boards.md) are published on the [web server](), where they can be downloaded.

![](/files/pics/os-build-list.png)

More details about the build system architecture and how to build the image locally are available on the [Build system](Build-system.md) page.

Instructions for installing a full-disk OS image on a board are available on the [How to install an image](How-to-install-an-image.md) page.

***

## 📁 GitHub repositories

This subproject includes several public GitHub repositories containing Linux OS components and flashing tools:

- [Linux build scripts](https://github.com/flipperdevices/flipperone-linux-build-scripts) — Linux OS image build scripts for supported RK3576-based boards. These scripts can be used to build the OS image locally and are also used by the official OS image build server to produce release images.
- [Rkbin](https://github.com/flipperdevices/rkbin) — Rockchip RK3576 binaries, including DDR trainer and internal storage access binaries in MaskROM mode.
- [U-Boot](https://github.com/flipperdevices/flipperone-linux-build-scripts) — Mirror of the official U-Boot bootloader sources with RK3576-specific patches not in mainline yet.
- [Linux kernel](https://github.com/flipperdevices/flipper-linux-kernel) — Our fork of the most recent release by Linus Torvalds with patches not in mainline yet.
- [rkloader](https://github.com/flipperdevices/rkloader) & [gofastboot](https://github.com/flipperdevices/gofastboot) — Go tools for flashing images to Rockchip devices via fastboot protocol.

***

# How to contribute

:::hint{type="info"}
To contribute to the Linux (CPU Software) sub-project, you need to have a GitHub account. You can create one on the [GitHub website](https://github.com/signup).
:::

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/EcotI__FOd58IUCUyNzqC-20260420-091800.jpg)

Anyone can contribute to the Linux (CPU Software) sub-project via the GitHub repository by commenting on the open tasks or making pull requests with suggested changes:

- :Link[Comment on an open task]{label="Comment on an open task" overridedLabel="Comment on an open task" spaceId docId="BDmPLCYR-Sy0560CBHiL_" version="v2" docAnchorId="#comment-on-an-open-task" loadingMethod="dynamic" newTab="false" href="About-CPU-Software.md"}
- :Link[Contribute via a pull request]{label="Contribute via a pull request" overridedLabel="Contribute via a pull request" spaceId docId="BDmPLCYR-Sy0560CBHiL_" version="v2" docAnchorId="#share-a-new-design-as-a-pull-request" loadingMethod="dynamic" newTab="false" href="About-CPU-Software.md"}

***

## Comment on an open task

::::hint{type="info"}
**⚠️ Contributions only — no flooding**

To keep collaboration productive, please keep comments on-topic. Open tasks are for contribution-related discussion only. If you have an idea or concern, first turn it into a concrete contribution and share it as a comment on a task. For general questions or discussions, you’re always welcome to join the conversation on :Link[social media]{href="https://x.com/Flipper_RND" newTab="true" hasDisabledNofollow="false"} or :Link[Discord]{href="https://discord.com/invite/flipper" newTab="true" hasDisabledNofollow="false"}!

:::Paragraph{indent="1"}
**Bad vs good comments:**
:::

:::Paragraph{indent="1"}
❌ — I like the green button instead of the orange one
👍 — I think the green button works better. Here's an example I made: `mypicture.jpg`&#x20;
:::
::::

Open tasks that need the community's help are labeled **help wanted**. If you have ideas on how to improve the design, you can contribute by commenting on the task and attaching screenshots, videos, or links:

::::WorkflowBlock
:::WorkflowBlockItem
In the :Link[Linux (CPU Software) GitHub project]{href="https://github.com/orgs/flipperdevices/projects/11" newTab="true" hasDisabledNofollow="false"}, click the open task you want to contribute to.
:::

:::WorkflowBlockItem
In the comments section, clearly write your comment and attach a screenshot, video, or provide a link.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/jnEqEalHspW_JJ2Suz3SU-20260325-175922.png)

**Attachment size limit:**

- Images: 10 MB
- Videos: 100 MB
:::

:::WorkflowBlockItem
Click **Comment**.
:::
::::

We review all ideas carefully! We may ask additional questions about your idea in the task thread, so please follow notifications from GitHub in your email.

***

## Contribute via a pull request

Contributing via pull requests allows anyone to propose changes to the components of our Linux OS. Once a PR is merged, your changes become part of the official OS builds.

To contribute to OS components:

1. Clone the [Linux build scripts](https://github.com/flipperdevices/flipperone-linux-build-scripts) repository. During the build process, these scripts also clone several other repositories (see the [Build system](Build-system.md) page for details on the architecture).
2. Fork and clone locally the repositories involved in the build process that you want to modify.
3. Edit your local copy of build scripts so they use your local repositories clones instead of cloning the remote ones you are modifying.
4. Make your changes in the forked repositories.
5. Build the OS image with your changes locally. Learn more in the :Link[Local build of the OS]{label="Local build of the OS" overridedLabel="Local build of the OS" spaceId docId="isVWIRz7zz0jE7gRAHigs" version="v2" docAnchorId="#local-build-of-the-os" loadingMethod="dynamic" newTab="false" githubPath="Build-system.md#local-build-of-the-os" href="Build-system.md"} section.
6. Flash the OS image to an RK3576-based board and test your changes.
7. Create and submit pull requests to all affected repositories.

We review all ideas carefully! We may ask additional questions about your pull requests in the thread, so please follow notifications from GitHub in your email.
