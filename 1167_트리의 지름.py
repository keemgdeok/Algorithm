N=int(input())

graph=[[] for _ in range(N+1)]
for _ in range(N):
    A=list(map(int, input().split()))
    i=1
    while A[i]!=-1:
        graph[A[0]].append((A[i], A[i+1]))
        i+=2
    A.clear()


def dfs(n, weight):
    for c, w in graph[n]:
        if visited[c]==-1:
            visited[c]=weight+w
            dfs(c, weight+w)

visited=[-1]*(N+1)
visited[1]=0
dfs(1,0)


idx=visited.index(max(visited))
visited=[-1]*(N+1)
visited[idx]=0
dfs(idx, 0)

print(max(visited))