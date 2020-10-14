parse_dict = {
    'heading1': {
        'prefix': '<h1>',
        'postfix': '</h1>'
    },
    'heading2': {
        'prefix': '<h2>',
        'postfix': '</h2>'
    },
    'heading3': {
        'prefix': '<h3>',
        'postfix': '</h3>'
    },
    'paragraph': {
        'prefix': '<p>',
        'postfix': '</p>'
    },
    'bullet_list': {
        'prefix': '<ul>',
        'postfix': '</ul>'
    },
    'ordered_list': {
        'prefix': '<ol>',
        'postfix': '</ol>'
    },
    'list_item': {
        'prefix': '<li>',
        'postfix': '</li>'
    },
    'bold': {
        'prefix': '<strong>',
        'postfix': '</strong>'        
    },
    'italic': {
        'prefix': '<em>',
        'postfix': '</em>'
    },
    'strike': {
        'prefix': '<s>',
        'postfix': '</s>'
    },
    'underline': {
        'prefix': '<u>',
        'postfix': '</u>'
    }
}


def parse(json):
    html_string = ''
    for content in json['content']:
        html_string += parse_content(content)
    return html_string


def parse_content(content):
    content_type = content['type']
    if content_type == 'text':
        return content['text']

    try:
        level = content['attrs']['level']
        print(f'{content_type}{level}')
        content_type = f'{content_type}{level}'
    except Exception:
        pass

    try:
        content_tags = parse_dict[content_type]
    except Exception:
        return ''

    inner_content_string = ''
    active_marks = []
    for inner_content in content['content']:
        new_marks, end_marks, active_marks = handle_marks(
            active_marks, inner_content
        )
        inner_content_string += end_marks + new_marks
        inner_content_string += parse_content(inner_content)

    _, end_marks, _ = handle_marks(active_marks, {})
    return content_tags['prefix'] + \
        inner_content_string + end_marks + content_tags['postfix']


def handle_marks(active, content):
    content_marks = content.get("marks", [])
    current_marks = [mark['type'] for mark in content_marks]
    end_marks = [mark for mark in active if mark not in current_marks]
    new_marks = [mark for mark in current_marks if mark not in active]

    new_marks_html = ''
    for mark in new_marks:
        new_marks_html += f'{parse_dict[mark]["prefix"]}'

    end_marks_html = ''
    for mark in end_marks:
        end_marks_html += f'{parse_dict[mark]["postfix"]}'

    return new_marks_html, end_marks_html, current_marks
