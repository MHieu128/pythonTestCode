from datetime import datetime
now = datetime.now()
year = str(now.year)
month = str(10).zfill(2)
dt = year + month
print(dt)