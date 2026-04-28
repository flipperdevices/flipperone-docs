---
title: Markup example
slug: resources/about-docs/markup-example
docTags: 
createdAt: Sun Apr 26 2026 18:22:16 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 28 2026 13:28:23 GMT+0000 (Coordinated Universal Time)
---

This page is a reference for contributors writing Flipper One documentation.
It covers both standard **Markdown** and **Archbee-specific syntax** supported by this wiki.

The source files live on GitHub at [github.com/flipperdevices/flipper-one-docs](https://github.com/flipperdevices/flipper-one-docs). Every merged pull request automatically rebuilds the live site. To contribute, fork the repo and open a pull request.

**Quick jump:**

- :Link[Headings]{label="Headings" overridedLabel="Headings" spaceId docId="43g4bBZ9VHcuZq4Hl9m1e" version="v2" docAnchorId="#headings" loadingMethod="dynamic" newTab="false" href="Markup-example.md"}
- :Link[Text styles]{label="Text styles" overridedLabel="Text styles" spaceId docId="43g4bBZ9VHcuZq4Hl9m1e" version="v2" docAnchorId="#text-styles" loadingMethod="dynamic" newTab="false" href="Markup-example.md"}
- :Link[Links]{label="Links" overridedLabel="Links" spaceId docId="43g4bBZ9VHcuZq4Hl9m1e" version="v2" docAnchorId="#links" loadingMethod="dynamic" newTab="false" href="Markup-example.md"}
- :Link[Images]{label="Images" overridedLabel="Images" spaceId docId="43g4bBZ9VHcuZq4Hl9m1e" version="v2" docAnchorId="#images" loadingMethod="dynamic" newTab="false" href="Markup-example.md"}
- :Link[Videos]{label="Videos" overridedLabel="Videos" spaceId docId="43g4bBZ9VHcuZq4Hl9m1e" version="v2" docAnchorId="#videos" loadingMethod="dynamic" newTab="false" href="Markup-example.md"}
- :Link[Lists]{label="Lists" overridedLabel="Lists" spaceId docId="43g4bBZ9VHcuZq4Hl9m1e" version="v2" docAnchorId="#lists" loadingMethod="dynamic" newTab="false" href="Markup-example.md"}
- :Link[Tables]{label="Tables" overridedLabel="Tables" spaceId docId="43g4bBZ9VHcuZq4Hl9m1e" version="v2" docAnchorId="#tables" loadingMethod="dynamic" newTab="false" href="Markup-example.md"}
- :Link[Code]{label="Code" overridedLabel="Code" spaceId docId="43g4bBZ9VHcuZq4Hl9m1e" version="v2" docAnchorId="#code-syntax-highlighting" loadingMethod="dynamic" newTab="false" href="Markup-example.md"}
- :Link[Callouts]{label="Callouts" overridedLabel="Callouts" spaceId docId="43g4bBZ9VHcuZq4Hl9m1e" version="v2" docAnchorId="#callouts" loadingMethod="dynamic" newTab="false" href="Markup-example.md"}
- :Link[Math]{label="Math" overridedLabel="Math" spaceId docId="43g4bBZ9VHcuZq4Hl9m1e" version="v2" docAnchorId="#math" loadingMethod="dynamic" newTab="false" href="Markup-example.md"}
- :Link[Mermaid diagrams]{label="Mermaid diagrams" overridedLabel="Mermaid diagrams" spaceId docId="43g4bBZ9VHcuZq4Hl9m1e" version="v2" docAnchorId="#mermaid-diagrams" loadingMethod="dynamic" newTab="false" href="Markup-example.md"}
- :Link[Archbee components]{label="Archbee components" overridedLabel="Archbee components" spaceId docId="43g4bBZ9VHcuZq4Hl9m1e" version="v2" docAnchorId="#archbee-components" loadingMethod="dynamic" newTab="false" href="Markup-example.md"}

***

## Headings

Flipper One documentation supports headings H1–H3.

# # Heading 1

## ## Heading 2

### ### Heading 3

***

## Text styles

<table isTableHeaderOn="true" columnWidths="331,332">
  <tr>
    <td>
      <p><strong>Flipper One docs</strong></p>
    </td>
    <td>
      <p><strong>Markdown</strong></p>
    </td>
  </tr>
  <tr>
    <td>
      <p>Regular text</p>
    </td>
    <td>
      <p><code>Regular text</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Bold</strong></p>
    </td>
    <td>
      <p><code>**Bold**</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><em>Italic</em></p>
    </td>
    <td>
      <p><code>*Italic*</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><em><strong>Bold italic</strong></em></p>
    </td>
    <td>
      <p><code>***Bold italic***</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><del>Strikethrough</del></p>
    </td>
    <td>
      <p><code>~~Strikethrough~~</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>Inline code</code></p>
    </td>
    <td>
      <p><code>`Inline code`</code></p>
    </td>
  </tr>
</table>

***

## Links

<table isTableHeaderOn="true" columnWidths="331,332">
  <tr>
    <td>
      <p><strong>Flipper One docs</strong></p>
    </td>
    <td>
      <p><strong>Markdown</strong></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><a href="https://archbee.com">Archbee</a></p>
    </td>
    <td>
      <p><code>[Archbee](https://archbee.com)</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><a href="https://example.com">https://example.com</a></p>
    </td>
    <td>
      <p><code>[https://example.com](https://example.com)</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><a href="Markup-example.md">Jump to Tables</a></p>
    </td>
    <td>
      <p><code>[Jump to Tables](./#tables)</code></p>
    </td>
  </tr>
</table>

***

## Images

**Remote URL:** `![Alt text](https://example.com/image.png "Caption")`

![Remote image](https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=300\&h=120\&fit=crop "Caption")

‎&#x20;

**Local path:**  `![Alt text](files/pics/test-image.jpg "Caption")`

![Local image](https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/pNHUZHZzPZd7qdM08jKuq_test-image.jpg "Caption")

:::hint{type="info"}
**Caption alignment** depends on the image source, not the syntax:

- **Remote URL** — caption is rendered **centered**
- **Local path** — caption is rendered **left-aligned**
:::

​

To **resize or align** an image, standard Markdown is not enough — use Archbee syntax:

`::Image[]{src="files/pics/test-image.jpg" size="40" position="flex-start" caption="Caption text"}`

::Image[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/sDIW27SOFL0HZKEvDEU_T-20260420-092354.png" size="40" width="1950" height="1200" position="flex-start" caption="Caption text"}

<table isTableHeaderOn="true" columnWidths="141,522">
  <tr>
    <td>
      <p><strong>Attribute</strong></p>
    </td>
    <td>
      <p><strong>Description</strong></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>src</code></p>
    </td>
    <td>
      <p>Path to the image (relative or absolute URL).</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>size</code></p>
    </td>
    <td>
      <p>Width value in percent.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>position</code></p>
    </td>
    <td>
      <p>Page alignment when the image is smaller than the content area: <code>flex-start</code> (left), <code>center</code>, <code>flex-end</code> (right). Has no effect on caption alignment.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>caption</code></p>
    </td>
    <td>
      <p>An optional caption is shown below the image. Always left-aligned for local images.</p>
    </td>
  </tr>
</table>

‎&#x20;

### Inline images

You can add inline images to the text using Archbee syntax:

`:inlineImage[]{src="files/pics/icon_usb_c.png" alt caption="usb-c icon"}`

This is how an inline image :inlineImage[]{src="https://api.archbee.com/api/optimize/3StCFqarJkJQZV-7N79yY/WAXNm79eG0f7AQuFyuqy6-20260420-163829.png" alt caption} looks in text.

***

## Videos

Two methods to embed video are supported.

**Method 1: YouTube** — use Archbee's embed syntax:

`::embed[]{url="https://www.youtube.com/watch?v=VIDEO_ID"}`

::embed[]{url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"}

​

**Method 2: Self-hosted / CDN video** — use the Archbee `:::Iframe` component:

```html
:::Iframe{iframeHeight="500" code="
<video    
    autoplay muted loop playsinline style="width: 100%; margin: 0 !important;"
    src="https://cdn.example.com/your-video.mp4"
></video>"}
<div class="text-center mt-2.5 text-gray-400 pb-5">
Caption
</div>

:::
```

:::Iframe{code="<video&#xA;    autoplay muted loop playsinline style=&#x22;width: 100%; margin: 0 !important;&#x22;&#xA;    src=&#x22;https://cdn.flipperzero.one/Pan_rotate_and_move_parts_compressed.mp4&#x22;&#xA;></video>&#xA;<div class=&#x22;text-center mt-2.5 text-gray-400 pb-5&#x22;>&#xA;Caption&#xA;</div>" iframeHeight="500"}

:::

***

## Lists

<table isTableHeaderOn="true" columnWidths="330,330">
  <tr>
    <td>
      <p><strong>Flipper One docs</strong></p>
    </td>
    <td>
      <p><strong>Markdown</strong></p>
    </td>
  </tr>
  <tr>
    <td>
      <ul>
      <li>Item A
      <ul>
      <li>Nested A.1</li>
      </ul>
      </li>
      <li>Item B</li>
      </ul>
    </td>
    <td>
      <p><code>- Item A</code></p>
      <p><code>  - Nested A.1</code></p>
      <p><code>- Item B</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <ol>
      <li>First</li>
      <li>Second</li>
      <li>Third</li>
      </ol>
    </td>
    <td>
      <p><code>1. First</code></p>
      <p><code>2. Second</code></p>
      <p><code>3. Third</code></p>
    </td>
  </tr>
</table>

***

## Divider

Use `***` or `---` to insert a horizontal divider.

***

## Tables

Archbee supports two table formats.

**Standard Markdown pipe tables** — simple and readable, but no control over column widths or alignment:

```markdown
| Column 1 | Column 2 | Column 3 |
| --- | --- | --- |
| Cell | **Bold** | ✅ |
```

<table isTableHeaderOn="true" columnWidths="221,221,221">
  <tr>
    <td>
      <p><strong>Column 1</strong></p>
    </td>
    <td>
      <p><strong>Column 2</strong></p>
    </td>
    <td>
      <p><strong>Column 3</strong></p>
    </td>
  </tr>
  <tr>
    <td>
      <p>Cell</p>
    </td>
    <td>
      <p><strong>Bold</strong></p>
    </td>
    <td>
      <p>✅</p>
    </td>
  </tr>
</table>

​ 

**HTML tables** — use when you need column widths, cell alignment, or images inside cells:

```html
<table isTableHeaderOn="true" columnWidths="165,330,165">
  <tr>
    <td><p>Header 1</p></td>
    <td><p>Header 2</p></td>
    <td align="center"><p>Header 3</p></td>
  </tr>
  <tr>
    <td><p>Cell</p></td>
    <td><p><strong>Bold cell</strong></p></td>
    <td align="center"><p>✅</p></td>
  </tr>
</table>
```

<table isTableHeaderOn="true" columnWidths="165,330,165">
  <tr>
    <td>
      <p><strong>Attribute</strong></p>
    </td>
    <td>
      <p><strong>Description</strong></p>
    </td>
    <td>
      <p><strong>Example</strong></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>isTableHeaderOn</code></p>
    </td>
    <td>
      <p>Renders the first row as a bold header</p>
    </td>
    <td>
      <p><code>"true"</code> / <code>"false"</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>columnWidths</code></p>
    </td>
    <td>
      <p>Comma-separated pixel widths per column. Total must not exceed 660 px</p>
    </td>
    <td>
      <p><code>"165,330,165"</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>align</code></p>
    </td>
    <td>
      <p>Horizontal alignment on a <code>&#x3C;td></code> element</p>
    </td>
    <td>
      <p><code>align="center"</code></p>
    </td>
  </tr>
</table>

***

## Code & syntax highlighting

**Fenced block with language:**

````markdown
```javascript
function greet(name) {
  return `Hello, ${name}!`;
}
```
````

```javascript
function greet(name) {
  return `Hello, ${name}!`;
}
```

​

**Diff block:**

````markdown
```diff
+ Added line
- Removed line
```
````

```diff
+ Added line
- Removed line
```

Supported language tags: `markdown`, `html`, `javascript`, `typescript`, `python`, `bash`, `c`, `cpp`, `json`, `yaml`, `diff`, `tex`, `mermaid`, and more.

***

## Callouts

Archbee supports four callout styles using `:::hint{type="..."}`:

```markdown
:::hint{type="info"}
Your text for the **info callout** here
:::
```

:::hint{type="info"}
Your text for the **info callout** here
:::

‎&#x20;

```markdown
:::hint{type="success"}
Your text for the **success callout** here
:::
```

:::hint{type="success"}
Your text for the **success callout** here
:::

‎&#x20;

```markdown
:::hint{type="warning"}
Your text for the **warning callout** here
:::
```

:::hint{type="warning"}
Your text for the **warning callout** here
:::

‎&#x20;

```markdown
:::hint{type="danger"}
Your text for the **danger callout** here
:::
```

:::hint{type="danger"}
Your text for the **danger callout** here
:::

***

## Math

Archbee only supports math via a fenced `tex` block. Inline math (`$...$`) is **not supported**.

````markdown
```tex
\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}
```
````

```tex
\int_{-\infty}^{\infty} e^{-x^2} \, dx = \sqrt{\pi}
```

***

## Mermaid diagrams

Use a fenced `mermaid` block. Supported diagram types: `flowchart`, `sequenceDiagram`, `classDiagram`, `gantt`, and more.

```none
flowchart TD
  A[Start] --> B{Is it Markdown?}
  B -- Yes --> C[Render nicely]
  B -- No  --> D[Fallback]
  C --> E[Ship it]
  D --> E
```

```mermaid
flowchart TD
  A[Start] --> B{Is it Markdown?}
  B -- Yes --> C[Render nicely]
  B -- No  --> D[Fallback]
  C --> E[Ship it]
  D --> E
```

​

```none
sequenceDiagram
  participant U as User
  participant S as System
  U->>S: Sends Markdown
  S-->>U: Renders page
```

```mermaid
sequenceDiagram
  participant U as User
  participant S as System
  U->>S: Sends Markdown
  S-->>U: Renders page
```

***

## Archbee components

### Workflow steps

Use `WorkflowBlock` with `WorkflowBlockItem` for numbered step-by-step flows:

```markdown
::::WorkflowBlock
:::WorkflowBlockItem
Step one title

Step description.
:::

:::WorkflowBlockItem
Step two title

Step description.
:::
::::
```

::::WorkflowBlock
:::WorkflowBlockItem
Step one title

Step description.
:::

:::WorkflowBlockItem
Step two title

Step description.
:::
::::

***

### Two-column layout

Use `VerticalSplit` to place content side by side:

```markdown
::::VerticalSplit{layout="middle"}
:::VerticalSplitItem
**Left side**

Content
:::

:::VerticalSplitItem
**Right side**

Content
:::
::::
```

::::VerticalSplit{layout="middle"}
:::VerticalSplitItem
**Left side**

Content
:::

:::VerticalSplitItem
**Right side**

Content
:::
::::

***

### Expandable section

Use `ExpandableHeading` for collapsible content:

```markdown
:::ExpandableHeading
### Section title

Content shown when expanded.
:::
```

:::ExpandableHeading
### Section title

Content shown when expanded.
:::

