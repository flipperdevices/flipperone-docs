# About Mechanics

::Image[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/PiuX0-xvP3jRWBk-tW5yn-20260324-105215.png" size="80" width="2060" height="1580" position="center"}

The Flipper One has a complex mechanical design. Its case is made of plastic, aluminum, and rubber. Inside, it has a 23 W·h Li-ion battery, parts that get hot, many buttons, ports, slots, and expansion modules support.

We opened some parts of the device design and invite the community to follow the project and help find the best solutions. Here’s what is now open:

- **Task tracker.** Anyone can explore the current tasks of the mechanical engineering team.
- **Device 3D model viewer.&#x20;**&#x59;ou can view it in your browser, download it in various formats, and 3D print it to test ergonomics. This also enables the community to start developing their own modules for the Flipper One.
- **Repository with design files.** You can review the design files, and share your suggestions with the team by opening an issue or submitting a PR with your proposed changes.

:::hint{type="warning"}
Please follow the **How to contribute** and **Rules** sections to keep the process structured and productive.
:::

# Task tracker

All tasks of the mechanical team are tracked in the GitHub Projects: :Link[Flipper One — Mechanics]{href="https://github.com/orgs/flipperdevices/projects/15" newTab="true" hasDisabledNofollow="false"}. Here you can find a classic Kanban board with tasks.

![Kanban board with mechanical team tasks](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/_GZt84iSLUAXE8-PYswHa-20260319-105013.png "Kanban board with mechanical team tasks")

:::hint{type="info"}
Tasks marked with the **Help needed** tag include questions or problems that need community assistance to resolve. Learn more about how to contribute **here**.
:::

# Device 3D model viewer

You can view, edit or export enclosure 3D-model via :Link[**Onshape**]{href="https://www.onshape.com/" newTab="true" hasDisabledNofollow="false"} - a cloud-based CAD (Computer-Aided Design), like SolidWorks or AutoCAD, but directly in your web browser.&#x20;

## View 3D model

Open the link in your web browser: :Link[Flipper One - Onshape]{href="https://cad.onshape.com/documents/32ee3b79861e4ff5fe28ee3b/w/8eca0dcb9e92b0271d434028/e/adb36e3c67cc1a734691cf20" newTab="true" hasDisabledNofollow="false"}. The 3D model will open in **view mode**. Here you can:

- **Pan and rotate the model.** Press the **Pan** or **Rotate** button on the bottom panel, then drag the model using the left mouse button.
- **Hide model parts.** Click the **eye icon** next to a part in the list on the left.
- **Move model parts.** Select a part in the 3D view or from the list on the left, then drag it to the desired position.

:::Iframe{code="<video&#xA;    autoplay muted loop playsinline style=&#x22;width: 100%; margin: 0 !important;&#x22;&#xA;    src=&#x22;https://cdn.flipperzero.one/Pan_rotate_and_move_parts_compressed.mp4&#x22;&#xA;></video>" iframeHeight="500"}

:::

## Export 3D model

Onshape supports exporting the model or its part in various formats. To export:

1. Select one or more parts of the model from the list on the left.&#x20;
2. Right-click one of the selected parts and choose **Export…**&#x20;
3. Choose the file format and export options, then click **Export**.

:::hint{type="info"}
**Supported formats:** STEP, STL, OBJ, SOLIDWORKS, IGES, Parasolid, GLTF, RHINO, COLLADA, JT, PVZ, ACIS, and 3MF.
:::

## Edit 3D model

To edit the model or design new parts for it, you’ll need to copy the model to your own account. Here’s how:

1. Log in to your Onshape account.&#x20;
2. Open the original Flipper One model using the link below.&#x20;
3. Click **Make a copy to edit** at the top of the screen and choose a location in your Onshape workspace where the model will be saved.&#x20;

Now your copy of the model opened in edit mode so you can edit it or design new parts for it, such as your own custom back cover.

:::hint{type="info"}
Check out the free :Link[Onshape Learning courses]{href="https://learn.onshape.com/" newTab="true" hasDisabledNofollow="false"} if you plan to work with it.
:::

# GitHub repo with design files

The :Link[flipperone-mechanics]{href="https://github.com/flipperdevices/flipperone-mechanics" newTab="true" hasDisabledNofollow="false"} repository contains all the versions of device's enclosure 3D models, as well as other design files (for example, text and outlines applied to the case).&#x20;

You can find more details about the folder structure, model parts descriptions, version naming conventions, and more in the repository’s README.

## Versioning scheme

Enclosure 3D model versions consist of two parts: **\<LETTER>.\<NUMBER>** (for example, A.1).

- **LETTER** — major version. Different major versions are **not mechanically compatible** with each other.
- **NUMBER** — minor revision. This may represent small changes (for example, graphics, labels, or minor tweaks). Different minor revisions **remain compatible** with each other.

## Folders structure

Description of the file and directory structure in this repository:

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

## 3D model parts

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/PDJWUIHqrJQ6DdbD-4if1-20260324-131638.jpg)

