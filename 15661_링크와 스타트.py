N=int(input())
graph=[list(map(int, input().split())) for _ in range(N)]
visited=[False]*N
ans=1e7



def dfs(iter):
    if iter==N:
        global ans
        start, link=0,0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start+=graph[i][j]
                elif not visited[i] and not visited[j]:
                    link+=graph[i][j]
        ans=min(ans, abs(start-link))
        return
    
    visited[iter]=True
    dfs(iter+1)
    visited[iter]=False
    dfs(iter+1)

dfs(0)
print(ans)
        