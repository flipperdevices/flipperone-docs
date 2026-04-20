---
title: How to join
docTags: 
createdAt: Tue Apr 14 2026 15:08:14 GMT+0000 (Coordinated Universal Time)
updatedAt: Mon Apr 20 2026 09:27:36 GMT+0000 (Coordinated Universal Time)
---

### Guide for the community on how to join Flipper One development

This page explains the overall structure of the Flipper One project, the sub-projects it consists of, and how you can contribute to its development.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/4tZetne1wIOtQsoxMFYEa-20260316-183949.jpg)

Flipper One is currently in active development. As a community-driven project, we’ve made the entire development process open — so you can see how things are built and even take part in shaping Flipper One’s future.

***

# Sub-projects structure of Flipper One

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/Ni-ecnmssC6fq6QyQzSkg-20260410-162751.jpg)

Flipper One is a large and complex project, divided into several sub-projects. Each sub-project is managed by a dedicated Flipper team, with its own structure, rules, and workflows. This Developer Portal acts as a wiki and the main entry point into all sub-projects, hosting their documentation and contribution guides.

**Currently, we have the following sub-projects:**

::::VerticalSplit{layout="left"}
:::VerticalSplitItem
### :Link[Hardware]{href="https://docs.flipper.net/one/about-hardware" newTab="true" hasDisabledNofollow="false"}

