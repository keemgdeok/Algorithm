import sys
N=int(input())
A=list(map(int, sys.stdin.readline().split()))

dp=[x for x in A]
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i]=max(dp[i], dp[j]+A[i] )
    
print(max(dp))

# 그림 그려서 다시 복습해보기 굿노트로

