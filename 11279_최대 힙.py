import heapq
import sys
input=sys.stdin.readline

N=int(input())

heap=[]
for i in range(N):
    num=int((input().strip()))*-1
    if num==0:
        if len(heap)==0: 
            print(0)
            continue
        print(-1*heap[0])
        heapq.heappop(heap)
    else:
        heapq.heappush(heap, num)
