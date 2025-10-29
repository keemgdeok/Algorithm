from itertools import permutations
import re

def solution(user_id, banned_id):
    k = len(banned_id)
    
    # * -> .
    for i in range(k):
        banned_id[i] = banned_id[i].replace("*",".")
        
    comb_uid = list(permutations(user_id, k))
    
    valid = set()
    
    for uid in comb_uid:
        is_valid = True
        
        for i in range(k):
            user = uid[i]
            pattern = banned_id[i]
            
            if len(user) != len(pattern) or not re.fullmatch(pattern, user):
                is_valid = False
                break
        if is_valid:
            valid.add(frozenset(uid))
    
    return len(valid)