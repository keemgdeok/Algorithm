import heapq

N=int(input())
time=[]
for _ in range(N):
    start, end=map(int, input().split())
    time.append([start, end])
time.sort()

room=[]
heapq.heappush(room, time[0][1])

for i in range(1,N):
    if time[i][0] < room[0]:
        heapq.heappush(room, time[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, time[i][1])

print(len(room))