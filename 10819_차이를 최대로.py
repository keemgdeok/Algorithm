N=int(input())
A=list(map(int, input().split()))
visited=[False]*N

ans=0
def dfs(temp):
    global ans
    if len(temp)==N:
        tot=0
        for i in range(N-1):
            tot+=abs(temp[i]-temp[i+1])
        ans=max(ans, tot)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            temp.append(A[i])
            dfs(temp)
            visited[i]=False
            temp.pop()

dfs([])
print(ans)