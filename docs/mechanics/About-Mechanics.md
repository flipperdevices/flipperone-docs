---
title: About Mechanics
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Sun Apr 26 2026 19:21:47 GMT+0000 (Coordinated Universal Time)
---

This page explains the structure of the Mechanics sub-project, provides links to design files, and outlines how to contribute to Flipper One's mechanical development.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/CQrg6SrR8-ulsW8dmNAug-20260414-183905.png)

The Mechanics sub-project is where we engineer the enclosure, buttons, plastic and metal parts, and mounting components of Flipper One. We share 3D models of the **Body**, **Back Plate**, and **Antenna Rail** with the community, and keep the development process open for feedback and discussion.

The Mechanics sub-project consists of:

- ✅ :Link[Task tracker]{href="https://github.com/orgs/flipperdevices/projects/15" newTab="true" hasDisabledNofollow="false"}
- ⚙️ :Link[3D models hosted on Onshape]{href="https://cad.onshape.com/documents/32ee3b79861e4ff5fe28ee3b/w/8eca0dcb9e92b0271d434028/e/adb36e3c67cc1a734691cf20" newTab="true" hasDisabledNofollow="false"}
- 📁 :Link[Design files on GitHub]{href="https://github.com/flipperdevices/flipperone-mechanics" newTab="true" hasDisabledNofollow="false"}

We'd love your feedback — look for tasks tagged **help wanted** in the task tracker, or contribute directly to the GitHub repository via pull requests.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/k9V0SKmJ5Nuk7BKxpo4zc-20260422-161729.jpg)

***

## ✅  Tasks tracker

All mechanical team tasks are tracked in the GitHub project :Link[Flipper One — Mechanics]{href="https://github.com/orgs/flipperdevices/projects/15" newTab="true" hasDisabledNofollow="false"}. There, you can see what the engineering team is working on and follow progress and discussions.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/j85RNnCbi9_-rFd0k5pPt-20260426-190415.png "Mechaincs sub-project task tracker on GitHub")

**Some tasks are open** to the community and marked with a **help wanted** label. You’re welcome to join the discussion on these tasks or submit your design proposals — just make sure to read the :Link[Contribution guide]{href="https://docs.flipper.net/one/about-mechanics#how-to-contribute" newTab="false" hasDisabledNofollow="true"} first.

***

## ⚙️ 3D models hosted on Onshape

You can view and export the 3D models via :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/BWs6BlQTIuaA34qFFvyY0-20260422-193237.png" alt caption} :Link[Onshape]{href="https://cad.onshape.com/documents/32ee3b79861e4ff5fe28ee3b/w/8eca0dcb9e92b0271d434028/e/adb36e3c67cc1a734691cf20" newTab="true" hasDisabledNofollow="false"} – a cloud-based CAD tool (similar to SolidWorks) that runs directly in your web browser. Onshape hosts the latest version of the 3D models. The same 3D models are also available in the :Link[CURRENT folder on GitHub]{href="https://github.com/flipperdevices/flipperone-mechanics/tree/dev/CURRENT" newTab="true" hasDisabledNofollow="false"}.

:::Iframe{code="<video&#xA;    autoplay muted loop playsinline style=&#x22;width: 100%; margin: 0 !important;&#x22;&#xA;    src=&#x22;https://cdn.flipperzero.one/Pan_rotate_and_move_parts_compressed.mp4&#x22;&#xA;></video>" iframeHeight="500"}

:::

We made some mechanical parts of Flipper One available for the community to explore. Feel free to review them, download them for 3D printing, or make your own external hardware modules for Flipper One.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/PDJWUIHqrJQ6DdbD-4if1-20260324-131638.jpg)

The 3D model consists of three parts:

- **Body** — the main enclosure of the device. It contains all electronics, the display, and the user controls. The public release provides this part as a solid shell with an empty interior.
- **Back Plate** — the back cover that provides access to the M.2 expansion port.
  This screw-on cover is interchangeable, with different designs for each module.
- **Antenna Rail** — a separate part for mounting SMA antennas. It is intentionally separate from the back plate so you can install antennas and route cables before attaching the plate, preventing cable damage during assembly.

:::hint{type="info"}
All surfaces and dimensions match the real product, allowing development of accessories, cases, mounts, back plates, antenna rails, and modules.
:::

***

### How to view 3D models

Simply click the :Link[Flipper One - Onshape]{href="https://cad.onshape.com/documents/32ee3b79861e4ff5fe28ee3b/w/8eca0dcb9e92b0271d434028/e/adb36e3c67cc1a734691cf20" newTab="true" hasDisabledNofollow="false"} link — the model will open in your browser in view mode. Here you can navigate the model:

