from tiptapparser import parse
from tests.testdata import test_data_values as td


def test_parse_simple_content():
    assert parse(td.simple_content_json) == td.simple_content_html


def test_parse_content_with_emphasis():
    assert parse(
        td.content_with_emphasis_json) == td.content_with_emphasis_html


def test_parse_content_with_lists():
    assert parse(td.content_with_lists_json) == td.content_with_lists_html
