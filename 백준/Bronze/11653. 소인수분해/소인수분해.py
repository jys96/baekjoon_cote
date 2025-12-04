request_num = int(input())

default_num = 2

while default_num * default_num <= request_num:
    
    if request_num % default_num == 0:
        request_num = request_num // default_num
        print(default_num)
    else:
        default_num += 1

if request_num > 1:
    print(request_num)