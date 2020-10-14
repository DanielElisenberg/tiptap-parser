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
    elif content_type == 'text':
        return content['text']
    else:
        return ''
    
    inner_content_string = ''
    for inner_content in content['content']:
        inner_content_string += parse_content(inner_content)
    
    return prefix + inner_content_string + postfix
