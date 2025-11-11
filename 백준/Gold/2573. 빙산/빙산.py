from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]

# requirement: 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오. 
# point: 덩어리 세는 BFS 1 개, 녹는 BFS 1개 / 빙하 감소는 인접한 0을 기준으로
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
    
def bfs(matrix, visited, i, j):
    dq = deque([(i, j)])
    visited[i][j]=1
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dy[i]; nx = x + dx[i]
            if not (0<=ny<N and 0<=nx<M): continue
            if matrix[ny][nx] > 0 and visited[ny][nx] == 0:
                dq.append((ny,nx))
                visited[ny][nx]=1

year=0
while True:
    ib=0
    visited = [[0]*M for _ in range(N)]
    has_iceberg = False
    for i in range(1, N-1):
        for j in range(1, M-1):
            if matrix[i][j] > 0 and visited[i][j]==0:
                bfs(matrix, visited, i, j)
                ib+=1
                has_iceberg = True

    if ib>=2:
        print(year)
        break

    if not has_iceberg:
        print(0)
        break

    year+=1
    iceberg = [[0]*M for _ in range(N)]
    for y in range(1, N-1):
        for x in range(1, M-1):
            if matrix[y][x] == 0: continue
            for k in range(4):
                ny = y + dy[k]; nx = x + dx[k]
                if matrix[ny][nx] == 0:
                    iceberg[y][x] += 1
    
    for y in range(1, N-1):
        for x in range(1, M-1):
            matrix[y][x] = max(matrix[y][x]-iceberg[y][x], 0)

            