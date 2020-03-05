import re


def parse(markdown):
    html = ''
    lines = markdown.split('\n')
    in_list = False
    i = 0
    for line in lines:
        # buscar strong y em
        new_line = strong(line)
        new_line = em(new_line)
        # en caso de lista
        other_line = h(new_line)
        if new_line != other_line:
            # cerrar ul
            if in_list:
                html += '</ul>'
            html += other_line
        else:
            other_line = ul(new_line, in_list)
            if new_line != other_line:
                html += other_line
                in_list = True
                # cerrar ul
                if i == len(lines) - 1:
                    html += '</ul>'
            else:
                # cerrar ul
                if in_list:
                    html += '</ul>'
                html += "{}{}{}".format('<p>', new_line, '</p>')
        i += 1
    return html


def em(word):
    return re.sub('_(.+)_', r'<em>\1</em>', word)


def strong(word):
    return re.sub('__(.+)__', r'<strong>\1</strong>', word)


def h(word):
    regex = '#+ (.+)'
    if re.match(regex, word) is not None:
        n = len(word.split()[0])
        return re.sub(regex, r'<h{}>\1</h{}>'.format(n, n), word)
    return word


def ul(word, is_list):
    regex = r'\* (.+)'
    if is_list:
        text = r'<li>\1</li>'
    else:
        text = r'<ul><li>\1</li>'
    if re.match(regex, word) is not None:
        return re.sub(regex, text, word)
    return word
