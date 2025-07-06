def solution(k, tangerine):
    answer = 0
    box=dict()
    for t in tangerine:
        if t in box:
            box[t]+=1
        else:
            box[t]=1
    box = sorted(box.items(), key=lambda x: -x[1])
    
    for number, b in box:
        if b >= k:
            return answer + 1
        else: # b<=k
            k-=b
            answer+=1
             
    
