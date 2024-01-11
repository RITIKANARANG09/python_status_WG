from datetime import datetime, timezone,timedelta

#today=datetime.now()   (naive)
today=datetime.now(timezone.utc)
tomorrow=today+timedelta(days=1)
print(today)
print(tomorrow)
print(today.strftime('%d-%m-%Y %H:%M:%S')) # string format time
user_date=input("enter date in YYYY-mm-dd format :")
user_date=datetime.strptime(user_date,'%Y-%m-%d')
print(user_date)