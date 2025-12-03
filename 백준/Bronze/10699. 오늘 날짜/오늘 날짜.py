from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))
print(datetime.now(KST).strftime('%Y-%m-%d'))