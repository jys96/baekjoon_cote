def solution(n, left, right):
    answer = []
    
    for k in range(left, right + 1):
        i = k // n  # 행
        j = k % n   # 열
        value = max(i, j) + 1
        answer.append(value)
    
    return answer