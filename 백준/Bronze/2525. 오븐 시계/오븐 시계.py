from datetime import timedelta

A, B = map(int, input().split())
C = int(input())

now_time = timedelta(hours=A, minutes=B)
add_minute = timedelta(minutes=C)

end_time = now_time + add_minute

total_sec = end_time.total_seconds()

h = int(total_sec // 3600)
m = int((total_sec % 3600) // 60)

print((h - 24) if h >= 24 else h, m)