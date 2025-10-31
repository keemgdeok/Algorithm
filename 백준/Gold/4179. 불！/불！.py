from collections import deque
import sys
input = sys.stdin.readline

# input
R, C = map(int, input().split())
maze = [[*input().strip()] for _ in range(R)]

"""
requirement : 
지훈이가 불에 타기전에 탈출할 수 있는지의 여부,
얼마나 빨리 탈출할 수 있는지를 결정

point :
2번의 BFS
first : 지훈이가 가장자리 까지 도달하는 BFS 
second : 불이 퍼지는 BFS

first + second 의 가장자리를 비교하여 값 도출
"""

escaped = [[0]*C for _ in range(R)]
INF = float('INF')
fired = [[INF]*C for _ in range(R)]

start_fired=[]
for y in range(R):
    for x in range(C):
        if maze[y][x] == 'J':
            start_jh = (y, x)            
        elif maze[y][x] == "F":
            start_fired.append((y, x))
        
# BFS 시작
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

# fire
fired_dq = deque()
for y, x in start_fired:
    fired_dq.append((y,x))
    fired[y][x] = 1

while fired_dq:
    y, x = fired_dq.popleft()
    for i in range(4):
        ny = y + dy[i]; nx = x + dx[i]
        if 0<=ny<R and 0<=nx<C and maze[ny][nx] != "#" and fired[ny][nx]==INF:
            fired[ny][nx] = fired[y][x] + 1
            fired_dq.append((ny, nx))
            
# Jihoon
jh_dq = deque()
jh_dq.append(start_jh)
escaped[start_jh[0]][start_jh[1]]=1

while jh_dq:
    y, x = jh_dq.popleft()
    if y==0 or y==R-1 or x==0 or x==C-1:
        print(escaped[y][x]); exit()
    for i in range(4):
        ny = y + dy[i]; nx = x + dx[i]
        if 0<=ny<R and 0<=nx<C and maze[ny][nx] == "." and not escaped[ny][nx] and escaped[y][x] + 1 < fired[ny][nx]:
            jh_dq.append((ny,nx))
            escaped[ny][nx] = escaped[y][x] + 1

print("IMPOSSIBLE")   
    

