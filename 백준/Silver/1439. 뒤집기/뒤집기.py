import sys
input = sys.stdin.readline

lst = input().rstrip()
count = [0, 0]

now = lst[0]
for i in range(1, len(lst)):
    if now != lst[i]:
        count[int(now)]+=1
        now = lst[i]   
count[int(now)]+=1

print(min(count))