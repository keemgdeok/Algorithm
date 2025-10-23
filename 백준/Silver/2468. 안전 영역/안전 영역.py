import sys
from collections import deque

N=int(input())

area = []
max_height = 0
for lines in sys.stdin.readlines():
    line = list(map(int, lines.split()))
    area.append(line)
    max_height = max(max_height, max(line))
    
def bfs(area, visited, height, i, j):
    dx = [1,-1, 0, 0]
    dy = [0, 0, -1, 1]

    dq=deque()
    dq.append((i, j))
    visited[i][j]=True
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and area[ny][nx]>height and not visited[ny][nx]:
                dq.append((ny, nx))          
                visited[ny][nx]=True
    return visited

answer = 1
for h in range(1, max_height+1):
    count=0
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if area[i][j]>h and not visited[i][j]:
                bfs(area, visited, h, i, j)
                count+=1
    answer = max(answer, count)

print(answer)


