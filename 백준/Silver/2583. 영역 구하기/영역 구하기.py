from collections import deque
import sys
input = sys.stdin.readline

# input
M, N, K = map(int, input().split())
rec = [[*map(int,input().split())] for _ in range(K)]


"""
requirement : 
K개의 직사각형 내부를 제외한 나머지 부분이 
몇 개의 분리된 영역으로 나누어지는지, 
분리된 각 영역의 넓이가 얼마인지를 구하라

point :
직사각형을 제외한 나머지 개수 -> bfs 실행 횟수
분리된 각 영역의 넓이 -> bfs 반
"""

# K개의 직사각형
matrix = [[0]*N for _ in range(M)]
for xstart, ystart, xend, yend in rec:
    for i in range(ystart, yend):
        for j in range(xstart, xend):
            matrix[i][j]=-1

def bfs(matrix, y, x, count):
    area = 1
    
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    
    dq = deque()
    dq.append((y, x))
    matrix[y][x]=count

    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dy[i]; nx = x + dx[i]
            if 0<=ny<M and 0<=nx<N and matrix[ny][nx] == 0:
                matrix[ny][nx] = count
                dq.append((ny, nx))
                area += 1

    return area

count = 0
areas = []
for y in range(M):
    for x in range(N):
        if matrix[y][x] == 0:
            count+=1
            areas.append(bfs(matrix, y, x, count))

print(count)
print(*sorted(areas))
