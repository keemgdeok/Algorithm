import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(sy, sx, visited):
    q = deque([(sy, sx)])
    visited[sy][sx] = True
    union = [(sy, sx)]
    sum_pop = board[sy][sx]

    while q:
        y, x = q.popleft()
        cur_pop = board[y][x]

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if l <= abs(board[ny][nx] - cur_pop) <= r:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    union.append((ny, nx))
                    sum_pop += board[ny][nx]

    if len(union) == 1:
        return False  # 인구 이동 없음

    new_pop = sum_pop // len(union)
    for y, x in union:
        board[y][x] = new_pop
    return True       # 인구 이동 발생

days = 0
while True:
    visited = [[False]*n for _ in range(n)]
    moved = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    moved = True

    if not moved:
        break
    days += 1

print(days)
