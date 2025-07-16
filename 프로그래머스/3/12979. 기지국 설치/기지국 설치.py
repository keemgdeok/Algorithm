def solution(n, stations, w):
    import math
    ans = 0
    coverage = w*2+1
    pos = 0
    
    for s in stations:
        gap = (s - w) - (pos + 1)
        if gap > 0:
            ans+=math.ceil(gap/coverage)
        pos = s+w
            
    if pos < n:
        gap = n-pos
        ans+=math.ceil(gap/coverage)
        
        
    return ans