::Image[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/9plDPlgbxscoFIacbj8Q9-20260331-093234.png" size="38" width="333" height="243" position="flex-start"}
:::

:::VerticalSplitItem
Electrical hardware development. This is where the printed circuit boards (PCBs), antennas, and everything related to the electrical connections of chips, connectors, and processors are designed. The Hardware team works closely with the Mechanics team to ensure the electronics are compatible with the enclosure. :Link[**Learn more**]{href="https://docs.flipper.net/one/about-hardware" newTab="true" hasDisabledNofollow="false"}**&#x20;→**
:::
::::

***

::::VerticalSplit{layout="left"}
:::VerticalSplitItem
### :Link[Mechanics]{href="https://docs.flipper.net/one/about-mechanics" newTab="true" hasDisabledNofollow="false"}

::Image[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/C5VLSGhfaLWBS5E3VIMF8-20260331-093258.png" size="50" width="357" height="333" position="flex-start"}
:::

:::VerticalSplitItem
Mechanical and industrial design. This is where the enclosure, buttons, plastic and metal parts, and mounting components are designed. Everything the user physically interacts with. Many mechanical tasks are tightly coupled with the Hardware team. :Link[**Learn more**]{href="https://docs.flipper.net/one/about-mechanics" newTab="true" hasDisabledNofollow="false"}**&#x20;→**
:::
::::

***

::::VerticalSplit{layout="left"}
:::VerticalSplitItem
### :Link[Linux (CPU Software)]{href="https://docs.flipper.net/one/about-linux-cpu-software" newTab="true" hasDisabledNofollow="false"}

::Image[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/ELzD0IezeYIDXuYC1yP2a-20260331-093341.png" size="34" width="267" height="318" position="flex-start"}
:::

:::VerticalSplitItem
Linux kernel, modules, drivers, userspace, bootloader, Rockchip tools, etc. This is the largest and most complex sub-project, spanning many repositories. It contains the core software that users will interact with directly. [**Learn more**](https://docs.flipper.net/one/about-linux-cpu-software) **→**
:::
::::

***

::::VerticalSplit{layout="left"}
:::VerticalSplitItem
### :Link[MCU Firmware]{href="https://docs.flipper.net/one/about-mcu-firmware" newTab="true" hasDisabledNofollow="false"}

::Image[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/On5sGCZ3-QWo2sYbRVTam-20260331-093415.png" size="38" width="309" height="306" position="flex-start"}
:::

:::VerticalSplitItem
Firmware for the RP2350 microcontroller. The MCU controls buttons, display, touchpad, and power subsystem, as well as co-processor communication between the MCU and CPU. [**Learn more**](https://docs.flipper.net/one/about-mcu-firmware)**&#x20;→**
:::
::::

***

::::VerticalSplit{layout="left"}
:::VerticalSplitItem
### :Link[User Interface]{href="https://docs.flipper.net/one/about-user-interface" newTab="true" hasDisabledNofollow="false"}

::Image[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/CzLfRFqDmQf-g_0Mu_WA--20260331-093442.png" size="36" width="282" height="273" position="flex-start"}
:::

:::VerticalSplitItem
UI/UX development. This is where the user interface, visual communication of the device, all graphics, and visual design are developed. [**Learn more**](https://docs.flipper.net/one/about-user-interface) **→**
:::
::::

***

::::VerticalSplit{layout="left"}
:::VerticalSplitItem
### :Link[Docs]{href="https://docs.flipper.net/one/about-docs" newTab="true" hasDisabledNofollow="false"}

::Image[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/RfUa81BVRdDm1qKCoXnrd-20260331-093508.png" size="36" width="273" height="273" position="flex-start"}
:::

:::VerticalSplitItem
Developer portal wiki, technical docs, guides, and datasheets. All documentation — including this wiki — is developed here. It covers both the Flipper One product documentation and descriptions of development processes and contribution guides. [**Learn more**](https://docs.flipper.net/one/about-docs)**&#x20;→**
:::
::::

***

::::VerticalSplit{layout="left"}
:::VerticalSplitItem
### [**Testing**](https://docs.flipper.net/one/testing-overview)

::Image[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/M8o8dC4criD5llKbqSJB6-20260331-093535.png" size="36" width="282" height="273" position="flex-start"}
:::

:::VerticalSplitItem
Tools for testing device subsystems and hardware validation. Includes various scripts and programs for testing power, networking, CPU, audio, graphics, etc. Also includes interface prototypes demos and sample audio and video files. [**Learn more**](https://docs.flipper.net/one/about-testing) **→**
:::
::::

***

# Inside a sub-project

A sub-project within the Flipper One project is a collection of entities used by the development team. Each sub-project includes at least three types of entities:

- 📚 **Documentation** — explains the sub-project structure, provides an overview of assets and platforms, and contribution guidelines.
- ✅ **Task tracker&#x20;**— used to track and discuss tasks, including those where the community can help.
- 📁 **Assets & platforms&#x20;**— includes source code, files, firmware builds, 3D models, UI mockups, images, and APIs available for community review and contribution.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/R-x3IVDbaRqBT2povHK4i-20260410-164947.jpg)

## 📚 Documentation

Each sub-project is different, so it has its own documentation explaining how it is organized and how it works. You can access this documentation through the Flipper One Developer Portal (this wiki) or in the README file of the sub-project’s GitHub repository.

Documentation usually includes:

- An overview of the sub-project structure
- Task tracker rules
- Contribution guidelines

For those who want to explore further, some sub-projects provide more in-depth materials, such as datasheets, test results, logs, and design guides.

:::hint{type="info"}
**You can contribute to the documentation**

This wiki is a sub-project of its own, and anyone can contribute by editing :Link[its source files on GitHub]{href="https://github.com/flipperdevices/flipperone-docs" newTab="true" hasDisabledNofollow="false"}. Learn more in the **Docs sub-project**.
:::

## ✅ Task tracker

Tasks for each sub-project are managed in a task tracker — a Kanban board on GitHub. Each task on the board is a GitHub issue from the sub-project repository. You can view :Link[all task trackers on GitHub]{href="https://github.com/orgs/flipperdevices/projects" newTab="true" hasDisabledNofollow="false"}.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/mcpZH-vu_oT0W5RG7ft-X-20260410-160905.png "Each Sub-project has its own Kanban board on GitHub")

### What’s the difference between GitHub issues and task tracker issues?

There’s no difference. The task tracker simply organizes the existing GitHub issues into a Kanban board. It also allows issues from different repositories to be grouped together in one place and managed as a single large task with sub-tasks.

For example, here is a :Link[list of GitHub issues]{href="https://github.com/flipperdevices/flipperone-mcu-firmware/issues" newTab="true" hasDisabledNofollow="false"} from the MCU Firmware sub-project and :Link[how they are organized on the Kanban board]{href="https://github.com/orgs/flipperdevices/projects/8" newTab="true" hasDisabledNofollow="false"}.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/QoPhF9YoGDfIllcZR8_5p-20260410-161735.jpg "Task tracker is a Kanban-style view of standard GitHub issues")

### Open tasks

Some of our tasks are open. This means the community can interact with them just as they would with any issue in a classic GitHub repository — leaving comments, attaching files, and so on. Each task includes a short title and a detailed description, often with links and screenshots to help you understand it.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/HfxrhnxuYaoQidaQHad-F-20260410-163206.jpg "Example of an open task in MCU Firmware sub-project")

Tasks can be marked with different **labels**:

- **help wanted** — tasks where we actively invite the community to participate and contribute to the solution. Example: [**Operating modes discussion**](https://github.com/flipperdevices/flipperone-ui/issues/1)
- **locked** — tasks that are closed to the community. This means we are not ready to discuss the task or accept feedback. You can still see Flipper team’s internal discussions.

::::hint{type="info"}
### ⚠️ Contributions only — no flooding

To keep collaboration productive, please keep comments on-topic. Open tasks are for contribution-related discussion only. If you have an idea or concern, first turn it into a concrete contribution and share it as a comment on a task. For general questions or discussions, you’re always welcome to join the conversation on :Link[social media]{href="https://x.com/Flipper_RND" newTab="true" hasDisabledNofollow="false"} or :Link[Discord]{href="https://discord.com/invite/flipper" newTab="true" hasDisabledNofollow="false"}!

:::Paragraph{indent="1"}
**Bad vs good comments:**
:::

:::Paragraph{indent="1"}
❌ — I like the green button instead of the orange one
👍 — I think the green button works better. Here's an example I made: `mypicture.jpg`&#x20;
:::
::::

***

## 📁 Assets & Platforms

Sub-projects may include various assets and platforms for the community to explore. Depending on the sub-project, these can include source code repositories, design files, 3D models, schematics, UI mockups, and more.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/5ApX8dgchRVvlbsStllFd-20260410-164009.jpg)

You can view, download, and edit the assets, as well as share your feedback with us. However, each of the Flipper teams defines its own contribution steps — make sure to review them before contributing. You can find contribution guides on the sub-project page.

***

# How to start

Feel free to jump in — you can contribute by joining task discussions, sharing ideas, asking questions, or suggesting improvements. If you have feedback or notice something that could be better, your input is always welcome.

## Step 1. Read the sub-project docs

Find a sub-project that interests you. Explore its documentation in this Developer Portal to understand how it works, how it’s structured, and how you can contribute.

## Step 2. Check the task tracker

Go to the task tracker of the sub-project you’re interested in to explore current tasks. Open Tasks where your help is welcome are labeled **help wanted**. Read through a task and follow the contribution guidelines when submitting your input.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/ZWucCsRvdOhYn-Og3KwFF-20260410-165617.png "Task where community contribution is welcome are marked \"help wanted")

:::hint{type="info"}
You can also visit the :Link[🚧 Open tasks]{href="https://docs.flipper.net/one/open-tasks" newTab="true" hasDisabledNofollow="false"} to find tasks that need community help or feedback.
:::

## Step 3. Join discussions in our socials

Follow us on X and join our Discord server to hang out, ask questions, and connect with other contributors.

::::LinkArray{contentSource="CUSTOM"}
:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/O5IbFQ7KAuHJE_lqbKbNX-20260401-145400.jpg"}
:Link[X.com/Flipper\_RND]{href="https://x.com/Flipper_RND" newTab="true" hasDisabledNofollow="false"}

Follow updates and project announcements on X.com
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://app.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/doVC8Airf2_FH2IwVxxAV_monosnap-miro-2023-04-13-19-25-16.png"}
:Link[Flipper Devices Discord]{href="https://discord.com/invite/flipper" newTab="true" hasDisabledNofollow="false"}

Chat with the community and Flipper team on our Discord server
:::
::::

## Step 4. Subscribe to our weekly digest

Each week, we'll share a quick update on how things are coming along and flag any areas where extra help would be welcome. No pressure to jump in right away — you might just spot something in a future update that catches your eye!

:::hint{type="info"}
⚠️ **Nerds Warning**: this is a developer-focused, highly technical newsletter.
:::

:::Iframe{code="<iframe width=&#x22;540&#x22; height=&#x22;750&#x22; src=&#x22;https://183c2432.sibforms.com/serve/MUIFAAgzua23MvPHbQJyGmSkqAwomY_d-OtcEmQJaZ90xXKQQ_70E5jmVi97OFh-kF6NR69IL74D7n6ieCsJTlnda6j8F0RncbcEgx2_tiYW6qISyQvH3voXD4pnmD2QG2zc0xuKFyp23AnaKWSmyfLm2npNnpagS7W1qW4edPKI60csfWz9k6YhaKyavmH0rZOVz6_ZJxmCtrji&#x22; frameborder=&#x22;0&#x22; scrolling=&#x22;auto&#x22; allowfullscreen style=&#x22;display: block;margin-left: auto;margin-right: auto;max-width: 100%;&#x22;></iframe>" iframeHeight="750"}

:::

