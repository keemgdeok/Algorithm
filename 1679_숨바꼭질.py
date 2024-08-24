from collections import deque

N, K=map(int, input().split())
MAX=10**5
graph=[0]*(MAX+1)

def bfs(n,k):
    dq=deque()
    dq.append(n)

    while dq:
        x=dq.popleft()
        if x==k: 
            print(graph[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=MAX and not graph[nx]:
                graph[nx]=graph[x]+1
                dq.append(nx)

bfs(N, K)

            