- **Pan model** — click :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/n3aUz4Jq-P7dqI647w6Kb-20260325-114158.png" alt caption} Pan or click and hold the :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/290PzLQDUGQo8RuaFZv_j-20260325-133300.png" alt caption} middle wheel on your mouse.
- **Rotate model** — click :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/NjfVebUq_P1cC0Sc3lFjR-20260325-115455.png" alt caption} Rotate or :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/UXZ-1Id6BT7BeIBA6UJrO-20260325-133317.png" alt caption} right-click and hold your mouse.
- **Hide parts** — click the :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/Ayoe8ZZYFOa_gCCftgCb9-20260325-115841.png" alt caption} eye icon next to a part in the left side bar.
- **Move parts** — click a part in the 3D view or from the list on the left, then drag it to the desired position.

:::hint{type="info"}
For all methods of navigating models in Onshape, view :Link[the official documentation]{href="https://cad.onshape.com/help/Content/View/view_navigation_and_viewing_parts.htm?TocPath=Getting%20Started%20with%20Onshape%7CUser%20Interface%20Basics%7C_____2" newTab="true" hasDisabledNofollow="false"}.
:::

***

### How to export 3D models

You can export the models for printing to test ergonomics, or develop your own modules for Flipper One. Onshape supports exporting models in various formats.

:::hint{type="info"}
**Supported export formats:** STEP, STL, OBJ, SOLIDWORKS, IGES, Parasolid, GLTF, RHINO, COLLADA, JT, PVZ, ACIS, and 3MF.
:::

To export:

::::WorkflowBlock
:::WorkflowBlockItem
Click the :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/hPFRUcyf8EaWor_92zYgu-20260422-172307.png" alt caption} **Export** button at the bottom of your screen.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/Buv4aLbc3ftesmFkXVe72-20260426-190522.png)
:::

:::WorkflowBlockItem
Select your preferred export format.

![Onshape export formats](../files/pics/export-formats.png)
:::

:::WorkflowBlockItem
Click **Export**.
:::
::::

***

## 📁 Design files on GitHub

The :Link[flipperone-mechanics]{href="https://github.com/flipperdevices/flipperone-mechanics" newTab="true" hasDisabledNofollow="false"} GitHub repository hosts both current and legacy versions of Flipper One’s enclosure 3D models in `.stp` format. It also includes other design files, such as enclosure text and labels, as well as designs for official hardware modules and add-ons. You can download the design files to explore and modify them.

:::hint{type="info"}
Both the :Link[CURRENT folder on GitHub]{href="https://github.com/flipperdevices/flipperone-mechanics/tree/dev/CURRENT" newTab="true" hasDisabledNofollow="false"} and :Link[Onshape]{href="https://cad.onshape.com/documents/32ee3b79861e4ff5fe28ee3b/w/8eca0dcb9e92b0271d434028/e/adb36e3c67cc1a734691cf20" newTab="true" hasDisabledNofollow="false"} host the latest Flipper One 3D models, but there is a difference:

- :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/35CMh7cPaEJY42c0x205l-20260422-192635.svg" alt caption}**&#x20;GitHub** — only download models in `.stp` format.
- :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/17t3meaKNqmY8q-e1hSp_-20260422-194815.png" alt caption}**&#x20;Onshape** — view the current models and export in multiple formats.
:::

***

### Repository structure

The repository has the following folder structure:

```none
├── OLD/                     # Deprecated enclosure revisions
│   ├── A.0/
│   └── ...
├── CURRENT/                 # Current supported enclosure revision
│   └── X.N/                 # Current revision <LETTER>.<NUMBER>
│       ├── Flipper One (X.N).stp   # Full enclosure 3D model (STEP)
│       ├── Graphics/               # Logos, engravings, decals, artwork for the enclosure
│       └── Modules/                # Official modules and add-ons
```

***

### Versioning scheme

Design versioning scheme includes two parts: `<LETTER>.<NUMBER>` (for example, A.1), where:

- `LETTER` — major version. Different major versions are not mechanically compatible with each other.
- `NUMBER` — minor revision. This may indicate small changes (for example, graphics, labels, or minor tweaks). Different minor revisions are compatible with each other.

***

## How to contribute

:::hint{type="info"}
To contribute to the Mechanics sub-project, you need to have a GitHub account. You can create one on the :Link[GitHub website]{href="https://github.com/signup" newTab="true" hasDisabledNofollow="false"}.
:::

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/Mo4LPAlsvBYBJ0LdlcZWd-20260423-202546.jpg)

**Before you start:** Check open tasks in the :Link[task tracker]{href="https://github.com/orgs/flipperdevices/projects/15" newTab="true" hasDisabledNofollow="false"} to see what the team is already working on or where help is wanted.

::::WorkflowBlock
:::WorkflowBlockItem
Download 3D models from :Link[GitHub]{href="https://github.com/flipperdevices/flipperone-mechanics" newTab="true" hasDisabledNofollow="false"} or :Link[Onshape]{href="https://cad.onshape.com/documents/32ee3b79861e4ff5fe28ee3b/w/8eca0dcb9e92b0271d434028/e/adb36e3c67cc1a734691cf20" newTab="true" hasDisabledNofollow="false"}.
:::

