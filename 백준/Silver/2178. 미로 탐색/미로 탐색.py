from collections import deque
N, M = map(int,input().split())

maze = [list(map(int, input())) for _ in range(N)]

def bfs(b, a):
    dx=[1, -1, 0, 0]
    dy=[0, 0, -1, 1]
    dq=deque()
    dq.append((b,a))
    maze[b][a]+=1
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny=y+dy[i]; nx=x+dx[i]
            if ny==N and nx==M: break
            if (0<=ny<N and 0<=nx<M) and maze[ny][nx]==1:
                maze[ny][nx]=maze[y][x]+1
                dq.append((ny, nx))

bfs(0,0)
print(maze[N-1][M-1]-1)
        
    