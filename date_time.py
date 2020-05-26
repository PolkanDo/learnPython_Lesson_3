from datetime import date, datetime, timedelta

today = date.today()
one_day = timedelta(days=1)
one_month = timedelta(days=30)
yesteday = today - one_day
month_ago = today - one_month

# standard date output
print(today)
print(yesteday)
print(month_ago)

# formatted date output
print(today.strftime('%d %B %Y'))
print(yesteday.strftime('%d/%m/%y'))
print(month_ago.strftime('%m-%d-%Y'))

date_string = "01/01/25 12:10:03.234567"
date_date = datetime.strptime(date_string, "%y/%m/%d %H:%M:%S.%f")
print(type(date_date))
print(date_date)