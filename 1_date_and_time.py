"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import date, datetime,timedelta
import locale

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(date.today().strftime('%d.%m.%Y'))
    print((date.today()-timedelta(days=1)).strftime('%d.%m.%Y'))
    print((date.today()-timedelta(days=30)).strftime('%d.%m.%Y'))

    


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    locale.setlocale(locale.LC_TIME, 'ru_RU')
    dt_new = datetime.strptime('01/01/20 12:10:03.234567','%m/%d/%y %H:%M:%S.%f')
    print(dt_new.strftime('%c'))

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
