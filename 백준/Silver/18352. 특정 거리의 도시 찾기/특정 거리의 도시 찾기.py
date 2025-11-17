import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    
visited = [-1]*(n+1)
dq = deque([x])
visited[x]=0

while dq:
    curr = dq.popleft()
    for nxt in graph[curr]:
        if visited[nxt] == -1:
            visited[nxt] = visited[curr] + 1
            dq.append(nxt)

flag = 0
for i in range(1, n+1):
    if k == visited[i]:
        print(i)
        flag=1
if flag == 0 : print(-1)
