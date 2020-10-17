tag_for = {
    'heading1': 'h1',
    'heading2': 'h2',
    'heading3': 'h3',
    'paragraph': 'p',
    'bullet_list': 'ul',
    'ordered_list': 'ol',
    'list_item': 'li',
    'bold': 'strong',
    'italic': 'em',
    'strike': 's',
    'underline': 'u',
    'link': 'a',
    'horizontal_rule': 'hr',
    'hard_break': 'br'
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
    if content_type in ['horizontal_rule', 'hard_break']:
        return f'<{tag_for[content_type]}>'

    try:
        level = content['attrs']['level']
        content_type = f'{content_type}{level}'
    except Exception:
        pass

    try:
        content_tag = tag_for[content_type]
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
    return f'<{content_tag}>' + inner_content_string \
        + end_marks + f'</{content_tag}>'


def handle_marks(active, content):
    content_marks = content.get("marks", [])
    current_marks = [mark for mark in content_marks]
    end_marks = [mark for mark in active if mark not in current_marks]
    new_marks = [mark for mark in current_marks if mark not in active]

    new_marks_html = ''
    for mark in new_marks:
        mark_type = mark['type']
        attributes = ''
        try:
            attributes += handle_mark_attributes(mark['attrs'])
        except Exception:
            pass
        new_marks_html += f'<{tag_for[mark_type]}{attributes}>'

    end_marks_html = ''
    for mark in end_marks:
        mark_type = mark['type']
        end_marks_html += f'</{tag_for[mark_type]}>'

    return new_marks_html, end_marks_html, current_marks


def handle_mark_attributes(attributes):
    attributes_html_string = ''
    for key, val in attributes.items():
        attributes_html_string += f' {key}="{val}"'
    return attributes_html_string
