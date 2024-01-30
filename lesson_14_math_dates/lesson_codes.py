# # 0-----==-=-=-=-=-=-=-=- math -=-=-=-=-=-=-=
import math

# print(math.e)  # matematika "e" soni
# print(math.inf)  # plus cheksizlik
# print(-math.inf)  # minus cheksizlik
# print(abs(-7.34))  # sonni moduldan chiqarish har doim musbat chiqadi
# # darajasini topish -===================
# print(pow(2, 3))
# print(math.pow(2, 3))
# # ildiz ostini chiqarish -===================
# print(math.sqrt(625))
# print(625 ** 0.5)
# print(pow(80, 0.5))
# print(math.sqrt(80))
# # sonni yaxlitlash -===================
# print(math.ceil(1.7))
# print(math.floor(1.7))

# # -=-==-=-==-====  datetime ==============================
from datetime import datetime, timedelta
from time import time

# import pytz
# now = datetime.now()
# print(now) # hozirgi vaqt

# date = datetime(2022, 3, 25, 20, 28, 50, 987657)
# print(date) # biron bir sanani olish

# besh_soatdan_keyin = now + timedelta(hours=5)  # timedelta qo'shishda foydalanamiz
# print(besh_soatdan_keyin)

# weeks = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
# print(weeks[now.weekday()])

# # bizlar strftime(date, format) dan foydalanganimizda sanani o'zimiz istagan xolda chiqarish uchun foydalanamiz
# guiter = datetime(2023, 12, 31, 23, 59, 59, 999999)
# print(guiter.strftime("  %H:%M:%S\n%d/%m/%Y"))
# print(now.strftime("  %H:%M:%S\n%d/%m/%Y"))

# # strptime(date_str, format)
# # stringdagi sanani datetime obyekti qilib sanaga aylantiradi
# date_string = "2020 12 5"
# date = datetime.strptime(date_string, "%Y %m %d")
# print(date)

# # foydalanuvchi str da sana kiritadi u qaysi haftaga to'gri kelishini topish
# date_str = input("Sanani kiriting: ")
# week = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
# date = datetime.strptime(date_str, "%Y %m %d")
# print(week[date.weekday()])

from datetime import datetime

# import pytz

# now = datetime.now()
# x_date_now = datetime.now(pytz.utc)
# us_date_now = datetime.now(pytz.timezone('US/Central'))
# print("Local", now)
# print("UTC", x_date_now)
# print("US", us_date_now)


# dt_us_mountain = datetime.now(pytz.timezone('America/Chihuahua'))
# print(dt_us_mountain)

# import calendar
#
# year = 2023
# month = 12
#
# print(calendar.calendar(year))

# import calendar
#
# text_cal = calendar.HTMLCalendar(firstweekday=0)
#
# # default value of width is 0
#
# # printing formatyear
# print(text_cal.formatyear(2023))

# count = 1
# for i in range(1, 5 + 1):
#     count *= i
# print(count)

def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        result = fib(n-1) + fib(n-2)
    return result

# print(fib())
