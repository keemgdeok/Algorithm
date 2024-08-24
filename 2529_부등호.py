N=int(input())
A=list(map(str, input().split()))
visited=[False]*10
ans=[]

def check(a, b, op):
    if op=='>':
        if a < b: return False
    if op=='<':
        if a > b: return False
    return True

def dfs(depth, n):
    if depth==N+1:
        ans.append(n)
        return
    
    for i in range(10):
        if depth==0 or check(n[depth-1], str(i), A[depth-1]):
            if not visited[i]:
                visited[i]=True
                dfs(depth+1, n+str(i))
                visited[i]=False


dfs(0, '')
ans.sort()
print(ans[-1])
print(ans[0])






