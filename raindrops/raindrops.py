def convert(number):
    resp = ''
    if number % 3 == 0:
        resp += 'Pling'
    if number % 5 == 0:
        resp += 'Plang'
    if number % 7 == 0:
        resp += 'Plong'
    if resp == '':
        resp = str(number)
    return resp
