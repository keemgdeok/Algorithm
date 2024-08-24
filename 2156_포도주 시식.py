N=int(input())
A=[int(input()) for _ in range(N)]

dp=[0]*N

dp[0]=A[0]
if N>1:
    dp[1]=A[0]+A[1]
if N>2:
    dp[2]=max(dp[1], A[1]+A[2], A[0]+A[2])
for i in range(3, N):
    dp[i]=max(A[i]+A[i-1]+dp[i-3], A[i]+dp[i-2], dp[i-1])

print(dp[N-1])
