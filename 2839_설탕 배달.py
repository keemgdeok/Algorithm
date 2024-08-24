import sys
input=sys.stdin.readline

N=int(input())
A=[1e7 for _ in range(5001)]
A[3]=1; A[5]=1

for i in range(3, N+1):
    for j in range(3, i):
        if A[j]==-1 or A[i-j]==-1: continue
        A[i]= min(A[j]+A[i-j], A[i])
    if A[i]==1e7: A[i]=-1

print(A[N])




