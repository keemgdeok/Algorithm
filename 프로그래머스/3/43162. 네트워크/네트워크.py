from collections import deque
    
def bfs(now, visited, n, computers):
    dq=deque()
    dq.append(now)
    visited[now]=1
    
    while dq:
        s = dq.popleft()    
        for i in range(n):
            if computers[s][i]==1 and visited[i]==0:
                dq.append(i)
                visited[i]=1
    return 1


def solution(n, computers):
    ans=0
    visited=[0]*n
    
    for node in range(n):
        if visited[node]==0:
            ans+=bfs(node, visited, n, computers)
    return ans