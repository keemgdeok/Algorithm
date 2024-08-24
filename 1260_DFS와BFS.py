from collections import deque

N, M, V = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)] # 0 열은 버림

for _ in range(M):
    i, j = map(int, input().split())
    graph[i][j] = graph[j][i] = 1


def dfs(graph, k):
    visited.add(k)
    print(k, end=" ")
    for i in range(1, N+1):
        if graph[k][i]==1 and i not in visited:
            dfs(graph, i)  



def bfs(grah, k):
    q = deque([k])
    visited.add(k)

    while q:
        k = q.popleft()
        visited.add(k)
        print(k, end=" ")

        for i in range(1, N+1):
            if graph[i][k] == 1 and i not in visited:
                q.append(i)
                visited.add(i)

visited = set()
dfs(graph, V)
print()
visited = set()
bfs(graph, V)


