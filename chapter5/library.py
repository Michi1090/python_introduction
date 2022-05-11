from calendar import month, isleap
from datetime import date, timedelta

print(month(2022, 5))
isleap(2022)

today = date.today()
print(today.strftime('%Y%m%d'))
print(today.strftime('%y%m%d'))
print(today.strftime('%Y年%m月%d日'))
print(today.strftime('%Y %B %d %a'))

one_week = timedelta(days = 7)
print(today + one_week)
print(today - one_week)
