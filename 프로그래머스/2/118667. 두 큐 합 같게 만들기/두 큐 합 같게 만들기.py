from collections import deque

def solution(queue1, queue2):
    s1 = sum(queue1)
    s2 = sum(queue2)
    
    if (s1+s2) % 2 != 0:
        return -1
    
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    
    target = (s1+s2) // 2
    limit = len(queue1) * 4
    
    ans=0
    while ans < limit:
        if s1 == target:
            return ans
        elif s1 > target:
            val = dq1.popleft()
            dq2.append(val)
            s1-=val
            s2+=val
        else:
            val = dq2.popleft()
            dq1.append(val)
            s1+=val
            s2-=val
        ans+=1
        
    return -1
            
    
    
    
    
    
    