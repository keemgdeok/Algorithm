import sys
sys.setrecursionlimit(10000)

N=int(input())
S, E= map(int, input().split())
M=int(input())
graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)
res=[]

for _ in range(M):
    x, y=map(int, input().split())
    graph[x].append(y); graph[y].append(x)

def dfs(v, n):
    visited[v]=True

    if v==E: res.append(n)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, n+1)

dfs(S,0)
if len(res)==0: print(-1)  
else: print(res[0])

