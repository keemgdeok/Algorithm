import sys
from collections import deque

m, n = input().split()
pictures = []
for line in sys.stdin.readlines():
    pictures.append(list(map(int,line.strip().split(" "))))

visited = [[0]*len(pictures[0]) for _ in range(len(pictures))]

def bfs(pictures, visited, i, j):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    dq = deque()
    dq.append((i,j))
    visited[i][j]=1
    area=1
    while dq:
        y, x = dq.popleft()   
        
        for i in range(4):
            ny = y + dy[i]; nx = x + dx[i]
            if 0<=ny<len(pictures) and 0<=nx<len(pictures[0]) and pictures[ny][nx]>0 and visited[ny][nx] == 0:
                dq.append((ny,nx))
                visited[ny][nx]=1
                area+=1
        
    return area

count = 0
extent = 0
for i in range(len(pictures)):
    for j in range(len(pictures[0])):
        if pictures[i][j] == 1 and visited[i][j]==0:
            count+=1
            area = bfs(pictures, visited, i, j)
            extent = max(extent, area)
# answer
print(count)
print(extent)
            


                

        
    