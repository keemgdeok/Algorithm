import sys
input = sys.stdin.readline

n, m = map(int, input().split())
y, x, d = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]

# 북, 동, 남, 서
dirs = [(-1,0), (0,1), (1,0), (0,-1)]
visited = [[0]*m for _ in range(n)]

answer = 0
while True:
    # 1.현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if board[y][x] == 0 and visited[y][x] == 0:
        visited[y][x] = 1
        answer+=1

    neighbor = []
    for dy, dx in dirs:
        ny = y + dy; nx = x + dx
        if not (0<=ny<n and 0<=nx<m): continue
        if board[ny][nx]==0 and visited[ny][nx]==0:
            neighbor.append((ny,nx))

    # 2.현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if not neighbor:
        back_dir = (d-2+4) % 4
        by = y + dirs[back_dir][0]; bx = x + dirs[back_dir][1]
        if 0<=by<n and 0<=bx<m and board[by][bx]==0:
            y = by; x=bx
            continue
        else: 
            break
    else: # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        d = (d-1+4) % 4
        fy = y + dirs[d][0]; fx = x + dirs[d][1]
        if not(0<=fy<n and 0<=fx<m): continue
        if board[fy][fx] == 0 and visited[fy][fx] == 0:
            y = fy; x = fx

print(answer)
 