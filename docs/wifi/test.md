# This is wifi/test.md

Cool, now when a key is pressed in the editor, its corresponding keycode is logged in the console.

![](files/pics/scam_cars.jpg)

::Image[]{src="files/pics/scam_cars.jpg" size="70" width="698" height="294" position="center" caption}

::Image[]{src="files/pics/scam_cars.jpg" size="50" position="center" caption width="698" height="294" darkWidth="698" darkHeight="294"}

::Image[]{src="files/pics/scam_cars.jpg" size="50" position="left" caption="This is caption"}

Now we want to make it actually change the content. For the purposes of our example, let's implement turning all ampersand, `&`, keystrokes into the word `and` upon being typed.

Our `onKeyDown` handler might look like this:

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
      <Editable
        onKeyDown={event => {
          if (event.key === '&') {
            // Prevent the ampersand character from being inserted.
            event.preventDefault()
            // Execute the `insertText` method when the event occurs.
            editor.insertText('and')
          }
        }}
      />
    </Slate>
  )
}
```

