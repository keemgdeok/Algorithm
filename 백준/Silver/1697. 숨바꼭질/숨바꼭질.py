from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 100001
visited = [-1]*MAX

def bfs(visited, start, end):
    dq = deque()
    dq.append(start)
    visited[start]=0
    while dq:
        now = dq.popleft()
        

        if now == end:
            return visited[now]
        
        for act in [now*2, now-1, now+1]:
            if not (0<=act<MAX): continue
            if visited[act]==-1:
                visited[act] = visited[now] + 1
                dq.append(act)

print(bfs(visited, n, k))