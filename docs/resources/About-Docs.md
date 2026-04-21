---
title: About Docs
slug: resources/docs
docTags: 
createdAt: Mon Apr 20 2026 11:30:48 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 21 2026 16:15:49 GMT+0000 (Coordinated Universal Time)
---

This page explains how the Docs sub-project works — how the Developer Portal is structured, how source files are stored and published, and how you can contribute.

\<image placeholder>

The Docs sub-project covers all documentation for Flipper One: this wiki, technical specs, datasheets, guides, and contribution instructions. Like all other Flipper One sub-projects, it is open for community contribution.

The Docs sub-project consists of:

- ✅ :Link[Task tracker]{href="https://github.com/orgs/flipperdevices/projects/10" newTab="true" hasDisabledNofollow="true"}
- 📁 :Link[Source Markdown files on GitHub]{href="https://github.com/flipperdevices/flipperone-docs" newTab="true" hasDisabledNofollow="true"}
- 📊 :Link[Diagrams on Miro]{href="https://miro.com/app/board/uXjVJ6y839o=/?moveToWidget=3458764666602002588&cot=10" newTab="true" hasDisabledNofollow="true"}
- 🎨 :Link[Illustrations on Figma]{href="https://www.figma.com/design/HcwlmmIJlW4LoiQu4RtwwH/Flipper-One-%E2%80%94-Docs?node-id=71-3&t=56y5oAygKLBg3nGe-1" newTab="true" hasDisabledNofollow="true"}

We'd love your feedback and help — look for tasks tagged **help wanted** in the task tracker, or contribute directly to the Docs GitHub repository via pull requests.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/CekWx_z_PDlUOfCesCeYO-20260421-161345.jpg)

***

# How the Developer Portal works

