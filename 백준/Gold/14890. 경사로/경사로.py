import sys

input = sys.stdin.readline

n, l = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]


def check_line(line):
    visited = [False]*n

    for i in range(n-1):
        # 같으면 continue
        if line[i] == line[i+1]:
            continue

        # 차이가 1이상 난다면 return False
        if abs(line[i] - line[i+1]) > 1:
            return False

        # 현재 칸이 더 낮다면
        if line[i] < line[i+1]:
            for j in range(l):
                if i-j<0 or line[i]!=line[i-j] or visited[i-j]:
                    return False
                visited[i-j] = True
        # 현재 칸이 더 높다면 line[i] > line[i+1]
        else:
            for j in range(l):
                if i+1+j >= n or line[i+1] != line[i+1+j] or visited[i+j+1]:
                    return False
                visited[i+1+j] = True

    return True

count = 0

# row
for row in board:
    if check_line(row):
        count+=1

for col in zip(*board):
    if check_line(col):
        count+=1

print(count)
