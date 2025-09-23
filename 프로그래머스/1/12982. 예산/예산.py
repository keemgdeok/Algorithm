def solution(d, budget):
    answer = 0
    d = sorted(d)
    for i in range(1,len(d)+1):
        if budget >= sum(d[:i]):
            answer+=1
    
    return answer