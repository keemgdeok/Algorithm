def solution(progresses, speeds):
    import math
    remain = []
    for i in range(len(progresses)):
        remain.append(math.ceil((100-progresses[i])/speeds[i]))
    
    answer = []
    max_day = remain[0]
    num=1
    for i in range(1,len(remain)):
        if remain[i] <= max_day:
            num+=1
        else:
            answer.append(num)
            max_day = remain[i]
            num=1
    answer.append(num)
    
    return answer