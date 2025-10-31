from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())

# input
tomato = []
for i in range(H):
    layer = []
    for j in range(N):
        layer.append([*map(int, input().split())])
    tomato.append(layer)

# requirement: 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하라
# point: 3차원 BFS

def bfs(tomato, start):
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, -1 ,1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    dq = deque()
    for s in start:
        dq.append(s)

    while dq:
        z, y, x = dq.popleft()
        
        for i in range(6):
            nz = z + dz[i]; ny = y + dy[i]; nx = x + dx[i]
            if 0<=nz<H and 0<=ny<N and 0<=nx<M and tomato[nz][ny][nx]==0:
                tomato[nz][ny][nx] += tomato[z][y][x] + 1
                dq.append((nz,ny,nx))

start = []
flag = True
for h in range(H):
    for y in range(N):
        for x in range(M):
            if tomato[h][y][x] == 1:
                start.append((h,y,x))

bfs(tomato, start)

answer = 0
for h in range(H):
    for y in range(N):
        if 0 in tomato[h][y]:
            print(-1); exit()
        answer = max(answer, max(tomato[h][y]))
            
print(answer-1)    
