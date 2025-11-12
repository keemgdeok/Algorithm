from collections import deque

N, M = map(int,input().split())

graph=[list(map(int, input().split())) for _ in range(M)]
dq = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            dq.append((i, j))

while dq:
    x, y = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<=nx<M) and (0<=ny<N) and graph[nx][ny]==0:
            graph[nx][ny]=graph[x][y]+1
            dq.append((nx, ny))
                     

ans=0
for line in graph:
    for tomato in line:
        if tomato == 0:
            print(-1)
            exit()
    ans = max(ans, max(line))

print(ans-1)

    


