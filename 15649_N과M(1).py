N, M=map(int, input().split())
A=[i for i in range(1,N+1)]
visited=[False]*(N+1)
ans=[]

def dfs(depth):
    if depth==M:
        print(*ans)
        return
    
    for i in range(1,N+1):
        if not visited[i]:
            visited[i]=True
            ans.append(i)
            dfs(depth+1)
            visited[i]=False
            ans.pop()


dfs(0)