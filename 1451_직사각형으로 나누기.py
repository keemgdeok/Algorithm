import sys
input=sys.stdin.readline

N, M=map(int, input().split())
A=[[] for _ in range(N)]
for i in range(N):
    A[i]=list(map(str, input().strip()))

rec1, rec2, rec3=[], [], []

maxi=0
i=0; j=0
def dfs(depth, i, j):
    global ans
    if depth==N*M:
        ans=sum(rec1)*sum(rec2)*sum(rec3)
        maxi=max(maxi, ans)

    rec1.append(A[i][j])
    dfs(depth+1, i+1, j)
    
    dfs(depth+1, i, j+1)

    dfs(depth+1, i+1, j+1)