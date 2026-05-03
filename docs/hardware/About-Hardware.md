---
title: About Hardware
slug: hardware/about
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:32:40 GMT+0000 (Coordinated Universal Time)
---

This page explains the structure of the Hardware sub-project, provides links to its resources, and outlines how to contribute to Flipper One's electrical hardware development.

![About Hardware](/files/pics/about-hardware-main.png)

The Hardware sub-project covers electrical hardware development: printed circuit boards (PCBs), antennas, schematics, and everything related to the electrical connections of chips, connectors, and processors. The Hardware team works closely with the Mechanics team to ensure the electronics are compatible with the enclosure.

The Hardware sub-project consists of:

- ✅ :Link[Task tracker]{href="https://github.com/orgs/flipperdevices/projects/9" newTab="true" hasDisabledNofollow="false"}
- ⚡ :Link[Design files on Altium 365]{href="https://flipper.365.altium.com/designs/folder-A78C8D02-EA07-49E1-AC7A-E84FAA2AF410" newTab="true" hasDisabledNofollow="false"}
- 📁 :Link[GitHub repository]{href="https://github.com/flipperdevices/flipperone-hardware" newTab="true" hasDisabledNofollow="false"}
- 📚 Docs:
  - 🔌 **Hardware section** (you're here)
  - :Link[🧪 Testing section]{href="../testing/About-Testing.md" newTab="true" hasDisabledNofollow="true"}

We'd love your feedback — look for tasks tagged **help wanted** in the task tracker, share your ideas in the comments, or contribute directly to the docs.

![Hardware sub-project structure](/files/pics/hardware-sub-project-structure.jpg)

***

## ✅  Tasks tracker

All Hardware team tasks are tracked in the GitHub project :Link[Flipper One — Hardware]{href="https://github.com/orgs/flipperdevices/projects/9" newTab="true" hasDisabledNofollow="false"}. There, you can see what the engineering team is working on and follow progress and discussions.

![Hardware board explainer](/files/pics/hardware-board-explainer.png)

**Some tasks are open** to the community and marked with a **help wanted** label. You're welcome to join the discussion on these tasks or submit your design proposals — just make sure to read the :Link[Contribution guide]{href="./#how-to-contribute" newTab="false" hasDisabledNofollow="true"} first.

***

## ⚡ Design files on Altium 365

Selected parts of Flipper One's electrical design — schematics, PCB layouts, and BOM — are hosted on :Link[Altium 365]{href="https://flipper.365.altium.com/designs/folder-A78C8D02-EA07-49E1-AC7A-E84FAA2AF410" newTab="true" hasDisabledNofollow="false"}, the cloud collaboration platform for circuit design. Altium 365 hosts the latest version of the shared design files; you can view them in your browser without installing any software.

![Altium 365 Web Viewer interface](/files/pics/altium-ui-general.png "Altium 365 Web Viewer interface")

Click any project in the Flipper One folder to open it in the Web Viewer. Five view tabs are available along the top:

- **SCH** — schematic
- **PCB** — 2D layout
- **3D** — interactive 3D render
- **Draftsman** — fabrication documentation
- **BOM** — Bill of Materials

***

### How to view the design files

The Altium 365 Web Viewer lets you browse the project directly in your browser — no Altium Designer install required.

::::WorkflowBlock
:::WorkflowBlockItem
**Open the Flipper One folder.** Go to :Link[Flipper One on Altium 365]{href="https://flipper.365.altium.com/designs/folder-A78C8D02-EA07-49E1-AC7A-E84FAA2AF410" newTab="true" hasDisabledNofollow="false"}.
:::

:::WorkflowBlockItem
**Sign in with your Altium or Google account.** If you don't have an Altium account, create one — it's free for viewing shared projects.

![Altium 365 sign-in](/files/pics/altium-ui-login.png)
:::

:::WorkflowBlockItem
**Open a project.** Click the project you want to inspect.
:::

:::WorkflowBlockItem
**Switch between views.** Use the tabs at the top of the viewer to move between SCH, PCB, 3D, Draftsman, and BOM.

![Altium 365 open project — schematic view](/files/pics/altium-ui-view.png)
:::

:::WorkflowBlockItem
**Inspect components and nets.** All views support pan and zoom, plus search and cross-probing — click a component on the schematic to highlight it on the PCB, or select a net to trace it across the design.
:::
::::

***

### How to export the design files

The Web Viewer includes a download control whose available formats depend on the view you're in. From the schematic, PCB, or BOM views you can download a copy of the document for offline reference.

![Altium 365 Web Viewer download control](/files/pics/altium-ui-download.png)

The Web Viewer can export the entire project or individual derived files for offline reference.

::::WorkflowBlock
:::WorkflowBlockItem
**Open a project and click the Downloads icon** in the top-right of the viewer. A panel opens with Project Source Files and Derived Files sections.
:::

:::WorkflowBlockItem
**Download the whole project.** In Project Source Files, click the project entry to download all source files as a single archive.

or

**Download individual files.** In Derived Files, pick what you need — Gerber, Assembly Docs, PDF Schematic, STEP, or BOM.
:::
::::

For full info about the download feature, see Altium's :Link[official Web Viewer documentation]{href="https://www.altium.com/documentation/altium-365/viewers/web-viewer#downloading" newTab="true" hasDisabledNofollow="false"}.

***

## 📚 Docs

Hardware documentation is split across two sections:

- 🔌 **Hardware section** (you're here) — port pinouts, modules, and subsystem references (Wi-Fi & Bluetooth, power, M.2, GPIO).
- :Link[🧪 Testing section]{href="../testing/About-Testing.md" newTab="true" hasDisabledNofollow="true"} — hardware verification procedures for each subsystem.

***

## How to contribute

The Hardware sub-project accepts contributions in two forms: **comments on open tasks** for ideas, suggestions, and improvements, and **edits to the docs** for documenting hardware experiments, findings, or external module designs.

***

### Suggest your change as a comment on an open task

::::hint{type="info"}
**⚠️ Contributions only — no flooding**

To keep collaboration productive, please keep comments on-topic. Open tasks are for contribution-related discussion only. If you have an idea or concern, first turn it into a concrete contribution and share it as a comment on a task. For general questions or discussions, you're always welcome to join the conversation on :Link[social media]{href="https://x.com/Flipper_RND" newTab="true" hasDisabledNofollow="false"} or :Link[Discord]{href="https://discord.com/invite/flipper" newTab="true" hasDisabledNofollow="false"}!

::::

![Contribute a comment on an open task](/files/pics/contribute-a-comment.jpg)

Open tasks that need the community's help are labeled **help wanted**. If you have ideas on how to improve the design, you can contribute by commenting on the task and attaching screenshots, schematics, or links:

:::::WorkflowBlock
:::WorkflowBlockItem
**Pick a task.** In the :Link[Hardware GitHub project]{href="https://github.com/orgs/flipperdevices/projects/9" newTab="true" hasDisabledNofollow="false"}, browse the open tasks and click the one labeled **help wanted** that you want to contribute to.
:::

::::WorkflowBlockItem
**Write your suggestion.** In the comments section, clearly describe your suggestion and attach a screenshot, schematic snippet, or a link to your design on Altium 365. Ensure your design is accessible for others to view.

![Good vs bad comment on a Hardware task](/files/pics/hardware-good-vs-bad-comment.png)

**Attachment size limit:**

- Images: 10 MB
- Videos: 100 MB
::::

:::WorkflowBlockItem
**Click Comment** to submit.
:::
:::::

We review all comments carefully! We may ask additional questions about your idea in the task thread, so please follow notifications from GitHub in your email.

***

### Contribute to the docs

If you've spotted an error in the Hardware section, want to clarify something, or want to share your hardware experiments and findings, you're welcome to contribute by editing the docs. The fastest way to jump straight to a page's source is the **Edit on GitHub** button on the live site — it opens the page's `.md` file directly in the GitHub editor.

![Contribute to the Hardware docs](/files/pics/hardware-contribute-to-docs.jpg)

For a longer change, fork the repository, make your edits on a new branch, and open a pull request:

::::WorkflowBlock
:::WorkflowBlockItem
**Read the&#x20;**:Link[Markup example]{href="../resources/Markup-example.md" newTab="true"}**&#x20;page** to learn the supported Markdown and Archbee syntax.
:::

:::WorkflowBlockItem
**Fork the repository.** Go to :Link[flipperone-docs]{href="https://github.com/flipperdevices/flipperone-docs" newTab="true"} and click **Fork** in the upper-right corner. Your fork opens on the `dev` branch — our staging branch for contributions. All your work happens here.
:::

:::WorkflowBlockItem
**Edit or create your&#x20;**`.md`**&#x20;file.** In your fork, find the file you want to edit under `docs/hardware/`, or create a new one in the appropriate subfolder. Follow the syntax shown on the Markup example page — some Markdown features behave differently in Archbee.
:::

:::WorkflowBlockItem
**(Optional) Add images.** If your change includes images, diagrams, or screenshots, upload them to `docs/files/pics/` and reference them with a relative path:

```markdown
![Alt text](/files/pics/your-image.png "Caption")
```

Use descriptive, lowercase filenames with hyphens (e.g. `gpio-pinout.png`). Keep images under 1 MB.
:::

:::WorkflowBlockItem
**(Optional) Register the new page in&#x20;**:Link[archbee.json]{href="https://github.com/flipperdevices/flipperone-docs/blob/public-release/archbee.json" newTab="true"}**.** Place it in the sidebar hierarchy (no deeper than two levels) — see :Link[How archbee.json works]{href="../resources/About-Docs.md#how-archbeejson-works" newTab="true"} for the syntax. It's okay to skip — we'll update the file after merging your PR.
:::

:::WorkflowBlockItem
**Create a branch and commit.** Name the branch `nickname/what-changed` (e.g. `john/gpio-module-experiment`). Keep commit messages concise — e.g. `Add: GPIO module pinout reference`.
:::

:::WorkflowBlockItem
**Open a pull request from your branch to the original repository.** The target is pre-selected to `dev` — leave it as is. Add a clear title and description, and ideally attach screenshots and a link to the related open task.

After review, we promote your changes from `dev` to `public-release`, which publishes them to the live site.
:::
::::

Once your pull request is merged into `dev` and later promoted to `public-release`, Archbee automatically picks up the changes and rebuilds the live site at :Link[docs.flipper.net/one]{href="https://docs.flipper.net/one" newTab="true"}.
