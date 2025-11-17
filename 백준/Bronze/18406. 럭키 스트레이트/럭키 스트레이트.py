import sys
input = sys.stdin.readline

lst = [*map(int, input().rstrip())]

if sum(lst[:len(lst)//2]) == sum(lst[len(lst)//2:]):
    print("LUCKY")
else:
    print("READY")
