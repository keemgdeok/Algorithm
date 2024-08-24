import sys
import heapq
input=sys.stdin.readline

N, K=map(int, input().split())
J=[]
for _ in range(N):
    heapq.heappush(J, list(map(int, input().split())))

C=[int(input()) for _ in range(K)]; C.sort()


ans=0; temp=[]
for c in C:
    while J and c>=J[0][0]:
        heapq.heappush(temp, -heapq.heappop(J)[1])        

    if temp:
        ans-=heapq.heappop(temp)
    elif not J:
        break
print(ans)
