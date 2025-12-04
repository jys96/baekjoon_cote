T = int(input())

for i in range(T):
    R, S = input().split()

    result = ''
    
    for t in S:
        for j in range(int(R)):
            result += t
    
    print(result)