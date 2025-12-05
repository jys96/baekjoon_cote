def check_eyes(eyes):
    eyes = list(map(int, eyes))
    count = 0
    eye = 0

    for i in eyes:
        agree_count = eyes.count(i)

        if count < agree_count:
            count = agree_count
            eye = i

        if count == 1:
            eye = max(eyes)

    return count, eye

agree_count, eye = check_eyes(input().split())

prize = 0

match agree_count:
    case 3:
        prize = 10000 + eye * 1000
    case 2:
        prize = 1000 + eye * 100
    case _:
        prize = eye * 100

print(prize)