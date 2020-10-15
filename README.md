# tiptap-parser
tiptap-parse is a python3 library for parsing json-output from the tiptap editor into html. Storing or processing content on the back end is far easier with the json-structured html content tiptap supplies. If it's preferred to run python in the back end, this library will make converting the json back to html painless.



### Get started

Install with pip

```
pip install tiptap-parse
```


import into your project and parse away:

```
from tiptapparse import parse

html_string = parse(json_content)
```

