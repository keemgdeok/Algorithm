import sys
from collections import deque
input = sys.stdin.readline

# requirement: 빌딩의 지도가 주어졌을 때, 얼마나 빨리 빌딩을 탈출할 수 있는지 구하
# point : deque에 불 -> 상근이 순으로 넣음, 불 먼저

T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(T):
    w, h = map(int, input().split())
    matrix = [[*input().rstrip()] for _ in range(h)]
    visited = [[-1]*w for _ in range(h)]
    
    # 좌표 모으기
    dq = deque()
    sg = (-1, -1)
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == "*":
                dq.append((i,j,0))
                visited[i][j] = -2
            elif matrix[i][j] == "@":
                sg = (i, j, 1)
            elif matrix[i][j] == "#":
                visited[i][j] = -2
            
    # 마지막 상근이 넣기
    dq.append(sg)
    visited[sg[0]][sg[1]] = 1
    
    while dq:
        y, x, stat = dq.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if (nx<0 or nx>=w or ny<0 or ny>=h): continue
            if not stat:
                if visited[ny][nx] == -1:
                    visited[ny][nx] = -2
                    dq.append((ny, nx, stat))
            elif stat:
                if visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    dq.append((ny, nx, stat))
            
    answer = 1e9
    for i in range(h):
        if visited[i][0] > 0: answer = min(answer, visited[i][0])
        if visited[i][-1] > 0: answer = min(answer, visited[i][-1])

    for j in range(w):
        if visited[0][j] > 0: answer = min(answer, visited[0][j])
        if visited[-1][j] > 0: answer = min(answer, visited[-1][j])
            
    print(answer if answer!=1e9 else "IMPOSSIBLE")
    