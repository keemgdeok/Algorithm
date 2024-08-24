from collections import deque

def bfs(a, b):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    c=0 

    dq = deque()
    dq.append((a, b))
    graph[a][b] = 0

    while dq:
        x, y = dq.popleft()
        c+=1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx<N) and (0<=ny<N) and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dq.append((nx, ny))
    return c


N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

cnt=0
ans=[]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt+=1
            ans.append(bfs(i, j))

print(cnt)
ans = sorted(ans)
for i in range(cnt):
    print(ans[i])


                 

