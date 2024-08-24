import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

# 사이클을 어떻게 찾고 판별하는가

def dfs(n):
    global cnt
    visited[n]=True 
    cycle.append(n)

    if visited[A[n]]:
        if A[n] in cycle: 
            cnt-=len(cycle[cycle.index(A[n]):])
        return
    else: dfs(A[n])

T=int(input())
for _ in range(T):
    N=int(input())
    A=[0]
    A+=list(map(int, input().strip().split()))

    visited=[False]*(N+1)

    cnt=N
    for i in range(1, N+1):
        if not visited[i]:
            cycle=[]
            dfs(i)

    print(cnt)