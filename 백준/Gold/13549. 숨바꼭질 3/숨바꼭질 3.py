from collections import deque
import sys
input = sys.stdin.readline
MAX = 100001
N, K = map(int, input().split())
visited = [-1]*MAX

def bfs(start, end):
    dq = deque()
    dq.append(start)
    visited[start] = 0
    
    while dq:
        now = dq.popleft()
        
        if now == end:
            return visited[now]
        
        for nxt in (now*2, now-1, now+1):
            if not (0<=nxt<len(visited)): continue
            if visited[nxt] != -1: continue
            
            if now*2 == nxt:
                dq.appendleft(nxt)
                visited[nxt] = visited[now]
            else:
                dq.append(nxt)
                visited[nxt] = visited[now] + 1

print(bfs(N,K))
