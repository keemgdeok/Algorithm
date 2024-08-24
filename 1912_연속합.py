N=int(input())
A=list(map(int, input().split()))

dp=[0 for _ in range(N)]
dp[0]=A[0]
for i in range(1,N):
    if dp[i-1]<0: dp[i]+=A[i]
    else: dp[i]=dp[i-1]+A[i]
    
print(max(dp))