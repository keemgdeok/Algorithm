import sys
import heapq

def solution(operations):
    min_hq=[]
    max_hq=[]
    for oper in operations:
        command, value = oper.split()
        value = int(value)
        
        if command == "I":
            heapq.heappush(min_hq, value)
            heapq.heappush(max_hq, (-value, value))
        else:
            if len(min_hq)==0:
                continue
            if value == 1: # 최댓값 삭제
                x = heapq.heappop(max_hq)[1]
                min_hq.remove(x) # 동기화
            else: # 최솟값 삭제
                x = heapq.heappop(min_hq)
                max_hq.remove((-x, x))
                
    if len(min_hq)==0:
        return [0, 0]
    else:
        return [heapq.heappop(max_hq)[1], heapq.heappop(min_hq)]
                
            
