A, B, C = map(int, input().split())
D = int(input())

total = A * 3600 + B * 60 + C
total = (total + D) % 86400  # 24시간 순환

h = total // 3600
m = (total % 3600) // 60
s = total % 60

print(h, m, s)
