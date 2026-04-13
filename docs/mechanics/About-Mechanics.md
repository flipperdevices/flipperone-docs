---
title: About Mechanics
docTags: 
createdAt: Wed Apr 08 2026 17:29:37 GMT+0000 (Coordinated Universal Time)
updatedAt: Mon Apr 13 2026 13:40:03 GMT+0000 (Coordinated Universal Time)
---

This page explains the structure of the Mechanics sub-project, provides links to design files, and outlines how to contribute to Flipper One's mechanical development.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/-rWWu6nWYzn0z9sCSiZK2-20260325-155001.jpg)

Our goal is to build a portable Linux computer, using feedback from our community and bringing those ideas into the final design of the device. Engineering the mechanical components for Flipper One is a challenging task — the enclosure must integrate multiple materials (plastic, aluminum, and rubber) while housing a complex array of internal components, including heat-generating chips, a heat sink, a lithium-ion battery, buttons, port and slot cutouts, and external module support.

On this page you’ll find:

- :Link[Mechanics sub-project structure]{href="https://docs.flipper.net/one/about-mechanics#mechanics-sub-project-structure" newTab="true" hasDisabledNofollow="false"}
- :Link[Task tracker]{href="https://docs.flipper.net/one/about-mechanics#task-tracker" newTab="true" hasDisabledNofollow="false"}
- :Link[3D model web viewer]{href="https://docs.flipper.net/one/about-mechanics#3d-model-web-viewer" newTab="true" hasDisabledNofollow="false"}
- :Link[GitHub repo with design files]{href="https://docs.flipper.net/one/about-mechanics#github-repo-with-design-files" newTab="true" hasDisabledNofollow="false"}
- :Link[How to contribute]{href="https://docs.flipper.net/one/about-mechanics#how-to-contribute" newTab="true" hasDisabledNofollow="false"}

***

# Mechanics sub-project structure

The sub-project consists of several entities:

- &#x20;📚 **Documentation** — explains the sub-project structure, provides an overview of assets and platforms, and contribution guidelines.
- ✅ **Task tracker** — shows current tasks of the mechanical engineering team and discussions.
- ⚙️ **3D model web viewer&#x20;**— allows viewing the 3D model directly in a browser and downloading it in different formats.
- 📁 **Repo with design files** — hosts current and legacy design files and allows submitting pull requests with proposed changes.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/xA0rvDdhznqljjrEw9INI-20260413-130026.jpg)

***

## ✅  Task tracker

All mechanical team tasks are tracked in the GitHub project :Link[Flipper One — Mechanics]{href="https://github.com/orgs/flipperdevices/projects/15" newTab="true" hasDisabledNofollow="false"}. There, you can see what the engineering team is working on and follow progress.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/BeWS1oVK3tyEiQh9mPzpn-20260413-115237.jpg "Mechaincs sub-project task tracker on GitHub")

**Some tasks are open** to the community and marked with a **help wanted** label. You’re welcome to join the discussion on these tasks or submit your design proposals — just make sure to read the [**Contribution guide**]() first.

***

## ⚙️ 3D model web viewer

You can view, edit, or export the 3D model via :Link[Onshape]{href="https://cad.onshape.com/documents/32ee3b79861e4ff5fe28ee3b/w/8eca0dcb9e92b0271d434028/e/adb36e3c67cc1a734691cf20" newTab="true" hasDisabledNofollow="false"} – a cloud-based CAD tool (similar to SolidWorks) that runs directly in your web browser. We’ll always upload the latest version of the Flipper One 3D model to Onshape.

:::Iframe{iframeHeight="500" code="<video&#xA;    autoplay muted loop playsinline style=&#x22;width: 100%; margin: 0 !important;&#x22;&#xA;    src=&#x22;https://cdn.flipperzero.one/Pan_rotate_and_move_parts_compressed.mp4&#x22;&#xA;></video>"}

:::

***

