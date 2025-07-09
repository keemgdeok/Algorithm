from collections import deque

mapping = {
    '(' : ')',
    ')' : '(',
    '[' : ']',
    ']' : '[',
    '{' : '}',
    '}' : '{' 
}

def solution(s):
    ans = 0
    n = len(s)
    dq = deque(s)
    
    ans+=checkString(dq)
    for _ in range(n-1):
        dq.append((dq.popleft()))
        ans+=checkString(dq)
    
    return ans    
    

def checkString(string):
    check=[]
    for s in string:
        if s == '(' or s == '[' or s == '{':
            check.append(s)
        else:
            if len(check) > 0 and check[-1]==mapping.get(s):
                check.pop()
            else:
                return 0
    
    if len(check)==0:
        return 1
    else:
        return 0
                
    
    