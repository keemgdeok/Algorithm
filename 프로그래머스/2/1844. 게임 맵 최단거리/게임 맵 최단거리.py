from collections import deque

def solution(maps):
    ans = 0
    row = len(maps)
    col = len(maps[0])
    dx=[1, -1, 0, 0]
    dy=[0, 0, -1, 1]
    dq=deque()
    dq.append((0,0))
    
    while dq:
        y, x=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<col and 0<=ny<row:
                if maps[ny][nx]==1:
                    dq.append((ny,nx))
                    maps[ny][nx]+=maps[y][x]
    
    
    ans = maps[row-1][col-1] 
    return ans if ans>1 else -1