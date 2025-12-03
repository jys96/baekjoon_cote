T = int(input())

for i in range(T):
    result = 0
    count = 0

    for j in input().split():

        if count == 0:
            result = float(j)
        else:
            if j == '@':
                result *= 3
            elif j == '%':
                result += 5
            elif j == '#':
                result -= 7
        
        count += 1

    print("%0.2f"%result)