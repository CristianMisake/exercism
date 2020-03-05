def recite(start_verse, end_verse):
    resp = []
    if start_verse == end_verse:
        text = 'On the {} day of Christmas my true love gave to me: '
        days = [
            'first', 'second', 'third', 'fourth',
            'fifth', 'sixth', 'seventh', 'eighth',
            'ninth', 'tenth', 'eleventh', 'twelfth'
        ]
        # convertidor de texto
        for i in range(start_verse):
            resp.append(part_recite(start_verse, i))
        resp.append(text.format(days[start_verse - 1]))
        # retornar respuesta
        resp = [''.join(resp[::-1])]
    else:
        for i in range(start_verse, end_verse + 1):
            resp.append(recite(i, i)[0])
    return resp


def part_recite(start_verse, part):
    # condición especial
    if start_verse == 1:
        part_one = ''
    else:
        part_one = 'and '
    # partes del recital
    parts = [
        '{}a Partridge in a Pear Tree.'.format(part_one),
        'two Turtle Doves, ',
        'three French Hens, ',
        'four Calling Birds, ',
        'five Gold Rings, ',
        'six Geese-a-Laying, ',
        'seven Swans-a-Swimming, ',
        'eight Maids-a-Milking, ',
        'nine Ladies Dancing, ',
        'ten Lords-a-Leaping, ',
        'eleven Pipers Piping, ',
        'twelve Drummers Drumming, ',
    ]
    return parts[part]
