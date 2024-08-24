import sys

left = list(input())
right=[]


for _ in range(int(input())):
    command = list(sys.stdin.readline().split())

    if command[0]=="L" and left:
        right.append(left.pop())
    elif command[0]=="D" and right:
        left.append(right.pop(-1))
    elif command[0]=="B" and left:
        left.pop()
    elif command[0]=="P":
        left.append(command[1])

ans = left + right[::-1]
print(''.join(ans))
