import re


def abbreviate(words):
    acronym = ''
    for word in re.sub('[^A-Z \']', ' ', words.upper()).split():
        acronym += word[0]
    return acronym
