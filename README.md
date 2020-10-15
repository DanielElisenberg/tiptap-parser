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
