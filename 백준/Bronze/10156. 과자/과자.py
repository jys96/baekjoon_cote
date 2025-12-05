K, N, M = map(int, input().split())

price = K * N
money = 0

if price > M:
    # 받아야함
    money = price - M
else: 
    money = 0

print(money)