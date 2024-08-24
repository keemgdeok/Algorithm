import sys
sys.setrecursionlimit(10**9)

def dfs(depth ,idx):
    if depth==6:
        print(*ans)
        return

    for i in range(idx,k):
            ans.append(L[i])
            dfs(depth+1, i+1)
            ans.pop()
            
            
while True:
    A=list(map(int, input().split()))
    if A[0]==0: break
    k=A[0]; L=A[1:]

    ans=[]
    dfs(0,0)
    print()
