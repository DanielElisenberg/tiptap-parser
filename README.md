# tiptap-parser
tiptap-parser is a python3 module for parsing json-output from the [tiptap](https://github.com/ueberdosis/tiptap) editor into html. Storing or processing content on the back end is far easier with the json-structured html content tiptap supplies. If it's preferred to run python in the back end, this module should make converting the json back to html painless.



### Get started

Install with pip

```
pip install tiptap-parser
```


Then import into your project and parse your content:

```
from tiptapparser import parse

html_string = parse(json_content)
```

### Example

```
from tiptapparser import parse

tiptap_json = {
  "type": "doc",
  "content": [
    {
      "type": "heading",
      "attrs": {
        "level": 1
      },
      "content": [
        {
          "type": "text",
          "text": "this is a h1"
        }
      ]
    },
    {
      "type": "paragraph",
      "content": [
        {
          "type": "text",
          "text": "this is a paragraph."
        }
      ]
    },
    {
      "type": "heading",
      "attrs": {
        "level": 2
      },
      "content": [
        {
          "type": "text",
          "text": "here is a h2"
        }
      ]
    },
    {
      "type": "paragraph",
      "content": [
        {
          "type": "text",
          "text": "and then another paragraph"
        }
      ]
    }
  ]
}

html_content = parse(tiptap_json)
# html_content:
# "<h1>this is a h1</h1><p>this is a paragraph.</p><h2>here is a h2</h2><p>and then another paragraph</p>"
```
