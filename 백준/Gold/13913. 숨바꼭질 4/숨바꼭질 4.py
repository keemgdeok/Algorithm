from collections import deque
import sys
input = sys.stdin.readline
MAX = 100001
N, K = map(int, input().split())
visited = [-1]*MAX
parent = [-1]*MAX

def bfs(visited, start, end):
    dq = deque()
    dq.append(start)
    visited[start] = 0
    
    while dq:
        now = dq.popleft()
        
        if now == end:
            return visited[K]
        
        for nxt in (now*2, now-1, now+1):
            if not (0<=nxt<len(visited)): continue
            if visited[nxt] != -1: continue
            dq.append(nxt)
            visited[nxt] = visited[now] + 1
            parent[nxt] = now
            
            
print(bfs(visited, N, K))

path = []
curr = K
while curr != N:
    path.append(curr)
    curr = parent[curr]
path.append(N)
print(*path[::-1])
