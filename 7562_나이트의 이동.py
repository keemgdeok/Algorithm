from collections import deque


def Night(a, b, ax, ay):
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1 ,-1, -2, -2, -1, 1, 2]

    dq = deque()
    dq.append((a, b)) # 첫번째 받을때는 a, b

    while dq:
        x, y = dq.popleft()  # while문 돌면서 받을때는 x, y
        visited[x][y] = True
        if x == ax and y == ay:
            return graph[x][y]
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx<N) and (0<=ny<N) and visited[nx][ny] == False:
                graph[nx][ny] = graph[x][y] + 1
                dq.append((nx, ny))
                visited[nx][ny] = True
            
num = int(input())

for _ in range(num):
    N = int(input())
    a, b = map(int, input().split())
    ax, ay = map(int, input().split())
    graph = [[0] * N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    

    print(Night(a, b, ax, ay))
