---
title: Markup example
docTags: 
createdAt: Mon Feb 09 2026 20:59:11 GMT+0000 (Coordinated Universal Time)
updatedAt: Thu Mar 26 2026 16:54:08 GMT+0000 (Coordinated Universal Time)
---

This page contains examples of markup that can be used in this wiki.
It supports basic **Markdown**, but also includes some **Archbee-specific syntax**.

This wiki is powered by the [**Archbee documentation system**](https://archbee.com) and is connected to the public GitHub repository [**github.com/flipperdevices/flipper-one-docs**](https://github.com/flipperdevices/flipper-one-docs).
That means anyone can suggest edits to any page, and once the Flipper team approves them, the changes will appear in this documentation.&#x20;

## GitHub Sources

The source files for this wiki are stored in the [**github.com/flipperdevices/flipper-one-docs**](https://github.com/flipperdevices/flipper-one-docs).
To edit any page, create a **pull request** with your changes: [**FIX How to make a pull request to this wiki**]().

Each time a change is committed to the GitHub repository, the wiki is automatically rebuilt and updated on the website.

# Archbee Markup

This wiki supports **Markdown** formatting, but not all features are available.
In some cases, you’ll need to use **Archbee-specific tags**.

**Quick jump:**

- [**Headings**](./#headings)
- [**Text styles**](./#text-styles)
- [**Links**](./#links)
- [**Images**](./#images)
- [**Videos & audio**](./#videos)
- [**Lists**](./#lists)
- [**Tables**](./#tables)
- [**Code & syntax highlighting**](./#code--syntax-highlighting)
- [**Quotes & callouts**](./#quotes--callouts)
- [**Math**](./#math)
- [**Mermaid diagrams**](./#mermaid-diagrams)
- [**Rules, escapes, emoji**](./#rules-escapes-emoji)
- [**Archbee syntax**](./#testing-archbee-syntax)

***

## Headings

# H1 Heading

## H2 Heading

### H3 Heading \<- Can't go any lower

Paragraph under headings. Line breaks work with two spaces at end.
This is a second line.

***

## Text styles

- Regular text
- **bold**
- *italic*
- ***bold italic***
- ~~strikethrough~~
- `inline code`
- $10^6$
- $H\_2O$

Block of text with soft-wrap and hard-wrap differences.
This line intentionally ends with two spaces to force a break.

***

## Links

- Inline link: [**Archbee**](https://archbee.com)
- Autolink: [**https://example.com**](https://example.com)
- Anchor to a section: [**Jump to Tables**](./#tables)

***

## Images

Markdown images with alt + title:

![Remote placeholder banner](https://placehold.co/800x180/png?text=Remote+Banner+800x180 "Remote Banner")

Relative image path:

![Local image](files/pics/test-image.jpg "Local asset example")

## Archbee image resize and align

The only way to resize image is archbee syntax:

`::Image[]{src="files/pics/test-image.jpg" size="40" position="left" caption="This is caption of text image, resized to 40 px ang alignet to left"}`

::Image[]{src="files/pics/test-image.jpg" size="40" position="flex-start" caption="This is caption of text image, resized to 40 px ang alignet to left" sha="793d70a667b264bda4823ee16319f78736d5e070" initialPath="files/pics/test-image.jpg" githubPath="docs/files/pics/test-image.jpg" width="1200" height="630" darkWidth="1200" darkHeight="630"}

***

## Videos

**YouTube via linked thumbnail (common Markdown pattern):**

::embed[[![Watch the demo](https://img.youtube.com/vi/dQw4w9WgXcQ/hqdefault.jpg)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)[**https://www.youtube.com/watch?v=dQw4w9WgXcQ**](https://www.youtube.com/watch?v=dQw4w9WgXcQ)[**https://www.youtube.com/watch?v=dQw4w9WgXcQ**](https://www.youtube.com/watch?v=dQw4w9WgXcQ)[**https://www.youtube.com/watch?v=dQw4w9WgXcQ**](https://www.youtube.com/watch?v=dQw4w9WgXcQ)[**https://www.youtube.com/watch?v=dQw4w9WgXcQ**](https://www.youtube.com/watch?v=dQw4w9WgXcQ)[**https://www.youtube.com/watch?v=dQw4w9WgXcQ**](https://www.youtube.com/watch?v=dQw4w9WgXcQ)[**https://www.youtube.com/watch?v=dQw4w9WgXcQ**](https://www.youtube.com/watch?v=dQw4w9WgXcQ)[**https://www.youtube.com/watch?v=dQw4w9WgXcQ**](https://www.youtube.com/watch?v=dQw4w9WgXcQ)[**https://www.youtube.com/watch?v=dQw4w9WgXcQ**](https://www.youtube.com/watch?v=dQw4w9WgXcQ)[**https://www.youtube.com/watch?v=dQw4w9WgXcQ**](https://www.youtube.com/watch?v=dQw4w9WgXcQ)[**https://www.youtube.com/watch?v=dQw4w9WgXcQ**](https://www.youtube.com/watch?v=dQw4w9WgXcQ)[**https://www.youtube.com/watch?v=dQw4w9WgXcQ**](https://www.youtube.com/watch?v=dQw4w9WgXcQ)]{url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"}

***

## Lists

Unordered list:

- Item A
  - Nested A.1
    - Nested A.1.a
- Item B

Ordered list (start at 3):
3\. Three
4\. Four
5\. Five

Mixed list:

- First

1. Second (numbered inside bullets)

- Third

***

## Tables

Basic table:

<table isTableHeaderOn="true" columnWidths="220,220,221">
  <tr>
    <td>
      <p>Feature</p>
    </td>
    <td align="center">
      <p>Supported</p>
    </td>
    <td>
      <p>Notes</p>
    </td>
  </tr>
  <tr>
    <td>
      <p>Bold</p>
    </td>
    <td align="center">
      <p>✅</p>
    </td>
    <td>
      <p><strong>text</strong></p>
    </td>
  </tr>
  <tr>
    <td>
      <p>Italic</p>
    </td>
    <td align="center">
      <p>✅</p>
    </td>
    <td>
      <p><em>text</em></p>
    </td>
  </tr>
  <tr>
    <td>
      <p>Footnotes</p>
    </td>
    <td align="center">
      <p>✅</p>
    </td>
    <td>
      <p>See <a href=""><strong>below</strong></a></p>
    </td>
  </tr>
</table>

Table with images & links:

<table isTableHeaderOn="true" columnWidths="220,220,221">
  <tr>
    <td align="center">
      <p>Avatar</p>
    </td>
    <td>
      <p>User</p>
    </td>
    <td>
      <p>Link</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><img src="https://placehold.co/48x48" alt=""></p>
    </td>
    <td>
      <p><strong>Alice</strong></p>
    </td>
    <td>
      <p><a href="https://example.com/alice"><strong>Profile</strong></a></p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <p><img src="https://placehold.co/48x48" alt=""></p>
    </td>
    <td>
      <p><strong>Bob</strong></p>
    </td>
    <td>
      <p><a href="https://example.com"><strong>Website</strong></a></p>
    </td>
  </tr>
</table>

***

## Code & syntax highlighting

Inline: `const hi = "world";`

Fenced (JavaScript):

```javascript
export function greet(name) {
  return `Hello, ${name}!`;
}
console.log(greet("Archbee"));
```

Fenced (Python):

```python
def fib(n):
    a, b = 0, 1
    seq = []
    while len(seq) < n:
        a, b = b, a + b
        seq.append(a)
    return seq

print(fib(10))
```

Fenced (Bash):

```bash
#!/usr/bin/env bash
set -euo pipefail
curl -I https://archbee.com
```

Diff block:

```diff
+ Added line
- Removed line
! Changed line (not standard, but some themes show this)
```

JSON block:

```json
{
  "name": "archbee-md-test",
  "private": true,
  "scripts": { "start": "node index.js" }
}
```

YAML block:

```yaml
name: archbee-md-test
on:
  push:
    branches: [ main ]
```

***

## Quotes & callouts

Regular blockquote:

:::BlockQuote
“Documentation is a love letter that you write to your future self.” — Damian Conway
:::

GitHub/Docs-style admonitions (blockquote + label):

:::BlockQuote
\[!NOTE]
This is a note-style callout.
:::

:::BlockQuote
\[!TIP]
Tips can sit under the same block.
:::

:::BlockQuote
\[!IMPORTANT]
Important things deserve clear emphasis.
:::

:::BlockQuote
\[!WARNING]
Warnings highlight risky steps.
:::

:::BlockQuote
\[!CAUTION]
Use with care.
:::

:::BlockQuote
💡 **Tip:** Remember to save your work often.
:::

:::hint{type="info"}
### Heading inside a callout

Archbee uses its own syntax for callouts. Available styles: info, warning, success, danger.
:::

***

## Math

Inline math: $E=mc^2$ and $\alpha + \beta = \gamma$.

Display math (used Archbee syntax):

```tex
\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}
```

***

## Mermaid diagrams

Flowchart:

```mermaid
flowchart TD
  A[Start] --> B{Is it Markdown?}
  B -- Yes --> C[Render nicely]
  B -- No  --> D[Fallback]
  C --> E[Ship it]
  D --> E
```

Sequence diagram:

```mermaid
sequenceDiagram
  participant U as User
  participant S as System
  U->>S: Sends Markdown
  S-->>U: Renders page
```

***

## Rules, escapes, emoji

Horizontal rules:

***

***

***

Escaped characters: \*literal asterisks\*, \_underscores\_, \`backticks\`, #hash.

Emoji shortcodes: 🚀 🎉 ⚡ ⚠️

***

# Testing archbee syntax

## Flow with steps

::::WorkflowBlock
:::WorkflowBlockItem
Included subitems

1. Subitem 1
2. Subitem 2
:::

:::WorkflowBlockItem
Added text

Text body
:::

:::WorkflowBlockItem
Added image

![Local image](files/pics/test-image.jpg "Local asset example")
:::
::::

## Formula

```tex
int_0^infty x^2 dx
```

## Callouts

:::hint{type="info"}
Test
:::

:::hint{type="success"}

:::

:::hint{type="warning"}

:::

:::hint{type="danger"}

:::

## Vertical divider

::::VerticalSplit{layout="middle"}
:::VerticalSplitItem
**Left side**

Text
:::

:::VerticalSplitItem
**Right side**

Text
:::
::::

## Expandible text

:::ExpandableHeading
### Expandible heading

With text
More text

![Local image](files/pics/test-image.jpg "Even with a local image")
:::

***

# Testing  text properties

Text without color

Colored text (bold)

**Bold text using Markdown**
