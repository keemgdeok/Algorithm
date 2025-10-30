import sys
input = sys.stdin.readline

# input
N = int(input())

line = sorted(list(map(int, input().split())))

for i in range(1,N):
    line[i]+=line[i-1]

print(sum(line))

