import math

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    result = A * B // math.gcd(A, B)

    print(result)