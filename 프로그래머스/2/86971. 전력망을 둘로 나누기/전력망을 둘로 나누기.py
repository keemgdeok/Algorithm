from collections import deque

def solution(n, wires):
    ans = 100
    # 1개씩 자르기
    for cut in range(n-1):
        # 가능한 송전탑 개수 확인
        count = bfs(n, wires, cut)
        ans = min(ans, abs((n-count) - count))

    return ans

def bfs(n, wires, cut):
    w = wires[:]
    w.pop(cut)
    
    visited=[0]*(n-1)
    count = set()
    
    dq=deque()
    v1, v2 = w[0]
    dq.append((v1, v2))
    visited[0]=1
    
    while dq:
        v1, v2 = dq.popleft()
        count.add(v1)
        count.add(v2)
        
        for i in range(n-2):
            if (v1 in w[i] or v2 in w[i]) and visited[i]==0:
                s, e = w[i]
                dq.append((s, e))
                visited[i]=1

    return len(count)
        
        
        
    
    



    