### Available 3D model parts

We made some mechanical parts of Flipper One available for the community to explore. Feel free to review them, download them for 3D printing, or make your own external hardware modules for Flipper One.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/PDJWUIHqrJQ6DdbD-4if1-20260324-131638.jpg)

The 3D model consists of three parts:

- **Body** — the main enclosure of the device. It contains all electronics, the display, and the user controls. The public release provides this part as a solid shell with an empty interior to prevent copying of the internal design.
- **Back Plate** — the rear cover that provides access to the M.2 expansion port.
  This screw-on cover is interchangeable, with different designs for each module.
- **Antenna Rail** — a separate part for mounting SMA antennas. It is intentionally separate from the back plate so you can install antennas and route cables before attaching the plate, preventing cable damage during assembly.

:::hint{type="info"}
All surfaces and dimensions match the real product, allowing development of accessories, cases, mounts, back plates, antenna rails, and modules.
:::

***

### How to view the 3D model

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

You can export the 3D model for printing to test ergonomics, or develop your own modules for Flipper One. Onshape supports exporting models or their parts in various formats.

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

To edit the model or design new parts for it, you’ll need to copy the model to your own account. Here’s how:

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

Now your copy of the model is opened in edit mode, so you can edit it or design new parts for it, such as your own custom back cover.

:::hint{type="info"}
Check out the free :Link[Onshape learning courses]{href="https://learn.onshape.com/" newTab="true" hasDisabledNofollow="false"} if you plan to work with it.
:::

***

## 📁 GitHub repo with design files

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

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/44Of2RVBCVPU9f2M5a6_1-20260326-141154.png)

Anyone can contribute to the Mechanics sub-project via the GitHub repository by commenting on the open tasks or making pull requests with suggested changes:

- [**Contribute to an open task**]()
- [**General suggestions regarding design**]()



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

## If you want to contribute to an open task

Tasks that need the community's help are labeled **help wanted**. If you have ideas on how to improve the design, you can contribute by commenting on the task and attaching screenshots or videos:

:::::WorkflowBlock
:::WorkflowBlockItem
In the Mechanics task tracker, find the open task you want to contribute to.
:::

::::WorkflowBlockItem
In the comments section, clearly write your comment and attach a screenshot, video, or provide a link to your 3D model on :Link[Onshape]{href="https://www.onshape.com/en/" newTab="true" hasDisabledNofollow="false"}.

:::hint{type="info"}
**Important:** If you share a link to your design on Onshape, ensure the model is accessible for others to view.
:::

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/jnEqEalHspW_JJ2Suz3SU-20260325-175922.png)

**Attachment size limit:**

- Images: 10 MB
- Videos: 100 MB *(test it)*
::::

:::WorkflowBlockItem
Click **Comment**.
:::
:::::

We review all ideas carefully! We may ask additional questions about your idea in the task thread, so please follow notifications from GitHub in your email.

***

## If you have a general suggestion regarding design

Suppose you have an idea to improve the current design of Flipper One, but there's no task for this in the task tracker. You still can modify the latest version of the design files and submit them to us. You’ll need to fork (copy) the GitHub repository, make your changes, and submit them as a pull request to our repository.

To submit your modifications to our GitHub repository:

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

***

## Rules

We welcome everyone to contribute, but we moderate user discussions in the repository to maintain a productive workflow. To avoid deletion of messages or bans, please follow these rules:

- **Be respectful and professional.** Offensive language or personal attacks will not be tolerated.
- **No spam or off-topic.** Keep comments relevant to the topic. This helps other contributors find relevant information more quickly.
- **Critique constructively.** We welcome criticism and value community involvement, but it must be constructive. If you disagree with a design decision, please propose an alternative solution.
- **Explain your ideas clearly.** Use text, screenshots, photos, or videos to make your suggestions understandable.
- **Respect versioning and naming conventions.** Follow existing folder structure and file naming rules when adding or changing files.
