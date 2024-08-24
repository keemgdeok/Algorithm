import sys
input=sys.stdin.readline

N=int(input())

A=[]
for _ in range(N):
    A.append(int(input()))

dp=[0]*301
dp[0]=A[0]
dp[1]=A[0]+A[1]
dp[2]=max(A[0]+A[2], A[1]+A[2])

for i in range(3, N):
    dp[i]=max(A[i]+dp[i-2], A[i]+A[i-1]+dp[i-3])


print(dp[N-1])
