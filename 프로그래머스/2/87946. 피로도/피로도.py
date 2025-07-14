from itertools import permutations

def solution(k, dungeons):
    ans = 0
    
    orders = permutations(dungeons, len(dungeons))
    
    for order in orders:
        fatigue=k
        num=0
        
        for dungeon in order:
            min_req = dungeon[0]
            cost = dungeon[1]
            
            if fatigue >= min_req:
                fatigue -= cost
                num+=1
            else:
                break
        
        ans=max(ans, num)

        
    return ans