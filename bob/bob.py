import re


def response(hey_bob):
    hey_bob = hey_bob.strip()
    if re.match(r'[A-Z\s\']+\?', hey_bob):
        return "Calm down, I know what I'm doing!"
    if re.match(r'(.+)\?$', hey_bob):
        return 'Sure.'
    if re.match(r'.*[A-Z]{2,}.*', hey_bob) and hey_bob == hey_bob.upper():
        return 'Whoa, chill out!'
    if re.sub(r'\s', '', hey_bob) == '':
        return 'Fine. Be that way!'
    return 'Whatever.'
