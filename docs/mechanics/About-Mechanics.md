---
title: About Mechanics
docTags: 
createdAt: Mon Apr 20 2026 10:15:55 GMT+0000 (Coordinated Universal Time)
updatedAt: Mon Apr 20 2026 10:24:55 GMT+0000 (Coordinated Universal Time)
---

This page explains the structure of the Mechanics sub-project, provides links to design files, and outlines how to contribute to Flipper One's mechanical development.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/CQrg6SrR8-ulsW8dmNAug-20260414-183905.png)

The Mechanics sub-project is where we engineer the enclosure, buttons, plastic and metal parts, and mounting components of Flipper One. We share 3D models of the **Body**, **Back Plate**, and **Antenna Rail** with the community, and keep the development process open for feedback and discussion.

The Mechanics sub-project consists of:

- ✅ :Link[Task tracker]{href="https://github.com/orgs/flipperdevices/projects/15" newTab="true" hasDisabledNofollow="false"}
- ⚙️ :Link[3D models on Onshape]{href="https://cad.onshape.com/documents/32ee3b79861e4ff5fe28ee3b/w/8eca0dcb9e92b0271d434028/e/adb36e3c67cc1a734691cf20" newTab="true" hasDisabledNofollow="false"}
- 📁 :Link[Design files on GitHub]{href="https://github.com/flipperdevices/flipperone-mechanics" newTab="true" hasDisabledNofollow="false"}

We'd love your feedback — look for tasks tagged **help wanted** in the task tracker, or contribute directly to the GitHub repository via pull requests.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/AECUDKqdLJkYxyuiMDdn_-20260416-170227.jpg)

***

## ✅  Tasks tracker

All mechanical team tasks are tracked in the GitHub project :Link[Flipper One — Mechanics]{href="https://github.com/orgs/flipperdevices/projects/15" newTab="true" hasDisabledNofollow="false"}. There, you can see what the engineering team is working on and follow progress and discussions.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/BeWS1oVK3tyEiQh9mPzpn-20260413-115237.jpg "Mechaincs sub-project task tracker on GitHub")

**Some tasks are open** to the community and marked with a **help wanted** label. You’re welcome to join the discussion on these tasks or submit your design proposals — just make sure to read the [**Contribution guide**](About-Mechanics.md) first.

***

## ⚙️ 3D models on Onshape

You can view, edit, or export the 3D models via :Link[Onshape]{href="https://cad.onshape.com/documents/32ee3b79861e4ff5fe28ee3b/w/8eca0dcb9e92b0271d434028/e/adb36e3c67cc1a734691cf20" newTab="true" hasDisabledNofollow="false"} – a cloud-based CAD tool (similar to SolidWorks) that runs directly in your web browser. We’ll always upload the latest version of the Flipper One 3D models to Onshape.

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

To open the 3D model, simply click the :Link[Flipper One - Onshape]{href="https://cad.onshape.com/documents/32ee3b79861e4ff5fe28ee3b/w/8eca0dcb9e92b0271d434028/e/adb36e3c67cc1a734691cf20" newTab="true" hasDisabledNofollow="false"} link — the model will open in your browser in view mode. Here you can navigate the model:

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
Select one or more parts in the sidebar on the left.&#x20;
:::

:::WorkflowBlockItem
Right-click one of the selected parts and click **Export…**

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/TfxJchXHNxpDs7UdSTu63-20260325-160855.png)
:::

:::WorkflowBlockItem
Choose the file format and export options, then click **Export**.
:::
::::

***

### How to edit 3D models

To edit the model or design a new one, you’ll need to copy the model to your own account. Here’s how:

::::WorkflowBlock
:::WorkflowBlockItem
Log in to your :Link[Onshape account]{href="https://www.onshape.com/en/" newTab="true" hasDisabledNofollow="false"}.
:::

:::WorkflowBlockItem
Open the Flipper One model in Onshape by clicking :Link[this link]{href="https://cad.onshape.com/documents/32ee3b79861e4ff5fe28ee3b/w/8eca0dcb9e92b0271d434028/e/adb36e3c67cc1a734691cf20" newTab="true" hasDisabledNofollow="false"}.
:::

:::WorkflowBlockItem
Click **Make a copy to edit** at the top of the screen and choose a location in your Onshape workspace where the model will be saved.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/5JkGeKKltayBByf4Ikq4b-20260325-132625.png)
:::
::::

Now your copy of the model is opened in edit mode, so you can edit it.

:::hint{type="info"}
Check out the free :Link[Onshape learning courses]{href="https://learn.onshape.com/" newTab="true" hasDisabledNofollow="false"} if you plan to work with it.
:::

