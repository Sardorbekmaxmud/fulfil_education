# # 1
# from datetime import datetime, timedelta
# from dateutil.relativedelta import relativedelta

# now_date = datetime.now()
#
# print(now_date)
# print(type(now_date))

# # 2
# date_string = "Feb 25 2020 4:20PM"  # 25-02-2020 16:20:00
#
# str_to_date = datetime.strptime(date_string, "%b %d %Y %I:%M%p")
# print(str_to_date)


# # 3
# given_date = datetime(2020, 2, 25)
# print(datetime.strftime(given_date - timedelta(days=7), "%Y-%m-%d"))


# # 4
# given_date = datetime(2020, 2, 25) # input
# print(datetime.strftime(given_date, "%A %d %B %Y")) # output Tuesday 25 February 2020


# # 5
# given_date = datetime(2020, 7, 26)
# print(given_date.strftime("%A")) # output: Sunday


# # 6
# given_date = datetime(2020, 3, 22, 10, 0, 0)
# add_7_days_and_12_hours = given_date + timedelta(days=7, hours=12)
# print(add_7_days_and_12_hours)


# # 7
# now_date = datetime.now()
# print(now_date.microsecond)
# import time
#
# milliseconds = int(round(time.time() * 1000))
# milliseconds2 = int(time.time() * 1000)
# print(milliseconds)
# print(milliseconds2)


# # 8
# given_date = datetime(2020, 2, 25)
# print(given_date.strftime("%d.%m.%Y %H:%M:%S")) # 25.02.2020 00:00:00
# print(type(given_date.strftime("%d.%m.%Y %H:%M:%S"))) # <class 'str'>


# # 9
# given_date = datetime(2020, 2, 25).date()
# print((given_date + relativedelta(months=4)).strftime("%d.%m.%Y"))


# # 10

# date_1 = datetime(2020, 2, 25)  # 2020-02-25
# date_2 = datetime(2020, 9, 17)  # 2020-09-17
#
# if date_2 > date_1:
#     print((date_2 - date_1).days, "days")
# else:
#     print((date_1 - date_2).days, "days")
