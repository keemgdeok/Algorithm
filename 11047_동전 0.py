N, K=map(int, input().split())

A=[]
for _ in range(N):
    A.append(int(input()))

count=0
for i in range(N-1,-1,-1):
    if K>=A[i]:
        count+=K//A[i]
        K%=A[i] 
    else: continue

print(count)


