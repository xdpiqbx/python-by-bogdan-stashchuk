import locale
from datetime import date

print(locale.getlocale())  # ('Ukrainian_Ukraine', '1251')


def seven():
    return 7


def sum_1(a, b=8, c=seven()):
    print(date.today().strftime('%x'))
    print(a + b + c)


sum_1(2)
