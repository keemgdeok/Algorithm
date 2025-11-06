import sys
from collections import deque
input = sys.stdin.readline

while True:
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break

    # input
    start = None
    bd = []
    for l in range(L):
        layer = [input().rstrip() for _ in range(R)]
        if start is None:
            for r in range(R):    
                for c in range(C):
                    if layer[r][c] == "S":
                        start = (l,r,c)
        bd.append(layer)
        input() 

    # requirement: 여기서 탈출하는 가장 빠른 길은 무엇일까?
    # point: 3차원 BFS
    
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    visited = [[[0]*C for _ in range(R)] for _ in range(L)]
    
    dq = deque()
    dq.append(start)
    visited[start[0]][start[1]][start[2]] = 1

    flag = 0
    while dq:
        z, y, x = dq.popleft()
        for i in range(6):
            nx = x + dx[i]; ny = y + dy[i]; nz = z + dz[i]
            if 0<=nx<C and 0<=ny<R and 0<=nz<L and not visited[nz][ny][nx] and bd[nz][ny][nx] != "#":
                visited[nz][ny][nx] = visited[z][y][x] + 1
                dq.append((nz, ny, nx))

                if bd[nz][ny][nx] == "E":
                    print(f"Escaped in {visited[nz][ny][nx]-1} minute(s).")
                    flag = 1
                    break

    if not flag: print("Trapped!")