The 3D model consists of three main parts:

- **Body** — the main enclosure of the device. It contains all electronics, the display, and the user controls. The public release provides this part as a solid shell with an empty interior to prevent copying of the internal design.
- **Back plate** — the rear cover that provides access to the M.2 expansion port.
  This screw-on cover is interchangeable, with different designs for each module.
- **Antenna rail** — a separate part for mounting SMA antennas. It is intentionally separate from the back plate so you can install antennas and route cables before attaching the plate, preventing cable damage during assembly.

:::hint{type="info"}
All surfaces and dimensions match the real product, allowing development of accessories, cases, mounts, back plates, antenna rails, and modules.
:::

# How to contribute

Anyone can contribute to the project through the GitHub repository, using **Issue** or **Pull Request**, depending on whether you need to modify design files.

## If you need to modify design files

If you want to suggest a change to the current design, you can fork (copy) the repository, make your modifications, and submit them back to our repository as a pull request.

Here’s the step-by-step process to propose a change via a pull request:

1. Fork the :Link[flipperone-mechanics]{href="https://github.com/flipperdevices/flipperone-mechanics" newTab="true" hasDisabledNofollow="false"} repository to your GitHub account.
2. Clone your fork to your PC.
3. Create a new branch. Give it clear name (type what you plan to change, for example: *usb-c-1-label-fix*).
4. Make your changes in design files locally on your PC.
5. Commit changes. Use a clear and concise commit description (for example: *USB-C 1 label fixed*).
6. Push your branch to your fork. This uploads your branch with changes to it.
7. Click **Compare & pull request** in your fork on GitHub, fill the title and description, add images if you need and submit the pull request

## If you don’t need to modify design files

If you have a design suggestion but cannot or do not want to modify the design files yourself, you can submit it by creating an Issue. Make sure to describe your idea clearly and in detail. Include photos, illustrations, or videos if they help explain your suggestion.

Here’s the step-by-step process to propose a change via an Issue:

1. Go to the :Link[flipperone-mechanics]{href="https://github.com/flipperdevices/flipperone-mechanics" newTab="true" hasDisabledNofollow="false"} repository and open the **Issues** tab.
2. Click **New Issue**.
3. Add a title and description for your PR. Explain your idea, add images if you need.
4. Submit the Issue.

# Rules

We welcome everyone to contribute, but we moderate user discussions in the repository to maintain a productive workflow. To avoid deletion of messages or bans, please follow these rules:

- **Be respectful and professional.** Offensive language or personal attacks will not be tolerated.
- **No spam or offtopic.** Keep comments relevant to the topic. This helps other contributors find relevant information more quickly.
- **Critique constructively.** We welcome criticism and value community involvement, but it must be constructive. If you disagree with a design decision, please propose an alternative solution.
- **Explain your ideas clearly.** Use text, screenshots, photos, or videos to make your suggestions understandable.
- **Respect versioning and naming conventions.**&#x20;
- Follow existing folder structure and file naming rules when adding or changing files.&#x20;
- **Follow versioning conventions and folder structure.&#x20;**&#x41;ll you need described in the repository's README.
