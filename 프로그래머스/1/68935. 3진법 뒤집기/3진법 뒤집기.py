import numpy as np

def transform_to_repr(n):
    return np.base_repr(n, 3)

def translate(n):
    print('in def translate', n)

    result = ""
    count = len(n)

    while count > 0:
        result += n[count-1]
        count -= 1
        
    return result
    
def solution(n):
    tranform_3 = transform_to_repr(n)
    answer = translate(tranform_3)

    return int(answer, 3)
    