import sys
input=sys.stdin.readline

N=int(input())
graph=[list(map(int, input().split())) for _ in range(N)]
visited=[False for _ in range(N)]
ans=101


def dfs(D, ind):
    global ans
    if D==N//2:
        start, link=0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start+=graph[i][j]
                elif not visited[i] and not visited[j]:
                    link+=graph[i][j]
        ans=min(ans, abs(start-link))
        return  

    for i in range(ind, N):
        if not visited[i]:
            visited[i]=True
            dfs(D+1, i+1)
            visited[i]=False


dfs(0,0)
print(ans)


