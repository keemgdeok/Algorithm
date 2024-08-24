N=int(input())
row=[0]*N
ans=0

def checkq(n):
    for i in range(n):
        if row[n]==row[i] or abs(row[n]-row[i])==abs(n-i):
            return False
    return True

def dfs(depth):
    global ans
    if depth==N:
        ans+=1
        return
    
    for i in range(N):
        row[depth]=i
        if checkq(depth):
            dfs(depth+1)

dfs(0)
print(ans)