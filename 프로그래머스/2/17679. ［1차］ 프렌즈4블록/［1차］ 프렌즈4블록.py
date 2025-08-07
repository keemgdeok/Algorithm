from collections import deque

def solution(m, n, board):
    removed = 0
    board = [list(row) for row in board]
    total_removed = 0
    
    while True:
        remove = find2by2(board, m, n)
        if not remove: 
            break
        
        removed += removeBlock(board, remove)
        
        dropBlock(board, m, n)
        
    
    return removed

def find2by2(board, m, n):
    remove = set()
    for i in range(m-1):
        for j in range(n-1):
            if (board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] and board[i][j] != " "):
                remove.add((i, j))
                remove.add((i, j+1))
                remove.add((i+1, j))
                remove.add((i+1, j+1))
    return remove
                
def removeBlock(board, remove):
    for i, j in remove:
        board[i][j] = " "
    return len(remove)

def dropBlock(board, m, n):
    for j in range(n):
        bottom = m-1
        for i in range(m-1, -1, -1):
            if board[i][j] != " ":
                board[bottom][j] = board[i][j]
                if bottom != i:
                    board[i][j] = " "
                bottom -= 1
        
        
                
            
                
        
    