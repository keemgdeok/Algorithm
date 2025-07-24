import string

def solution(msg):
    ans = []
    dic = {chr(ord('A') + i): i + 1 for i in range(26)}
    next_idx=27
    idx=0
    while idx < len(msg):
        w = msg[idx]
        while idx + len(w) < len(msg) and w + msg[idx + len(w)] in dic :
            w += msg[idx + len(w)]
            
        ans.append(dic[w])
        
        if idx + len(w) < len(msg):
            c = msg[idx + len(w)]
            dic[w+c] = next_idx
            next_idx+=1
        
        idx+=len(w)
            
    return ans