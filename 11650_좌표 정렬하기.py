N=int(input())

A=[]
for _ in range(N):
    x, y=list(map(int, input().split()))
    A.append([y, x])

A=sorted(A)
for i in range(N):
    print(A[i][1], A[i][0])