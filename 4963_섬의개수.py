import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [-1, -1, -1,  0, 0,  1, 1, 1]
    dy = [-1,  0,  1, -1, 1, -1, 0, 1]
    graph[x][y]=0

    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0<= nx <h) and (0<= ny <w):
            if graph[nx][ny]==1:
                dfs(nx, ny)
                

w, h = map(int, input().split())

graph = []
for _ in range(h):
    graph.append(list(map(int, input().split())))
    
cnt=0
for i in range(h):
    for j in range(w):
        if graph[i][j] == 1:
            dfs(i, j)
            cnt+=1

print(cnt)