***

## 📁 Design files on GitHub

The :Link[flipperone-mechanics]{href="https://github.com/flipperdevices/flipperone-mechanics" newTab="true" hasDisabledNofollow="false"} GitHub repository contains both current and legacy versions of Flipper One’s enclosure 3D models. It also includes other design files, such as enclosure text and labels, as well as designs for official hardware modules and add-ons. You can download the design files to explore and modify them.

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

# How to contribute

:::hint{type="info"}
To contribute to the Mechanics sub-project, you need to have a GitHub account. You can create one on the :Link[GitHub website]{href="https://github.com/signup" newTab="true" hasDisabledNofollow="false"}.
:::

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/EcotI__FOd58IUCUyNzqC-20260420-091800.jpg)

Anyone can contribute to the Mechanics sub-project via the GitHub repository by commenting on the open tasks or making pull requests with suggested changes:

- [**Comment on an open task**](./#comment-on-an-open-task)
- [**Share a new design as a pull request**](./#share-a-new-design-as-a-pull-request)



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

***

## Comment on an open task

Open tasks that need the community's help are labeled **help wanted**. If you have ideas on how to improve the design, you can contribute by commenting on the task and attaching screenshots, videos, or links:

:::::WorkflowBlock
:::WorkflowBlockItem
In the :Link[Mechanics GitHub project]{href="https://github.com/orgs/flipperdevices/projects/15" newTab="true" hasDisabledNofollow="false"}, click the open task you want to contribute to.
:::

::::WorkflowBlockItem
In the comments section, clearly write your comment and attach a screenshot, video, or provide a link to your 3D model on :Link[Onshape]{href="https://www.onshape.com/en/" newTab="true" hasDisabledNofollow="false"}. Unfortunately, `.stp` files can't be attached to the comment.

:::hint{type="info"}
**Important:** If you share a link to your design on Onshape, ensure the model is accessible for others to view.
:::

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/jnEqEalHspW_JJ2Suz3SU-20260325-175922.png)

**Attachment size limit:**

- Images: 10 MB
- Videos: 100 MB
::::

:::WorkflowBlockItem
Click **Comment**.
:::
:::::

We review all ideas carefully! We may ask additional questions about your idea in the task thread, so please follow notifications from GitHub in your email.

***

## Share a new design as a pull request

If you have an idea for improving the design of Flipper One that isn't covered by an existing open task, you're still welcome to contribute it. Fork the GitHub repository (this creates your own linked copy), make your changes to the design files, and submit a pull request to our repository:

::::WorkflowBlock
:::WorkflowBlockItem
Go to the :Link[flipperone-mechanics]{href="https://github.com/flipperdevices/flipperone-mechanics" newTab="true" hasDisabledNofollow="false"} repository.
:::

:::WorkflowBlockItem
Fork the repository to your GitHub account by clicking the **Fork** button in the upper-right corner, then confirm your action.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/O40uj7MONYA7c8t19e5UZ_image.png)
:::

:::WorkflowBlockItem
In your forked repository, go to the **CURRENT** folder (where the `Flipper One (X.X).stp` file is located).
:::

:::WorkflowBlockItem
Click the **Add file&#x20;**&#x64;ropdown button (near the top right of the file list).

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/aaYiTPWW4JULDCfa2fZHY-20260326-140414.png)
:::

:::WorkflowBlockItem
Select **Upload files**.
:::

:::WorkflowBlockItem
Drag and drop a design file with your idea into the browser window, or click **choose your files** to select it from your computer.
:::

:::WorkflowBlockItem
Once the file finishes uploading, scroll down to the **Commit changes&#x20;**&#x62;ox at the bottom.
:::

:::WorkflowBlockItem
Add a clear, concise commit **description** (for example: *USB-C 1 label fixed*).
:::

:::WorkflowBlockItem
Below, select **Create a new branch for this commit and start a pull request**.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/X4nGTF1mayohLgBciMm1q-20260325-200702.png)
:::

:::WorkflowBlockItem
Name the branch to reflect your GitHub nickname and the area of changes. For example: `john/back-plate-improvement`
:::

:::WorkflowBlockItem
Click **Propose changes**.
:::

:::WorkflowBlockItem
In the **Open a pull request** page, add a **title** and a **description** explaining what changed in the design file.

We highly recommend attaching screenshots that show what changed.
:::

:::WorkflowBlockItem
Click **Create pull request**.
:::
::::

We review all ideas carefully! We may ask additional questions about your idea in the pull request thread, so please follow notifications from GitHub in your email.
