---
title: How to join
slug: how-to-join
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:40:34 GMT+0000 (Coordinated Universal Time)
---

### Guide for the community on how to join Flipper One development

This page explains the overall structure of the Flipper One project, the sub-projects it consists of, and how you can contribute to its development.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/4tZetne1wIOtQsoxMFYEa-20260316-183949.jpg)

Flipper One is currently in active development. As a community-driven project, we’ve made the entire development process open — so you can see how things are built and even take part in shaping Flipper One’s future.

***

# Choose your contribution path

You do not need to understand the whole project before helping. Pick the kind of contribution you want to make, then open the matching sub-project page.

<table isTableHeaderOn="true" columnWidths="190,250,220">
  <tr>
    <td align="left">
      <p><strong>I want to...</strong></p>
    </td>
    <td align="left">
      <p><strong>Start here</strong></p>
    </td>
    <td align="left">
      <p><strong>Useful first action</strong></p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p>Fix or improve docs</p>
    </td>
    <td align="left">
      <p><a href="./resources/docs/About-Docs.md">Docs sub-project</a></p>
    </td>
    <td align="left">
      <p>Open a pull request with a clear page fix, screenshot update, or missing explanation.</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p>Test Linux builds or drivers</p>
    </td>
    <td align="left">
      <p><a href="./cpu-software/About-CPU-Software.md">Linux (CPU Software)</a> and <a href="./testing/About-Testing.md">Testing</a></p>
    </td>
    <td align="left">
      <p>Pick an open task, run the documented test, and share logs, board, image version, and result.</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p>Suggest a hardware or module improvement</p>
    </td>
    <td align="left">
      <p><a href="./hardware/About-Hardware.md">Hardware</a> and <a href="./mechanics/About-Mechanics.md">Mechanics</a></p>
    </td>
    <td align="left">
      <p>Attach a schematic snippet, model link, measurement, or clear module use case.</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p>Help with UI or visual design</p>
    </td>
    <td align="left">
      <p><a href="./user-interface/About-User-Interface.md">User Interface</a></p>
    </td>
    <td align="left">
      <p>Share a screenshot and a viewable Figma link that follows the display constraints.</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p>Contribute firmware changes</p>
    </td>
    <td align="left">
      <p><a href="./mcu-firmware/About-MCU-Firmware.md">MCU Firmware</a></p>
    </td>
    <td align="left">
      <p>Read the firmware contribution guide, build locally, and open a focused pull request.</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p>Browse tasks that need help</p>
    </td>
    <td align="left">
      <p><a href="./Open-tasks.md">Open tasks</a></p>
    </td>
    <td align="left">
      <p>Choose a task labeled <code>help wanted</code>, read existing comments, claim it with a brief reply, then add specific evidence or a concrete proposal.</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p>Ask a general question</p>
    </td>
    <td align="left">
      <p><a href="https://discord.com/invite/flipper">Discord</a> or <a href="https://x.com/Flipper_RND">X.com/Flipper_RND</a></p>
    </td>
    <td align="left">
      <p>Keep open task threads for contribution-related discussion, not general chat.</p>
    </td>
  </tr>
</table>

***

# Where should I ask this?

Use the right place for your question or contribution. This keeps open task threads focused for the teams working on Flipper One.

<table isTableHeaderOn="true" columnWidths="220,220,220">
  <tr>
    <td align="left">
      <p><strong>What you have</strong></p>
    </td>
    <td align="left">
      <p><strong>Where it belongs</strong></p>
    </td>
    <td align="left">
      <p><strong>Include this</strong></p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p>A reproducible bug or test result</p>
    </td>
    <td align="left">
      <p>The relevant GitHub issue or task tracker</p>
    </td>
    <td align="left">
      <p>Steps, expected result, actual result, logs, screenshots, hardware or image version.</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p>A docs fix or missing explanation</p>
    </td>
    <td align="left">
      <p>The Docs repository or a Docs task</p>
    </td>
    <td align="left">
      <p>Page link, confusing section, and proposed replacement text.</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p>A UI or visual design proposal</p>
    </td>
    <td align="left">
      <p>User Interface task comments</p>
    </td>
    <td align="left">
      <p>Screenshot, viewable Figma link, and short explanation of the interaction.</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p>A hardware, module, or accessory idea</p>
    </td>
    <td align="left">
      <p>Hardware or Mechanics task comments</p>
    </td>
    <td align="left">
      <p>Use case, connector or interface, dimensions, power or signal requirements, and any draft files.</p>
    </td>
  </tr>
  <tr>
    <td align="left">
      <p>A broad feature wish or general product question</p>
    </td>
    <td align="left">
      <p>Discord, social channels, or a relevant docs page question</p>
    </td>
    <td align="left">
      <p>What you want to do and why existing docs did not answer it.</p>
    </td>
  </tr>
</table>

***

# Sub-projects structure of Flipper One

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/kBApFvrmGBeMdNqOiyoIm-20260422-152345.jpg)

