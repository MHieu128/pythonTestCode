from datetime import datetime
now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
type(date_time)
print( "pre : ",date_time)
date_time = datetime.fromtimestamp(datetime.timestamp(now) + 1800)
date_time = date_time.strftime("%m/%d/%Y, %H:%M:%S")
print( "after : ",date_time)