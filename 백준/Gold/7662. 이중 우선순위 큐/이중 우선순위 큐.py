import sys
import heapq
input = sys.stdin.readline

T = int(input())

for t in range(T):
    Q = int(input())
    max_q = []; min_q = []
    valid = {}
    for q in range(Q):
        sign, num = input().split()
        num = int(num)
        if sign == "I":
            heapq.heappush(max_q, (-num, num))
            heapq.heappush(min_q, num)
            valid[num] = valid.get(num, 0) + 1
        elif sign == "D":
            if not (max_q and min_q): continue
            
            if num == 1:
                while max_q and valid.get(max_q[0][1], 0) == 0:
                    heapq.heappop(max_q)

                if max_q:
                    popped = heapq.heappop(max_q)[1]
                    valid[popped] -= 1
                
            elif num == -1:
                while min_q and valid.get(min_q[0], 0)==0:
                    heapq.heappop(min_q)
                if min_q:
                    popped = heapq.heappop(min_q)
                    valid[popped] -=1

    while max_q and valid.get(max_q[0][1], 0)==0:
        heapq.heappop(max_q)
    while min_q and valid.get(min_q[0], 0)==0:
        heapq.heappop(min_q)
        
    if not (max_q and min_q): print("EMPTY")
    else: print(max_q[0][1], min_q[0])
    
        