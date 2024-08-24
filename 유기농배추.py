import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0 ,0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M) and (0 <= ny < N):
            if farm[ny][nx] == 1:
                farm[ny][nx] = 0
                dfs(nx, ny)

T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    farm = [[0]*M for i in range(N)]
    cnt = 0

    # 배추 위치 표시
    for j in range(K):
        X, Y = map(int, input().split())
        farm[Y][X] = 1

    for i in range(M):
        for j in range(N):
            if farm[j][i] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt) 

    



