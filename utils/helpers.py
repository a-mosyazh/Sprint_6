import datetime


def get_next_day():
    today = int(datetime.date.today().strftime('%d'))
    return today + 1
