import sys
import heapq
input=sys.stdin.readline

N=int(input())
card=[]
for i in range(N):
    heapq.heappush(card, int(input()))

cost=0
while len(card)>1:
    a=heapq.heappop(card)
    b=heapq.heappop(card)

    cost+=a+b
    heapq.heappush(card, a+b)

print(cost)