:::WorkflowBlockItem
Edit the 3D models using any CAD tool.
:::

:::WorkflowBlockItem
Submit your work as a **pull request** to our GitHub repo. If there is an open task, you can submit your work in the comment section.
:::
::::

***

## Submit your design as a pull request

If you have an idea for improving the design of Flipper One, you're welcome to contribute it. Copy the GitHub repository, make your changes to the design files, and submit a pull request to the original repository:

::::WorkflowBlock
:::WorkflowBlockItem
**Open the repository.** Go to :Link[flipperone-mechanics]{href="https://github.com/flipperdevices/flipperone-mechanics" newTab="true" hasDisabledNofollow="false"} on GitHub.
:::

:::WorkflowBlockItem
**Fork the repository.** Click the **Fork** button in the upper-right corner and confirm to copy it to your GitHub account.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/2jGWJn2oQ6yvqc05wUV9x-20260426-190852.png)
:::

:::WorkflowBlockItem
**In your fork, open the CURRENT folder.**
:::

:::WorkflowBlockItem
**Click the Add file dropdown.**

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/1hy5kMVH_S45lKYwnnJ3e-20260426-191010.png)
:::

:::WorkflowBlockItem
**Select :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/hHcooERJ1R9C3tGrRKQOq_image.png" alt caption}Upload files** from the dropdown.
:::

:::WorkflowBlockItem
**Upload your files.** Drag and drop a file, or click **choose your files** to select it from your computer.
:::

:::WorkflowBlockItem
**After uploading, scroll down to Commit changes.**
:::

:::WorkflowBlockItem
**Write a commit description.** Keep it clear and concise — for example, *Add bumps to aluminum bracket*.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/cMstWOb0PqfMBq6LcdXju-20260426-191048.png)
:::

:::WorkflowBlockItem
**Click Commit changes** to save them in your repository.
:::

:::WorkflowBlockItem
**Open a pull request.** In your repository, click **Contribute → Open pull request**.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/ObqBpjO7nGF1wdtmfzyiF-20260426-191221.png)
:::

:::WorkflowBlockItem
**Check the target branch.** Confirm changes will be pushed to **flipperdevices/flipperone-mechanics**, base: **dev**.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/e4hVU57mbgVlqinJAFkfw-20260426-191307.png)
:::

:::WorkflowBlockItem
**Add a title and description.** Write the pull request **title** and a **description** in Markdown — preview it with **Preview**.

We highly recommend attaching screenshots that show what changed and a link to the open task this pull request is associated with.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/TXnaNL73fyF3sCig7g-St-20260426-191440.png "Pull request example")
:::

:::WorkflowBlockItem
**Click Create pull request.**
:::
::::

We review all ideas carefully! We may ask additional questions about your idea in the pull request thread, so please follow notifications from GitHub in your email.

***

## Suggest your change as a comment on an open task

::::hint{type="info"}
**⚠️ Contributions only — no flooding**

To keep collaboration productive, please keep comments on-topic. Open tasks are for contribution-related discussion only. If you have an idea or concern, first turn it into a concrete contribution and share it as a comment on a task. For general questions or discussions, you’re always welcome to join the conversation on :Link[social media]{href="https://x.com/Flipper_RND" newTab="true" hasDisabledNofollow="false"} or :Link[Discord]{href="https://discord.com/invite/flipper" newTab="true" hasDisabledNofollow="false"}!

::::

‎ 

Open tasks that need the community's help are labeled **help wanted**. If you have ideas on how to improve the design, you can contribute by commenting on the task and attaching screenshots, videos, or links:

:::::WorkflowBlock
:::WorkflowBlockItem
**Pick a task.** In the :Link[Mechanics GitHub project]{href="https://github.com/orgs/flipperdevices/projects/15" newTab="true" hasDisabledNofollow="false"}, browse the open tasks and click the one labeled **help wanted** that you want to contribute to.
:::

::::WorkflowBlockItem
**Write your suggestion.** In the comments section, clearly describe your suggestion and attach a screenshot, video, or a link to your 3D model on :Link[Onshape]{href="https://www.onshape.com/en/" newTab="true" hasDisabledNofollow="false"}. Unfortunately, `.stp` files can't be attached to the comment.

:::hint{type="info"}
**Important:** If you share a link to your design on Onshape, ensure the model is accessible for others to view.
:::

![Good vs bad comment on a Mechanics task](/files/pics/mechanics-good-vs-bad-comment.png)

**Attachment size limit:**

- Images: 10 MB
- Videos: 100 MB
::::

:::WorkflowBlockItem
**Click Comment** to submit.
:::
:::::

We review all comments carefully! We may ask additional questions about your idea in the task thread, so please follow notifications from GitHub in your email.
