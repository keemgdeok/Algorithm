N=int(input())
dp=[1 for _ in range(10)]
for _ in range(N-1):
        for i in range(1, 10):
            dp[i]+=dp[i-1]
print(sum(dp) % 10007)
#print(dp[0]%10007)

# 제출은 다른풀이




