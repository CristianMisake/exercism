"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = {'score': 50, 'value': 'YACHT'}
ONES = {'score': 1, 'value': 1}
TWOS = {'score': 2, 'value': 2}
THREES = {'score': 3, 'value': 3}
FOURS = {'score': 4, 'value': 4}
FIVES = {'score': 5, 'value': 5}
SIXES = {'score': 6, 'value': 6}
FULL_HOUSE = {'score': None, 'value': 'FULL_HORSE'}
FOUR_OF_A_KIND = {'score': None, 'value': 'FOUR_OF_A_KIND'}
LITTLE_STRAIGHT = {'score': 30, 'value': 'LITTLE_STRAIGHT'}
BIG_STRAIGHT = {'score': 30, 'value': 'BIG_STRAIGHT'}
CHOICE = {'score': 30, 'value': 'CHOICE'}


def score(dice, category):
    # case of YACHT
    if category['value'] == 'YACHT':
        return yacht(dice)
    # case of FULL_HORSE
    if category['value'] == 'FULL_HORSE':
        return full_horse(dice)
    # case of FOUR_OF_A_KIND
    if category['value'] == 'FOUR_OF_A_KIND':
        return four_of_a_kind(dice)
    # case of LITTLE_STRAIGHT
    if category['value'] == 'LITTLE_STRAIGHT':
        return little_straight(dice)
    # case of BIG_STRAIGHT
    if category['value'] == 'BIG_STRAIGHT':
        return big_straight(dice)
    # case of CHOICE
    if category['value'] == 'CHOICE':
        return array_sum(dice)
    # case of particular
    return particular(dice, category)


def no_repeat_list(list_origin):
    new_list = {}
    for i in list_origin:
        if i in new_list:
            new_list[i] += 1
        else:
            new_list[i] = 1
    return new_list


def array_sum(dice):
    resp = 0
    for i in dice:
        resp += i
    return resp


def yacht(dice):
    for i in dice:
        if dice[0] != i:
            return 0
    return YACHT['score']


def particular(dice, category):
    puntaje = 0
    for i in dice:
        if category['value'] == i:
            puntaje += category['score']
    return puntaje


def full_horse(dice):
    dice.sort()
    items = no_repeat_list(dice)
    first_item = items[list(items.keys())[0]]
    if len(items) != 2:
        return 0
    count = len([item for item in dice if item == first_item])
    return (array_sum(dice) if count in [2, 3] else 0)


def four_of_a_kind(dice):
    resp = 0
    dice.sort()
    items = no_repeat_list(dice)
    if len(items) > 2:
        return 0
    for i in items:
        resp += (i * 4 if items[i] in [4, 5] else 0)
    return resp


def little_straight(dice):
    dice.sort()
    return (LITTLE_STRAIGHT['score'] if dice == [1, 2, 3, 4, 5] else 0)


def big_straight(dice):
    dice.sort()
    return (BIG_STRAIGHT['score'] if dice == [2, 3, 4, 5, 6] else 0)
