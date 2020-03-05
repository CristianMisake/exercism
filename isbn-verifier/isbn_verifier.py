import re


def is_valid(isbn):
    new_isbn = re.sub('-', '', isbn)
    i = len(new_isbn)
    if i == 10:
        result = 0
        for digit in new_isbn:
            if digit.isnumeric():
                result += int(digit) * i
            else:
                if digit.lower() == 'x':
                    result += (len(new_isbn) - i + 1) * i
                else:
                    return False
            i -= 1
        return result % 11 == 0
    else:
        return False
