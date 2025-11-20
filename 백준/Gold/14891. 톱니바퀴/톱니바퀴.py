import sys
from collections import deque
input = sys.stdin.readline

gear = [deque(map(int,input().rstrip())) for _ in range(4)]
k = int(input())
action = [[*map(int, input().split())] for _ in range(k)]

for num, direct in action:
    # 무엇을 움직이는가
    num-=1
    flag = [0]*4
    flag[num] = direct

    # 왼쪽 전파
    for i in range(num, 0, -1):
        if gear[i][6] != gear[i-1][2]:
            flag[i-1] = -flag[i]
        else:
            break
    # 오른쪽 전파
    for i in range(num, 3):
        if gear[i][2] != gear[i+1][6]:
            flag[i+1] = -flag[i]
        else: 
            break
    
    # 회전
    for i in range(4):
        if flag[i] == 1:
            gear[i].rotate(1)
        elif flag[i] == -1:
            gear[i].rotate(-1)

result = 0
for i in range(4):
    if gear[i][0] == 1:
        result += 2**i
print(result)
