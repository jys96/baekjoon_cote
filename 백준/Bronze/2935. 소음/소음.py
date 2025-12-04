A = int(input())
operator = input()
B = int(input())

if operator == '+':
    print(A + B)
elif operator == '*':
    print(A * B)
else:
    print('잘못된 연산자가 입력되었습니다.')