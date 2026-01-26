def solution(numbers):
    answer = []
    length = len(numbers)
    
    for i in range(length):
        a = numbers[i]
        
        for j in range(length):
            b = numbers[j]
            
            if i is not j:
                sum = a + b
            
                if sum not in answer:
                    answer.append(sum)
            
    answer.sort()
    
    return answer