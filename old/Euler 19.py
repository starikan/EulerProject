# -*- coding: utf-8 -*-
__author__ = 'Starik'

# import time
import datetime

start = curr = datetime.date(1901, 1, 1)
end = datetime.date(2000, 12, 31)
day = datetime.timedelta(days=1)

data = []
while end >= curr:
    data.append({"date":curr, "day":curr.day, "weekday":curr.weekday()})
    curr += day
f_data = [i for i in data if i["day"] == 1 and i["weekday"] == 6]
for i in f_data: print i
print len(f_data)


# Вариант по-лучше с форума

# import datetime
# count = 0
# for y in range(1901,2001):
#     for m in range(1,13):
#         if datetime.datetime(y,m,1).weekday() == 6:
#             count += 1
# print count


# from calendar import weekday
# print sum(int(weekday(y, m, 1) == 6) for y in range(1901, 2001) for m in range(1, 13))