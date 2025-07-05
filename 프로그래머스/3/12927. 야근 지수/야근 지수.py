import heapq

def solution(n, works):
    answer = 0
    heap = []
    
    # 최대힙 생성
    for w in works:
        heapq.heappush(heap, -w)
    

    while n>0:
        if heap[0] == 0:
            return 0
        heapq.heappush(heap, (heapq.heappop(heap)+1))
        n-=1    

    # calc
    for _ in range(len(heap)):
        answer += heapq.heappop(heap)**2
    
    return answer