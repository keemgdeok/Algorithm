N, M=map(int, input().split())
ans=[]

def dfs(depth, idx):
    if depth==M:
        print(*ans)
        return
    
    for i in range(idx,N+1):
        ans.append(i)
        dfs(depth+1, i)
        ans.pop()

dfs(0,1)