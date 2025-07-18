from collections import Counter

def solution(topping):
    ans = 0
    left = set()
    right = Counter(topping)
    
    for t in topping:
        right[t]-=1
        if right[t]==0:
            del right[t]
        left.add(t)
        
        if len(left) == len(right):
            ans+=1

    return ans