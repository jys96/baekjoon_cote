a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = []

first = [a[0], b[0], c[0]]
second = [a[1], b[1], c[1]]

for i in first:
    if first.count(i) == 1:
        d.append(i)
        break

for i in second:
    if second.count(i) == 1:
        d.append(i)
        break

str_d = list(map(str, d))

print(' '.join(str_d))
