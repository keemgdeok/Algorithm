def solution(s):
    try:
        int(s)
        if 4==len(s) or 6==len(s):
            return True
    except:
        return False
    
    return False