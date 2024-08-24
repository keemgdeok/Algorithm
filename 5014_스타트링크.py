import sys
from collections import deque
input=sys.stdin.readline

F, S, G, U, D=map(int, input().split())
visited=[0 for _ in range(F+1)]
visited[S]=1

def bfs():
    dq=deque()
    dq.append(S)

    while dq:
        floor=dq.popleft()
        if floor==G: break
        for i in (U, -D):
            next=floor+i
            if 0<next<=F:
                if not visited[next]:
                    visited[next]=visited[floor]+1
                    dq.append(next)

bfs()
if not visited[G]: print("use the stairs")
else: print(visited[G]-1)

