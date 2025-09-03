from collections import deque

def solution(board):
    ans = 0
    row = len(board)
    col = len(board[0])
    visited = [[0]*col for _ in range(row)]

    y,x = 0, 0
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'R':
                y, x = i, j
                
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    dq = deque()
    dq.append((y, x))
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            nx=x; ny=y
            while 0<=nx<col and 0<=ny<row and board[ny][nx]!="D":
                nx+=dx[i]; ny+=dy[i]
            nx-=dx[i];ny-=dy[i]

            if (nx!=x or ny!=y) and visited[ny][nx]==0:
                visited[ny][nx]+=visited[y][x]+1
                dq.append((ny,nx))
                
            
    for i in range(row):
        for j in range(col):
            if board[i][j]=="G":
                return visited[i][j] if visited[i][j]>0 else -1
