import sys
sys.setrecursionlimit(100000)

N=int(input())

graph=[[] for _ in range(N+1)]
for _ in range(N-1):
    a, b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(N+1)

def dfs(idx):
    for i in graph[idx]:
        if not visited[i]:
            visited[i]=idx
            dfs(i)

dfs(1)
for i in range(2, N+1):
    print(visited[i])