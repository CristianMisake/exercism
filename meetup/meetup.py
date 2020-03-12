from datetime import date, timedelta


all_week = [
        'Monday', 'Tuesday',
        'Wednesday', 'Thursday',
        'Friday', 'Saturday',
        'Sunday'
]
MeetupDayException = ValueError


def meetup(year, month, week, day_of_week):
    day = 0
    if week == 'teenth':
        day = 13
    if week == '1st':
        day = 1
    if week == '2nd':
        day = 8
    if week == '3rd':
        day = 15
    if week == '4th':
        day = 22
    if week == '5th':
        day = 29
    if week == 'last':
        day = lass_day(year, month) - 6
    if lass_day(year, month) < day:
        raise MeetupDayException('.+')
    else:
        return func_teenth(date(year, month, day), day_of_week)


def func_teenth(ini_date, dest_day):
    ini_week = all_week.index(ini_date.strftime('%A'))
    dest = all_week.index(dest_day)
    count = 0
    while ini_week != dest:
        if len(all_week) - 1 == ini_week:
            ini_week = 0
        else:
            ini_week += 1
        count += 1
    return ini_date + timedelta(days=count)


def lass_day(year, month):
    if month == 12:
        year += 1
        month = 0
    return (date(year, month + 1, 1) - timedelta(days=1)).day
