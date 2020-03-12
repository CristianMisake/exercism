import re


def decode(string):
    # case length is 0
    if len(string) == 0:
        return ''
    # decode
    resp = ''
    number = ''
    for s in string:
        if re.match('[0-9]+', s):
            number = int('{}{}'.format(number, s))
        else:
            if number == '':
                resp += s
            else:
                resp += s * number
                number = ''
    return resp


def encode(string):
    # case length is 0
    if len(string) == 0:
        return ''
    # encode
    resp = ''
    str_ant = string[0]
    count = 0
    for s in string:
        if str_ant == s:
            count += 1
        else:
            resp += '{}{}'.format(('' if count == 1 else count), str_ant)
            str_ant = s
            count = 1
    resp += '{}{}'.format(('' if count == 1 else count), str_ant)
    return resp
