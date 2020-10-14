from tiptapparser import parse
from tests.testdata import test_data_values as td

def test_parse():
    assert parse(td.simple_content_json) == td.simple_content_html

