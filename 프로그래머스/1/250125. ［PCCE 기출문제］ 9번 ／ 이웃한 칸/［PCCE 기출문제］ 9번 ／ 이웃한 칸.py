def solution(board, h, w):
    answer = 0
    target = board[h][w]
    n = len(board)
    
    dh = [-1, 1, 0, 0]
    dw = [0, 0, -1, 1]
    
    for i in range(4):
        new_h = h + dh[i]
        new_w = w + dw[i]
        
        if 0 <= new_h < n and 0 <= new_w < n:
            if board[new_h][new_w] == target:
                answer += 1
    
    return answer