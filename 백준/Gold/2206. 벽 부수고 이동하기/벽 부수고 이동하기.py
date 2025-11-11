from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[*map(int, input().rstrip())] for _ in range(N)]

# requirement : 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
# point : 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
# 1000*1000*1000 = 10^9 이라 시간초과 -> 상태공간을 확장하여 한번의 BFS를 사용/ 3차원 배열 사용

def bfs(matrix, visited, n, m):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    dq = deque([(0,0,0)]) # y, x, 벽 부순 횟수
    visited[0][0][0]=1

    while dq:
        y, x, done = dq.popleft()
        if y == N-1 and x == M-1:
            return visited[done][y][x]
        
        for i in range(4):
            ny = y + dy[i]; nx = x + dx[i]
            if not (0<=ny<N and 0<=nx<M): continue
            if done > 1: continue
            if matrix[ny][nx] == 0:
                if visited[done][ny][nx] == 0:
                    visited[done][ny][nx] = visited[done][y][x] + 1
                    dq.append((ny, nx, done))
            elif matrix[ny][nx] == 1:
                if done == 0 and visited[1][ny][nx]==0:
                    dq.append((ny, nx, done+1))
                    visited[1][ny][nx] = visited[done][y][x] + 1
    return -1

visited = [[[0]*M for _ in range(N)] for _ in range(2)]
result = bfs(matrix, visited, N, M)
print(result)