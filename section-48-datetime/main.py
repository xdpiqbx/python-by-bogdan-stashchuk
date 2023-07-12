from datetime import date, time, datetime, timedelta

import time as t

print('=============================================== date')

print(type(date))  # <class 'type'>

my_date = date(day=24, month=2, year=2022)

print(my_date)  # 2003-12-30

print(my_date.day)  # 24
print(my_date.month)  # 2
print(my_date.year)  # 2022
print(my_date.ctime())  # Thu Feb 24 00:00:00 2022
print(my_date.weekday())  # 3
print(my_date.isoweekday())  # 4
print(my_date.isocalendar())  # datetime.IsoCalendarDate(year=2022, week=8, weekday=4)
print('=============================================== \n')

print('=============================================== time')

print(type(time))  # <class 'type'>
my_time = time(hour=10, minute=35, second=50, microsecond=900)
print(my_time)  # 10:35:50.000900
print(my_time.hour)  # 10
print(my_time.minute)  # 35
print(my_time.second)  # 50
print(my_time.microsecond)  # 900

print('=============================================== \n')

print('=============================================== datetime')

my_datetime = datetime(year=2000, month=10, day=20, hour=10, minute=25, second=50)
print(my_datetime)  # 2000-10-20 10:25:50
print(my_datetime.now())  # 2021-09-16 21:29:25.662851
print(my_datetime.now().microsecond)  # 803602
print(my_datetime.isoformat())  # 2000-10-20T10:25:50

# =============================================== strftime, strptime

print(my_datetime.strftime('%d-%b-%Y %H:%M:%S'))  # 20-Oct-2000 10:25:50
print(my_datetime.now().strftime('%d-%b-%Y %H:%M:%S'))

date_str = '20-Oct-2000 10:25:50'
converted_date = datetime.strptime(date_str, '%d-%b-%Y %H:%M:%S')

print('converted_date => ', converted_date.isoformat())
print('=============================================== \n')

print('=============================================== timedelta')
print("datetime.now()", datetime.now())
print("dateti + delta", datetime.now() + timedelta(days=10, minutes=120))
print("dateti - delta", datetime.now() - timedelta(days=45, minutes=10, hours=17))

print('=============================================== \n')

print('=============================================== time as t')
print(t)  # <module 'time' (built-in)>
print(t.time())  # 1689187621.7798398
print(t.ctime(t.time()))  # Wed Jul 12 21:47:01 2023

start = t.time()
t.sleep(2.5)  # or other long operation
stop = t.time()

print("stop - start: ", stop - start)  # after 2 seconds
