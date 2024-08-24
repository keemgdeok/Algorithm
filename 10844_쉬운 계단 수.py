N = int(input())

dp = [[0 for _ in range(10)] for _ in range(101)]
dp[1] = [1 for _ in range(10)]
dp[1][0]=0


for i in range(1, 101):
    for j in range(10):
        if j==0:
            dp[i][j+1]+=dp[i-1][j]
        elif j==9:
            dp[i][j-1]+=dp[i-1][j]
        else:
            dp[i][j-1]+=dp[i-1][j]
            dp[i][j+1]+=dp[i-1][j]

# print(dp[N])
print(sum(dp[N]) % 1000000000)
print(dp[3])