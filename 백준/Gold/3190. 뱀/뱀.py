import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [[-1]*n for _ in range(n)]
k = int(input())
for _ in range(k):
    y, x = map(int, input().split())
    board[y-1][x-1] = -2 
l = int(input())
action = [input().split() for _ in range(l)]

# 동 -> 남 -> 서 -> 북
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

dq = deque([(0,0)])
board[0][0] = 1
time = 0
direct = 0
while True: # n-1: 머리 , 0: 꼬리
    y, x = dq[-1] # 머리

    ny = y + dy[direct]; nx = x + dx[direct]
    if not (0<=ny<n and 0<=nx<n) or board[ny][nx] > 0: # 벽 or 자기자신과 부딪힐때
        print(time+1)
        break

    # action 방향으로 한칸 이동
    dq.append((ny, nx))
    
    # 이동 후, 결과
    if board[ny][nx] == -1: 
        ty, tx = dq.popleft() # 꼬리 떼기
        board[ty][tx] = -1    
    
    board[ny][nx] = 1
    time += 1
    
    # action, 방향 설정
    if action and int(action[0][0]) == time:
        if action[0][1] == 'L':
            direct = (direct - 1 + 4) % 4
        elif action[0][1] == 'D':
            direct = (direct + 1) % 4
        action.pop(0)