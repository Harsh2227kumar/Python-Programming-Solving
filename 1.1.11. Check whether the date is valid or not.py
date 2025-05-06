from datetime import datetime, timedelta
year = int(input("year: "))
month = int(input("month: "))
day = int(input("day: "))

try:
	date = datetime(year, month, day)
	print("valid")
	next_date = date + timedelta(days=1)
	print(f"incremented date: {next_date.strftime('%Y-%m-%d')}")
except ValueError:
	print("invalid")