import sys
input = sys.stdin.readline

# 지도의 크기: n, m / 주사위 놓은 곳의 좌표 x, y / 명령의 개수 k
n, m, y, x, k = map(int, input().split())
board = []
for _ in range(n):
    board.append([*map(int, input().split())])
actions = [*map(int, input().split())]

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.
# 주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여져 있는 곳의 좌표는 (x, y) 이다. 
# 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.

# 1: 밑, 2:북, 3:동, 4:서, 5:남, 6:윗
def roll_dice(direct, dice):
    # 동
    if direct == 1:
        tmp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = tmp
    # 서
    elif direct == 2:
        tmp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = tmp
    # 북
    elif direct == 3:
        tmp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = tmp
    # 남
    elif direct == 4:
        tmp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = tmp

dice = [0]*7
for act in actions:
    ny, nx = y, x
    if act == 1:
        nx+=1
    elif act == 2:
        nx-=1
    elif act == 3:
        ny-=1
    elif act == 4:
        ny+=1

    if not (0<=ny<n and 0<=nx<m):
        continue
    y, x = ny, nx
    
    roll_dice(act, dice)
    if board[y][x] == 0:
        board[y][x] = dice[1]
    else:
        dice[1] = board[y][x]
        board[y][x] = 0

    print(dice[6])