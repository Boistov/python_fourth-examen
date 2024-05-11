import datetime


today = datetime.datetime.today()
a = today - datetime.timedelta(days=2)
b = today + datetime.timedelta(days=2)

print(f"{a.strftime('%Y-%m-%d')}")
print(f"{today.strftime('%Y-%m-%d')}")
print(f"{b.strftime('%Y-%m-%d')}")

