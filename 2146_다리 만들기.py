from collections import deque

N=int(input())

graph=[list(map(int, input().split())) for _ in range(N)]
visited=[[False]*N for _ in range(N)]

dx=[1, -1, 0, 0]
dy=[0, 0, -1, 1]
# 섬 구분
def bfs1(a, b):
    global color
    dq=deque()
    dq.append((a, b))
    visited[a][b]=True
    graph[a][b]=color

    while dq:
        x, y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]; ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny]=True
                    graph[nx][ny]=color
                    dq.append((nx, ny))

def bfs2(island):
    global ans
    dist=[[-1]*N for _ in range(N)]

    dq=deque()

    for i in range(N):
        for j in range(N):
            if graph[i][j]==island:
                dq.append((i,j))
                dist[i][j]=0

    while dq:
        x, y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]; ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny]==0 and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[x][y]+1
                    dq.append((nx, ny))
                elif graph[nx][ny]>0 and graph[nx][ny]!=island:
                    ans=min(dist[x][y], ans)
                    return
                

color=1
for i in range(N):
    for j in range(N):
        if graph[i][j]==1 and not visited[i][j]:
            bfs1(i,j)
            color+=1


ans=1e9
for i in range(1, color):
    bfs2(i)


print(ans)