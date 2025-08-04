from collections import deque

def solution(x, y, n):
    if x==y:
        return 0
    
    dq=deque([(x, 0)])
    visited = {x}
    
    while dq:
        curr, cnt = dq.popleft()
        
        for nextval in [curr+n, curr*2, curr*3]:
            if nextval == y:
                return cnt+1
            if nextval < y and nextval not in visited:
                visited.add(nextval)
                dq.append((nextval, cnt+1))
    
    return -1


