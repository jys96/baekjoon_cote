def check_bill(wallet, bill):
    result = False
    
    
    if (max(wallet) < max(bill)) or (min(wallet) < min(bill)):
        result = True
    
    return result

def half_bill(bill):
    if bill[0] > bill[1]:
        bill[0] = bill[0] // 2
    elif bill[0] < bill[1]:
        bill[1] = bill[1] // 2
    
    return bill

def translate_bill(bill):
    
    return [bill[1], bill[0]]

def solution(wallet, bill):
    answer = 0
    
    while check_bill(wallet, bill):
        bill = half_bill(bill)
        bill = translate_bill(bill)
        answer += 1
        
    return answer