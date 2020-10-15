import json

with open('tests/testdata/testdata.json', 'r') as test_data_file:
    test_data = json.load(test_data_file)

    simple_content_json = test_data['simple_content_json']
    simple_content_html = test_data['simple_content_html']

    content_with_emphasis_json = test_data['content_with_emphasis_json']
    content_with_emphasis_html = test_data['content_with_emphasis_html']

    content_with_lists_json = test_data['content_with_lists_json']
    content_with_lists_html = test_data['content_with_lists_html']

    content_with_links_json = test_data['content_with_links_json']
    content_with_links_html = test_data['content_with_links_html']

    complex_content_json = test_data['complex_content_json']
    complex_content_html = test_data['complex_content_html']
