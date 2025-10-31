from collections import deque
import sys
input = sys.stdin.readline

# input
R, C = map(int, input().split())
maze = [input().rstrip() for _ in range(R)]

dq = deque()
ji = [-1, -1]
visited = [[-1]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if maze[i][j] == "J":
            ji = [i, j]
        elif maze[i][j] == "F":
            dq.append((i,j,0))
            visited[i][j] = -2
        elif maze[i][j] == "#":
            visited[i][j] = -2

dq.append((*ji, 1))
visited[ji[0]][ji[1]] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while dq:
    y, x, stat = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx<0 or nx>=C or ny<0 or ny>=R): continue

        if stat==0:
            if visited[ny][nx] == -1:
                visited[ny][nx] = -2
                dq.append((ny, nx, stat))
        else:
            if visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                dq.append((ny, nx, stat))

ans = int(1e9)
for i in range(R):
    if visited[i][0] > 0: ans = min(ans, visited[i][0])
    if visited[i][-1] > 0: ans = min(ans, visited[i][-1])

for j in range(C):
    if visited[0][j] > 0: ans = min(ans, visited[0][j])
    if visited[-1][j] > 0: ans = min(ans, visited[-1][j])

print(ans if ans != int(1e9) else "IMPOSSIBLE")