Flipper One is a large and complex project, divided into several sub-projects. Each sub-project is managed by a dedicated Flipper team, with its own structure, rules, and workflows. This Developer Portal acts as a wiki and the main entry point into all sub-projects, hosting their documentation and contribution guides.

‎ 

**Currently, we have the following sub-projects:**

::::VerticalSplit{layout="left"}
:::VerticalSplitItem
### [Hardware](./hardware/About-Hardware.md)

::Image[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/9plDPlgbxscoFIacbj8Q9-20260331-093234.png" size="38" width="333" height="243" position="flex-start"}
:::

:::VerticalSplitItem
Electrical hardware development. This is where the printed circuit boards (PCBs), antennas, and everything related to the electrical connections of chips, connectors, and processors are designed. The Hardware team works closely with the Mechanics team to ensure the electronics are compatible with the enclosure. [**Learn more →**](./hardware/About-Hardware.md)
:::
::::

***

::::VerticalSplit{layout="left"}
:::VerticalSplitItem
### [Mechanics](./mechanics/About-Mechanics.md)

::Image[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/C5VLSGhfaLWBS5E3VIMF8-20260331-093258.png" size="50" width="357" height="333" position="flex-start"}
:::

:::VerticalSplitItem
Mechanical and industrial design. This is where the enclosure, buttons, plastic and metal parts, and mounting components are designed. Everything the user physically interacts with. Many mechanical tasks are tightly coupled with the Hardware team. [**Learn more →**](./mechanics/About-Mechanics.md)
:::
::::

***

::::VerticalSplit{layout="left"}
:::VerticalSplitItem
### [Linux (CPU Software)](./cpu-software/About-CPU-Software.md)

::Image[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/ELzD0IezeYIDXuYC1yP2a-20260331-093341.png" size="34" width="267" height="318" position="flex-start"}
:::

:::VerticalSplitItem
Linux kernel, modules, drivers, userspace, bootloader, Rockchip tools, etc. This is the largest and most complex sub-project, spanning many repositories. It contains the core software that users will interact with directly. [**Learn more →**](./cpu-software/About-CPU-Software.md)
:::
::::

***

::::VerticalSplit{layout="left"}
:::VerticalSplitItem
### [MCU Firmware](./mcu-firmware/About-MCU-Firmware.md)

::Image[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/On5sGCZ3-QWo2sYbRVTam-20260331-093415.png" size="38" width="309" height="306" position="flex-start"}
:::

:::VerticalSplitItem
Firmware for the RP2350 microcontroller (MCU), which controls the display, power subsystem, and CPU boot process, and handles button and touchpad events. [**Learn more →**](./mcu-firmware/About-MCU-Firmware.md)
:::
::::

***

::::VerticalSplit{layout="left"}
:::VerticalSplitItem
### [User Interface](./user-interface/About-User-Interface.md)

::Image[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/CzLfRFqDmQf-g_0Mu_WA--20260331-093442.png" size="36" width="282" height="273" position="flex-start"}
:::

:::VerticalSplitItem
UI/UX development. This is where the user interface, visual communication of the device, all graphics, and visual design are developed. [**Learn more →**](./user-interface/About-User-Interface.md)
:::
::::

***

::::VerticalSplit{layout="left"}
:::VerticalSplitItem
### [Docs](./resources/docs/About-Docs.md)

::Image[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/RfUa81BVRdDm1qKCoXnrd-20260331-093508.png" size="36" width="273" height="273" position="flex-start"}
:::

:::VerticalSplitItem
Developer portal wiki, technical docs, guides, and datasheets. All documentation — including this wiki — is developed here. It covers both the Flipper One product documentation and descriptions of development processes and contribution guides. [**Learn more →**](./resources/docs/About-Docs.md)
:::
::::

***

::::VerticalSplit{layout="left"}
:::VerticalSplitItem
### [Testing](./testing/About-Testing.md)

::Image[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/M8o8dC4criD5llKbqSJB6-20260331-093535.png" size="36" width="282" height="273" position="flex-start"}
:::

:::VerticalSplitItem
Tools for testing device subsystems and hardware validation. Includes various scripts and programs for testing power, networking, CPU, audio, graphics, etc. Also includes interface prototypes, demos, and sample audio and video files. [**Learn more →**](./testing/About-Testing.md)
:::
::::

***

# Inside a sub-project

A sub-project within the Flipper One project is a collection of entities used by the development team. Each sub-project includes at least three types of entities:

- 📚 **Documentation** — explains the sub-project structure, provides an overview of assets and platforms, and contribution guidelines.
- ✅ **Task tracker&#x20;**— used to track and discuss tasks, including those where the community can help.
- 📁 **Assets & platforms&#x20;**— includes source code, files, firmware builds, 3D models, UI mockups, images, and APIs available for community review and contribution.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/R-x3IVDbaRqBT2povHK4i-20260410-164947.jpg)

***

## 📚 Documentation

Each sub-project is different, so it has its own documentation explaining how it is organized and how it works. You can access this documentation through the Flipper One Developer Portal (this wiki) or in the README file of the sub-project’s GitHub repository.

Documentation usually includes:

- An overview of the sub-project structure
- Task tracker rules
- Contribution guidelines

For those who want to explore further, some sub-projects provide more in-depth materials, such as datasheets, test results, logs, and design guides.

:::hint{type="info"}
**You can contribute to the documentation**

This wiki is a sub-project of its own, and anyone can contribute by editing [its source files on GitHub](https://github.com/flipperdevices/flipperone-docs). Learn more in the [Docs sub-project](./resources/docs/About-Docs.md).
:::

***

## ✅ Task tracker

Tasks for each sub-project are managed in a task tracker — a Kanban board on GitHub. Each task on the board is a GitHub issue from the sub-project repository. You can view [all task trackers on GitHub](https://github.com/orgs/flipperdevices/projects).

![MCU Firmware task tracker](/files/pics/mcu-firmware-task-tracker.png)

‎ 

### What’s the difference between GitHub issues and task tracker issues?

There’s no difference. The task tracker simply organizes the existing GitHub issues into a Kanban board. It also allows issues from different repositories to be grouped together in one place and managed as a single large task with sub-tasks.

For example, here is a [list of GitHub issues](https://github.com/flipperdevices/flipperone-mcu-firmware/issues) from the MCU Firmware sub-project and [how they are organized on the Kanban board](https://github.com/orgs/flipperdevices/projects/8).

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/QoPhF9YoGDfIllcZR8_5p-20260410-161735.jpg "Task tracker is a Kanban-style view of standard GitHub issues")

‎ 

### Open tasks

Some of our tasks are open. This means the community can interact with them just as they would with any issue in a classic GitHub repository — leaving comments, attaching files, and so on. Each task includes a short title and a detailed description, often with links and screenshots to help you understand it.

![Example of an open task in MCU Firmware sub-project](/files/pics/open-task.jpg)

Tasks can be marked with different **labels**:

- **help wanted** — tasks where we actively invite the community to participate and contribute to the solution. Example: [Operating modes discussion](https://github.com/flipperdevices/flipperone-ui/issues/1)
- **locked** — tasks that are closed to the community. This means we are not ready to discuss the task or accept feedback. You can still see Flipper team’s internal discussions.

::::hint{type="info"}
### ⚠️ Contributions only — no flooding

To keep collaboration productive, please keep comments on-topic. Open tasks are for contribution-related discussion only. If you have an idea or concern, first turn it into a concrete contribution and share it as a comment on a task. For general questions or discussions, you’re always welcome to join the conversation on [social media](https://x.com/Flipper_RND) or [Discord](https://discord.com/invite/flipper)!

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

1. Pick a path from the table above and read that sub-project’s overview and contribution guide.
2. Find a matching **help wanted** task on the [🚧 Open tasks](./Open-tasks.md) page or in the sub-project task tracker.
3. Read the task description and existing comments before posting.
4. Share something concrete: a test result, log, screenshot, code change, design file, or docs fix.

![Open tasks](/files/pics/step-2-check-task-tracker.png)

For docs pull requests, also read the [Docs sub-project](./resources/docs/About-Docs.md), [Markup reference](./resources/docs/Markup-reference.md), and [Style guide](./resources/docs/Style-guide.md).

## Join discussions in our socials

Follow us on X and join our Discord server to hang out, ask questions, and connect with other contributors.

::::LinkArray{contentSource="CUSTOM"}
:::LinkArrayItem{headerType="IMAGE" headerImage="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/O5IbFQ7KAuHJE_lqbKbNX-20260401-145400.jpg"}
[X.com/Flipper\_RND](https://x.com/Flipper_RND)

Follow updates and project announcements on X.com
:::

:::LinkArrayItem{headerType="IMAGE" headerImage="https://app.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/doVC8Airf2_FH2IwVxxAV_monosnap-miro-2023-04-13-19-25-16.png"}
[Flipper Devices Discord](https://discord.com/invite/flipper)

Chat with the community and Flipper team on our Discord server
:::
::::

## Subscribe to our weekly digest

Each week, we'll share a quick update on how things are coming along and flag any areas where extra help would be welcome. No pressure to jump in right away — you might just spot something in a future update that catches your eye!

:::hint{type="info"}
⚠️ **Nerds Warning**: this is a developer-focused, highly technical newsletter.
:::

:::Iframe{code="<iframe width=&#x22;540&#x22; height=&#x22;750&#x22; src=&#x22;https://183c2432.sibforms.com/serve/MUIFAAgzua23MvPHbQJyGmSkqAwomY_d-OtcEmQJaZ90xXKQQ_70E5jmVi97OFh-kF6NR69IL74D7n6ieCsJTlnda6j8F0RncbcEgx2_tiYW6qISyQvH3voXD4pnmD2QG2zc0xuKFyp23AnaKWSmyfLm2npNnpagS7W1qW4edPKI60csfWz9k6YhaKyavmH0rZOVz6_ZJxmCtrji&#x22; frameborder=&#x22;0&#x22; scrolling=&#x22;auto&#x22; allowfullscreen style=&#x22;display: block;margin-left: auto;margin-right: auto;max-width: 100%;&#x22;></iframe>" iframeHeight="750"}

:::

