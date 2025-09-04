import heapq

def solution(n, k, enemy):
    attacked = []
    for i in range(len(enemy)):
        heapq.heappush(attacked, -enemy[i])
        n-=enemy[i]
        
        while n<0 and k>0:
            n += -heapq.heappop(attacked)
            k-=1
            
        if n < 0 and k == 0:
            return i
        
    return len(enemy)