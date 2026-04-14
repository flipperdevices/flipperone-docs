---
title: Markup example
slug: resources/docs/markup-example
docTags: 
createdAt: Wed Apr 08 2026 17:29:37 GMT+0000 (Coordinated Universal Time)
updatedAt: Tue Apr 14 2026 15:00:29 GMT+0000 (Coordinated Universal Time)
---

# Markup Reference

This page is a reference for contributors writing Flipper One documentation.
It covers both standard **Markdown** and **Archbee-specific syntax** supported by this wiki.

The source files live on GitHub at [**github.com/flipperdevices/flipper-one-docs**](https://github.com/flipperdevices/flipper-one-docs). Every merged pull request automatically rebuilds the live site. To contribute, fork the repo and open a pull request.

**Quick jump:**

- [**Headings**](./#headings)
- [**Text styles**](./#text-styles)
- [**Links**](./#links)
- [**Images**](./#images)
- [**Videos**](./#videos)
- [**Lists**](./#lists)
- [**Tables**](./#tables)
- [**Code**](./#code--syntax-highlighting)
- [**Callouts**](./#callouts)
- [**Math**](./#math)
- [**Mermaid diagrams**](./#mermaid-diagrams)
- [**Archbee components**](./#archbee-components)

***

## Headings

Flipper One documentation supports headings H1–H3.

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
      <h1>Heading 1</h1>
    </td>
    <td>
      <p><code># Heading H1</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <h2>Heading 2</h2>
    </td>
    <td>
      <p><code>## Heading H2</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <h3>Heading 3</h3>
    </td>
    <td>
      <p><code>### Heading H3</code></p>
    </td>
  </tr>
</table>

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
      <p><a href="https://archbee.com"><strong>Archbee</strong></a></p>
    </td>
    <td>
      <p><code>[Archbee](https://archbee.com)</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><a href="https://example.com"><strong>https://example.com</strong></a></p>
    </td>
    <td>
      <p><code>[https://example.com](https://example.com)</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><a href="Markup-example.md"><strong>Jump to Tables</strong></a></p>
    </td>
    <td>
      <p><code>[Jump to Tables](./#tables)</code></p>
    </td>
  </tr>
</table>

***

## Images

Standard Markdown image syntax:

<table isTableHeaderOn="true" columnWidths="119,360,184">
  <tr>
    <td>
    </td>
    <td>
      <p><strong>Flipper One docs</strong></p>
    </td>
    <td>
      <p><strong>Markdown</strong></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Remote URL</strong></p>
    </td>
    <td>
      <p><img src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=300&#x26;h=120&#x26;fit=crop" alt="Remote image"></p>
    </td>
    <td>
      <p><code>![Alt text](https://example.com/image.png "Title")</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <p><strong>Local path</strong></p>
    </td>
    <td>
      <hr>
      <p><img src="files/pics/test-image.jpg" alt="Local image"></p>
    </td>
    <td>
      <p><code>![Alt text](files/pics/test-image.jpg "Title")</code></p>
    </td>
  </tr>
</table>



:::hint{type="info"}
**Caption alignment** depends on the image source, not the syntax:

- **Remote URL** — caption is rendered **centered**
- **Local path** — caption is rendered **left-aligned**
:::

​

To **resize or align** an image, standard Markdown is not enough — use Archbee syntax:

`::Image[]{src="files/pics/test-image.jpg" size="40" position="flex-start" caption="Caption text"}`

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
      <p>Path to the image (relative or absolute URL)</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>size</code></p>
    </td>
    <td>
      <p>Width value (exact unit unclear — likely a percentage of the content area)</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>position</code></p>
    </td>
    <td>
      <p>Page alignment when image is smaller than content area: <code>flex-start</code> (left), <code>center</code>, <code>flex-end</code> (right). Has no effect on caption alignment.</p>
    </td>
  </tr>
  <tr>
    <td>
      <p><code>caption</code></p>
    </td>
    <td>
      <p>Optional caption shown below the image. Always left-aligned for local images.</p>
    </td>
  </tr>
</table>

***

## Videos

Two ways to embed video are supported.

**YouTube** — use Archbee's embed syntax:

`::embed[]{url="https://www.youtube.com/watch?v=VIDEO_ID"}`

::embed[]{url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"}

​

**Self-hosted / CDN video** — use the Archbee `:::Iframe` component:

```html
:::Iframe{iframeHeight="500" code="
<video    
    autoplay muted loop playsinline style="width: 100%; margin: 0 !important;"
    src="https://cdn.example.com/your-video.mp4"
></video>"}

:::
```

:::Iframe{iframeHeight="500" code="<video&#xA;    autoplay muted loop playsinline style=&#x22;width: 100%; margin: 0 !important;&#x22;&#xA;    src=&#x22;https://cdn.flipperzero.one/Pan_rotate_and_move_parts_compressed.mp4&#x22;&#xA;></video>"}

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
      <p><code>- Item A</code>
      <code>  - Nested A.1</code>
      <code>- Item B</code></p>
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
      <p><code>1. First</code>
      <code>2. Second</code>
      <code>3. Third</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <ul class="contains-task-list">
      <li class="task-list-item"><input type="checkbox" disabled> Item B</li>
      <li class="task-list-item"><input type="checkbox" disabled> Item A</li>
      </ul>
    </td>
    <td>
      <p><code>[] Item A</code>
      <code>[] Item B</code></p>
    </td>
  </tr>
</table>

***

## Divider

Use `***` or `---` to insert a horizontal divider:

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
      <p><code>"110,440,110"</code></p>
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

Supported language tags: `javascript`, `typescript`, `python`, `bash`, `c`, `cpp`, `json`, `yaml`, `diff`, `tex`, `mermaid`.

***

## Callouts

Archbee supports four callout styles using `:::hint{style="..."}`:

:::hint{type="info"}
**info** — General information or context.

`:::hint{style="info"} Your text here :::`
:::

:::hint{type="success"}
**success** — Positive outcome or confirmation.

`:::hint{style="success"} Your text here :::`
:::

:::hint{type="warning"}
**warning** — Something to be careful about.

`:::hint{style="warning"} Your text here :::`
:::

:::hint{type="danger"}
**danger** — Risk of data loss or breaking change.

`:::hint{style="danger"} Your text here :::`
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

