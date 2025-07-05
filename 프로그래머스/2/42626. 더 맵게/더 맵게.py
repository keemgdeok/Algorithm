import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while True:
        if scoville[0] >= K:
            return answer
        if scoville[0] < K and len(scoville)==1:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + 2*second)
        answer+=1