def solution(s):
    answer = [0,0]
    
    while s != "1":
        #1
        before = len(s)
        s = s.replace("0", "")
        after = len(s)
        answer[1] += before - after
        
        #2
        s = ""
        while after > 0:
            s += str(after % 2)
            after//=2
        s = s[::-1]
        answer[0] += 1

    return answer

        
    


