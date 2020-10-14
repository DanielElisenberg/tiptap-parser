def parse(json):
    html_string = ''
    for content in json['content']:
        html_string += parse_content(content)
    return html_string


def parse_content(content):
    content_type = content['type']
    prefix = ''
    postfix = ''

    if content_type == 'heading':
        level = content['attrs']['level']
        prefix = f'<h{level}>'
        postfix = f'</h{level}>'
    elif content_type == 'paragraph':
        prefix = '<p>'
        postfix = '</p>'
    elif content_type == 'bullet_list':
        prefix = '<ul>'
        postfix = '</ul>'
    elif content_type == 'ordered_list':
        prefix = '<ol>'
        postfix = '</ol>'
    elif content_type == 'list_item':
        prefix = '<li>'
        postfix = '</li>'
    elif content_type == 'text':
        return content['text']
    else:
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
    return prefix + inner_content_string + end_marks + postfix


def handle_marks(active, content):
    content_marks = content.get("marks", [])
    current_marks = [mark['type'] for mark in content_marks]

    end_marks = [mark for mark in active if mark not in current_marks]
    new_marks = [mark for mark in current_marks if mark not in active]

    tag = {
        'bold': 'strong',
        'italic': 'em',
        'strike': 's',
        'underline': 'u'
    }

    new_marks_html = ''
    for mark in new_marks:
        new_marks_html += f'<{tag[mark]}>'
    end_marks_html = ''
    for mark in end_marks:
        end_marks_html += f'</{tag[mark]}>'

    return new_marks_html, end_marks_html, current_marks
