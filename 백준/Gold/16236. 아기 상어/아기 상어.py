from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
sea = [[*map(int, input().split())] for _ in range(N)]

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
size = 2; eat = 0; ans = 0

for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            sea[i][j] = 0
            sr, sc = i, j
            break
    else:
        continue
    break
    
while True:
    dist = [[-1]*N for _ in range(N)]
    dq = deque([(sr, sc)])
    dist[sr][sc] = 0
    candidates = []
    min_d = float("INF")
    
    while dq:
        y, x = dq.popleft()
        d = dist[y][x]
        if d + 1 > min_d: continue
        for i in range(4):
            ny = y + dy[i]; nx = x + dx[i]
            if not (0 <= ny < N and 0 <= nx < N): continue
            if dist[ny][nx]!=-1: continue
            if sea[ny][nx] > size: continue

            dist[ny][nx] = d + 1
            if 0 < sea[ny][nx] < size:
                min_d = d+1
                candidates.append((ny,nx))
            else:
                dq.append((ny, nx))

    if not candidates: break
    r, c = min(candidates)
    ans+= dist[r][c]
    eat+=1
    if eat == size:
        size += 1
        eat = 0
    sea[r][c] = 0
    sr, sc = r, c
            
print(ans)
            

