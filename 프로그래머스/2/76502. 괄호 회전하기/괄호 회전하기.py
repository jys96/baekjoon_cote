def checking_str(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:  # 여는 괄호
            stack.append(char)
        else:  # 닫는 괄호
            if not stack:  # 스택이 비어있으면 실패
                return False
            if pairs[stack[-1]] == char:  # 짝이 맞으면
                stack.pop()
            else:  # 짝이 안 맞으면
                return False
    
    return len(stack) == 0  # 스택이 비어있어야 성공

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        rotated = s[i:] + s[:i]  # 왼쪽으로 i칸 회전
        if checking_str(rotated):
            answer += 1
    
    return answer