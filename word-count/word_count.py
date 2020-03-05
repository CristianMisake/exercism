import re


def count_words(sentence):
    array_count = {}
    # print(re.sub('^.\'', ' ', sentence.lower()).split())
    split_array = re.sub('[^a-zA-Z\'0-9]', ' ', sentence.lower()).split()
    for word in split_array:
        # caso especial con las ''
        groups_word = re.search('\'+(.+[^\'])\'+', word)
        if groups_word is not None:
            word = groups_word.group(len(groups_word.groups()))
        # verificar si la palabra ya fue usada para sumarla o crearla
        if word in list(array_count.keys()):
            array_count[word] += 1
        else:
            array_count[word] = 1
    return array_count
