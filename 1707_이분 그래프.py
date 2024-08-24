# 이분 그래프는 BFS를 할 때 같은 레벨의 정점끼리는 모조건 같은 색으로 칠해진다.
from collections import deque

T=int(input())

def bfs(n):
    global flag
    dq=deque()
    dq.append(n)
    i=0; visited[n]=1

    while dq:
        k = dq.popleft()

        for i in graph[k]:
            if not visited[i]:
                visited[i]=visited[k]*-1 # idea
                dq.append(i)
            if visited[k]+visited[i]!=0:
                flag=False
                return


for _ in range(T):
    N, M=map(int, input().split())
    graph=[[] for _ in range(N+1)]

    for _ in range(M):
        x, y=map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    visited=[0]*(N+1)    

    flag=True
    for i in range(1,N+1):
        if visited[i]==0:
            bfs(i)

    if flag: print("YES")
    else: print("NO")