The Flipper One Developer Portal is hosted on [**Archbee**](https://archbee.com), but all source files live in the :Link[flipper-one-docs GitHub repository]{href="https://github.com/flipperdevices/flipper-one-docs" newTab="true" hasDisabledNofollow="false"} — made possible by Archbee's GitHub integration. Diagrams, screenshots, and illustrations are created in Miro and Figma, then exported to the repository alongside the Markdown.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/HewLM9f9czM5cdbaLMptM-20260421-155957.jpg "Draft")

:::hint{type="info"}
**In short:** GitHub is the source of truth for all text, images, and page hierarchy. Archbee reads from GitHub and renders the live site at :Link[docs.flipper.net/one]{href="https://docs.flipper.net/one" newTab="true" hasDisabledNofollow="false"}.
:::

Whenever a pull request is merged into the `public-release` branch, Archbee automatically rebuilds the site with the changes.

***

# Repository structure

The repository contains the source files for the entire Developer Portal:

```none
flipperone-docs/
├── .archbee.json          # Archbee integration settings
├── README.md              # Repository overview
├── tools/
│   └── generate_open_tasks.py  # Generates Open-tasks.md from GitHub issues
└── docs/
    ├── Welcome.md         # Main page at docs.flipper.net/one
    ├── Summary.md         # Controls the sidebar hierarchy
    ├── How-to-join.md
    ├── Open-tasks.md      # Auto-generated — do not edit manually
    ├── files/
    │   └── pics/          # Images and other assets
    ├── general/
    ├── hardware/
    ├── mechanics/
    ├── mcu-firmware/
    ├── cpu-software/
    ├── user-interface/
    ├── testing/
    └── resources/
```

***

## How Summary.md works

`Summary.md` defines the left sidebar (table of contents) of the Developer Portal. It defines sections, page names, file paths, and nesting levels. Ideally, nesting should not go deeper than two levels.

When adding a new page, always update :Link[docs/Summary.md ]{href="https://github.com/flipperdevices/flipperone-docs/blob/public-release/docs/Summary.md" newTab="true" hasDisabledNofollow="false"}to include it. Without this, the page will not appear in the sidebar, and readers won't be able to find it.

### Syntax

The file uses nested Markdown bullet lists with ## category headings. For example:

```markdown
- [Welcome](Welcome.md)
- [How to join](How-to-join.md)

## 🔌 Hardware
- [About Hardware](hardware/About-Hardware.md)
- [GPIO port](hardware/GPIO-port.md)
- [Expansion modules](hardware/modules/Expansion-modules.md)
  - [GPIO modules](hardware/modules/GPIO-Modules.md)
  - [M.2 modules](hardware/modules/M2-Modules.md)
```

‎&#x20;

### Rules

- A bullet of the form `- [Title](path.md)` becomes a navigable page. The path is relative to the `docs/` folder.
- A `## Heading` line becomes a category group that visually separates sections (for example, `## Hardware`).
- Indented bullets (two spaces per level) become sub-pages nested under the parent page.
- Emojis in titles render as-is in the sidebar. They are purely cosmetic and used for quick visual scanning.

:::hint{type="info"}
**Page names in the sidebar** come from the first H1 heading (`#`) in the `.md` file — not from the square brackets in `Summary.md`. Keep page titles short so they fit comfortably in the sidebar.

This is a known issue — we notified Archbee.
:::

‎&#x20;

### How to add a new page

1. Create the `.md` file under `docs/...`
2. Add a bullet to `Summary.md` at the right place in the hierarchy.
3. Open a pull request. The live site rebuilds on merge.

If you forget step 3, the page may publish without the correct sidebar position. Always update both files in the same pull request.

***

# ✅ Task tracker

All Docs sub-project tasks are tracked in the GitHub project [**Flipper One — Docs**](https://github.com/orgs/flipperdevices/projects/10). There, you can see what the team is working on and find open tasks where the community can help.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/thnPuI0oZ2C2o4ekvaFP2-20260421-151307.jpg "Update for the Docs sub-project")

Tasks labeled **help wanted** are open for contribution. You're welcome to join discussions or submit changes — just read the contribution guide below first.

***

# 📊 Diagrams on Miro

All diagrams used in the Developer Portal, architecture overviews, flow charts, and conceptual visuals are designed on the [**Flipper One — Docs Miro board**](https://miro.com/app/board/uXjVJ6y839o=/).

The board is publicly viewable: anyone can open it, inspect a diagram, and export a copy for reference or offline editing. Once a diagram is finalized, it's exported as an image and committed to `docs/files/pics/` in the repository — that exported file is what actually renders in the live docs.

:::hint{type="info"}
Spotted an error or have an idea for a new diagram? Share them with us in a :Link[pull request]{href="https://docs.flipper.net/one/about-docs#share-fixes-and-guides-as-a-pull-request" newTab="true" hasDisabledNofollow="false"}.
:::

***

# 🎨 Illustrations on Figma

Illustrations used across the Developer Portal — section illustrations and decorative graphics are designed in the [**Flipper One — Docs Figma file**](https://www.figma.com/design/HcwlmmIJlW4LoiQu4RtwwH/Flipper-One-%E2%80%94-Docs).

Like the Miro board, the Figma file is publicly viewable: you can browse every frame, inspect layers, and export illustrations at any resolution. Finalized illustrations are exported to `docs/files/pics/` in the repository, which is what the live site renders.

:::hint{type="info"}
Have an idea for a new illustration or a tweak to an existing one? Share them with us in a :Link[pull request]{href="https://docs.flipper.net/one/about-docs#share-fixes-and-guides-as-a-pull-request" newTab="true" hasDisabledNofollow="false"}.
:::

***

# How to contribute

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/HX3LlC7T8p5Y5nP3T41Em-20260421-141111.jpg)

Anyone can contribute to the Docs sub-project via GitHub by commenting on the open tasks or making pull requests with fixes and guides:

- :Link[Comment on an open task]{href="https://docs.flipper.net/one/about-docs#comment-on-an-open-task" newTab="false" hasDisabledNofollow="true"}
- :Link[Share fixes and guides as a pull request]{href="https://docs.flipper.net/one/about-docs#share-fixes-and-guides-as-a-pull-request" newTab="false" hasDisabledNofollow="true"}

***

## Comment on an open task

::::hint{type="info"}
**⚠️ Contributions only — no flooding**

To keep collaboration productive, please keep comments on-topic. Open tasks are for contribution-related discussion only. If you have an idea or concern, first turn it into a concrete contribution and share it as a comment on a task. For general questions or discussions, you’re always welcome to join the conversation on :Link[social media]{href="https://x.com/Flipper_RND" newTab="true" hasDisabledNofollow="false"} or :Link[Discord]{href="https://discord.com/invite/flipper" newTab="true" hasDisabledNofollow="false"}!

:::Paragraph{indent="1"}
**Bad vs good comments:**
:::

:::Paragraph{indent="1"}
❌ — I don't like this section
👍 — Step 2 should remind readers to check the "Update GitHub PR" box
:::
::::

‎&#x20;

Open tasks that need the community's help are labeled **help wanted**. If you have ideas on how to improve the guide, you can contribute by commenting on the task and attaching screenshots, videos, or links:

:::::WorkflowBlock
:::WorkflowBlockItem
In the :Link[Docs GitHub project]{href="https://github.com/orgs/flipperdevices/projects/10" newTab="true" hasDisabledNofollow="false"}, click the open task you want to contribute to.
:::

::::WorkflowBlockItem
In the comments section, clearly write your comment, and if necessary, attach a screenshot, video, or a link.

:::hint{type="info"}
**Important:** If you share a link, ensure the content is accessible to others.
:::

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/HW8_FuiKf7SdOnTpe77VY-20260421-142833.png)

**Attachment size limit:**

- Images: 10 MB
- Videos: 100 MB
::::

:::WorkflowBlockItem
Click **Comment**.
:::
:::::

We review all comments carefully! We may ask additional questions about your idea in the task thread, so please follow notifications from GitHub in your email.

***

## Share fixes and guides as a pull request

Anyone can contribute to the Flipper One documentation via GitHub — fork the repository, make your changes, and open a pull request:

:::::WorkflowBlock
:::WorkflowBlockItem
Read the [**Markup example**](https://docs.flipper.net/one/markup-example) page to learn the supported Markdown and Archbee syntax before writing or editing pages.
:::

:::WorkflowBlockItem
Go to the [**flipper-one-docs**](https://github.com/flipperdevices/flipper-one-docs) repository on GitHub and fork it to your account by clicking the **Fork** button in the upper-right corner.

![](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/lbp-PmXVHpP_Th11IKb0Q-20260421-151341.png "Update for the Docs sub-project")
:::

:::WorkflowBlockItem
In your forked repository, find the `.md` file you want to edit under `docs/`, or create a new one in the appropriate subfolder.
:::

::::WorkflowBlockItem
(Optional) If you are **adding a new page**, you can also edit :Link[docs/Summary.md]{href="https://github.com/flipperdevices/flipperone-docs/blob/public-release/docs/Summary.md" newTab="true" hasDisabledNofollow="false"} to add it to the sidebar hierarchy.

:::hint{type="info"}
It's okay if you don't do it — we'll update this file after merging your PR with a new page.
:::
::::

::::WorkflowBlockItem
Commit your changes to a new branch in your fork.

:::hint{type="info"}
Name the branch to reflect your GitHub nickname and the area of changes. For example: `john/GitHub-integration-update`

Make a commit description concise and clear. For example: `Update: rename authentication to auth`
:::
::::

:::WorkflowBlockItem
Open a pull request to the `public-release` branch of the original repository. Add a clear title and description explaining what you changed.
:::
:::::

Once your pull request is merged, Archbee automatically picks up the changes and rebuilds the live site at [**docs.flipper.net/one**](https://docs.flipper.net/one).
