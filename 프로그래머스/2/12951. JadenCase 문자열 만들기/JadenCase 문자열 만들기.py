def solution(s):    
    s = list(map(str, s.split(" ")))
    ans = []
    for a in s:
        ans.append(a.capitalize())
        
    return " ".join(ans)