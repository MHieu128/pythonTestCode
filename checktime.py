from datetime import datetime
now = datetime.now()
dateInput = "202107"
year = dateInput[:4]
month = int(dateInput[4:])
if now.month == month and now.year:
    print ("yes")
else:
    print ("No")