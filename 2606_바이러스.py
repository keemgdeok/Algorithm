N=int(input())
M=int(input())

graph=[[] for _ in range(N+1)]
for _ in range(M):
    a, b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(N+1)
visited[1]=True

def dfs(n):
    global cnt
    for i in graph[n]:
        if not visited[i]:
            visited[i]=True; cnt+=1 
            dfs(i)

cnt=0
dfs(1)
print(cnt)