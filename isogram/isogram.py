import re


def is_isogram(string):
    only_text = re.sub('[^a-z]', '', string.lower())
    for i in range(len(only_text) - 1):
        if only_text[i] in only_text[i + 1:]:
            return False
    return True
