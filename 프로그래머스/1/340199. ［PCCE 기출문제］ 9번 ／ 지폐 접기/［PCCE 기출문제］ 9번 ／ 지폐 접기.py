def ch_in(wallet, bill):
    if wallet >= bill:
        return True
    else:
        return False

def half_bill(bill):
    if bill[0] > bill[1]:
        bill[0] = bill[0] // 2
    else:
        bill[1] = bill[1] // 2

    return bill

def rotation_bill(wallet, bill):
    result = []
    for i in range(2):
        result.append(ch_in(wallet[i], bill[i]))

    if False in result:
        result = []
        result.append(ch_in(wallet[0], bill[1]))
        result.append(ch_in(wallet[1], bill[0]))

        if False in result:
            return False
        else:
            return True
    else:
        return True

def solution(wallet, bill):
    answer = 0

    while True:
        result = rotation_bill(wallet, bill)

        if result == True:
            break
        else:
            bill = half_bill(bill)
            answer += 1

    return answer