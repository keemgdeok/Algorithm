def solution(diffs, times, limit):
    answer = 0
    ## result가 최소가 되는 level을 찾자
    low = 1
    high = max(diffs)
    
    while low <= high:
        mid = (low + high) // 2
        
        # time cost 계산
        total_cost = spend_time(diffs, times, mid)
        if total_cost <= limit:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return answer
            
def spend_time(diffs, times, level):
    cost = 0
    n = len(diffs)
    for i in range(n):
        if diffs[i] <= level:
            cost += times[i]
        else:
            cost += (times[i-1]+times[i]) * (diffs[i]-level)  + times[i]
            
    return cost
    
    
    
    
    