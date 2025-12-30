def solution(board, h, w):
    answer = 0
    
    nearby = [
        board[h-1][w] if h > 0 else '',
        board[h+1][w] if h < len(board)-1 else '',
        board[h][w-1] if w > 0 else '',
        board[h][w+1] if w < len(board[h])-1 else '',
    ]
    
    for i in nearby:
        if i == board[h][w]:
            answer += 1
    
    return answer