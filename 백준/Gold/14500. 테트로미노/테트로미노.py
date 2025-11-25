import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]

visited = [[False]*m for _ in range(n)]
answer = 0

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(y, x, depth, total):
    global answer
    if depth == 4:
        answer = max(answer, total)
        return

    for dy, dx in dirs:
        ny = y + dy; nx = x + dx
        if 0<=ny<n and 0<=nx<m and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, depth+1, total+board[ny][nx])
            visited[ny][nx] = False

def check_t(y, x):
    global answer
    center = board[y][x]
    neighbor = []

    for dy, dx in dirs:
        ny = y + dy; nx = x + dx
        if 0<=ny<n and 0<=nx<m:
            neighbor.append(board[ny][nx])

    if len(neighbor) >= 3:
        neighbor.sort(reverse=True)
        total = center + sum(neighbor[:3])
        answer = max(answer, total)

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

        check_t(i, j)

print(answer)


    