# This is general/test.md

code snippet:

```jsx
const App = () => {
  const editor = useMemo(() => withReact(createEditor()), [])
  const [value, setValue] = useState([
    {
      type: 'paragraph',
      children: [{ text: 'A line of text in a paragraph.' }],
    },
  ])

  return (
    <Slate editor={editor} value={value} onChange={value => setValue(value)}>
      <Editable />
    </Slate>
  )
}
```

:::Iframe{iframeHeight="0" code="<iframe src=&#x22;https://cad.onshape.com/documents/879fe9690e62f5a30ab284c9/w/c8500e686f485a7334741fc5/e/bb24b78e6696b3fb234bd8f6?renderMode=0&uiState=68ecf32ac7e8d1839d3ba67d&#x22; width=&#x22;800&#x22; height=&#x22;600&#x22; frameborder=&#x22;0&#x22; allowfullscreen></iframe>"}

:::

