import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)


def bfs(k):
    visited.add(k)
    
    for i in graph[k]:
        if i not in visited:
            bfs(i)


visited = set()
cnt=0
for i in range(1, N+1):
    if i not in visited:
        cnt+=1
        bfs(i)

print(cnt)
    
