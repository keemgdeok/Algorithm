import sys
import math
input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]
B, C = map(int, input().split())

answer=0
for a in A:
    answer+=1
    rem = a-B
    if rem>0:
        answer += (rem+C-1) // C

print(answer)
