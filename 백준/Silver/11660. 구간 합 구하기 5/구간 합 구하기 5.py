import sys
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

lst = []
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    lst.append((x1, y1, x2, y2))

# 시작
# 다이나믹 프로그래밍
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = matrix[0][0]
for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i-1][j-1]

for x1, y1, x2, y2 in lst:
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])