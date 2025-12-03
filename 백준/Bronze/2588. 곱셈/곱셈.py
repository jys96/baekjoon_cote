A = input()
B = input()


list = []

for i in B[::-1]:
    sum = int(i) * int(A)
        
    print(sum)
    list.append(sum)

sum = 0
z = 1

for num in list:
    sum += num * z
    z *= 10

print(sum)