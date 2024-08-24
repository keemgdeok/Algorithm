import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int, input().split()))
dp=[[x for x in A] for _ in range(2)]

dp[1][0]=-1001

for i in range(1,N):
    dp[0][i]=max(dp[0][i-1]+A[i], A[i])
    dp[1][i]=max(dp[0][i-1], dp[1][i-1] + A[i])

print(max(max(dp[0]), max(dp[1])))
