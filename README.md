# Flipper One Documentation sources

![Flipper One Developer Portal](https://cdn.flipper.net/flipper-one-developer-portal-splash.jpg)

This repository is part of the [Flipper One — Docs](https://docs.flipper.net/one/resources/about-docs) sub-project (also called the Developer Portal). It contains the documentation source files used to generate the [Flipper One Developer Portal](https://docs.flipper.net/one).

## Links

* **Developer Portal:** [docs.flipper.net/one](https://docs.flipper.net/one)
* [**Sub-project overview**](https://docs.flipper.net/one/resources/about-docs)
* [**Task tracker**](https://github.com/orgs/flipperdevices/projects/10)
* [**Miro templates**](https://miro.com/app/board/uXjVJ6y839o=/)
* [**Figma templates**](https://www.figma.com/design/HcwlmmIJlW4LoiQu4RtwwH/Flipper-One-%E2%80%94-Docs?node-id=0-1&p=f&t=aYrPCUA166BloJuV-0)

## How to contribute

This repository contains the source files from which the Developer Portal is generated. You can contribute by editing existing pages and creating new ones.
1. Read [How to contribute](https://docs.flipper.net/one/resources/about-docs#how-to-contribute).
2. Fork this repository.
3. Edit Markdown files (Read the [Markup reference](https://docs.flipper.net/one/resources/about-docs/markup-reference)).
4. Create a pull request.

## Automation

Three GitHub Actions in [`.github/workflows/`](.github/workflows/) run automatically:

- **Update Open-tasks page** runs every hour. It runs the [`tools/generate_open_tasks.py`](tools/generate_open_tasks.py) script, which collects all issues labeled `help wanted` across all Flipper One repositories and regenerates [`docs/Open-tasks.md`](docs/Open-tasks.md) — published as the [Open Tasks](https://docs.flipper.net/one/open-tasks) page. Don't edit that file by hand.
- **Validate** runs on every pull request. It checks the documentation structure and scans for broken links before a PR is merged.
- **Test Open Tasks generator** runs when the generator, templates, or dependencies change.

  To run the Open Tasks generator locally, install the Python dependencies from [`requirements.txt`](requirements.txt) first.

## Publishing

Publishing is handled by Archbee's GitHub integration, not a GitHub Action. Every merge to the `public-release` branch triggers Archbee to rebuild and publish the live site at [docs.flipper.net/one](https://docs.flipper.net/one).

## Files structure

```
flipperone-docs/
├── .github/
│   └── workflows/
│       ├── test-open-tasks-generator.yml # Tests Open Tasks generator
│       ├── update-open-tasks.yml  # Regenerates Open-tasks.md
│       └── validate.yml           # Validates docs structure and links on PRs
├── archbee.json                   # Sidebar hierarchy + Archbee integration settings
├── README.md                      # Repository overview
├── tools/
│   └── generate_open_tasks.py     # Generates Open-tasks.md from GitHub issues
└── docs/
    ├── Welcome.md                 # Main page at docs.flipper.net/one
    ├── How-to-join.md
    ├── Open-tasks.md              # Auto-generated — do not edit manually
    ├── general/                   # Tech specs, controls, and features
    ├── hardware/                  # 🔌 Hardware sub-project
    ├── mechanics/                 # ⚙️ Mechanics sub-project
    ├── cpu-software/              # 🐧 Linux (CPU Software) sub-project
    ├── mcu-firmware/              # 🕹️ MCU Firmware sub-project
    ├── user-interface/            # 🎨 User Interface sub-project
    ├── testing/                   # 🧪 Testing sub-project
    ├── resources/
    │   ├── docs/                  # Docs sub-project
    │   └── rockchip/              # Rockchip RK3576 reference
    └── files/
        ├── pics/                  # Images and other assets
        └── icons/                 # OS / brand icons used in docs
```

Each section's pages are listed in the sidebar — see [`archbee.json`](archbee.json) for the full hierarchy.
