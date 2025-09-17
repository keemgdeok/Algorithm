

def solution(board):
    answer = 1234    
    
    max_len=0
    for i in range(len(board)):
        if board[i][0]:
            max_len=1
            break
    for j in range(len(board[0])):
        if board[0][j]:
            max_len=1
            break
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j]:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1])+1
                max_len = max(board[i][j], max_len)
            
    return max_len**2