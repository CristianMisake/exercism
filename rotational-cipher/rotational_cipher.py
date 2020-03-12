def rotate(text, key):
    resp = ''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters_u = letters.upper()
    for t in text:
        if t in letters:
            index = letters.index(t) + key
            new_index = (index if index < 26 else index - 26)
            resp += letters[new_index]
        else:
            if t in letters_u:
                index = letters_u.index(t) + key
                new_index = (index if index < 26 else index - 26)
                resp += letters_u[new_index]
            else:
                resp += t
    return resp
