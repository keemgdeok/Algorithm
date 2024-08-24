N=int(input())
A=list(map(int, input().split()))
rev_A=A[::-1]
inc=[1]*N
dec=[1]*N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            inc[i]=max(inc[j]+1, inc[i])
        if rev_A[i] > rev_A[j]:
            dec[i]=max(dec[j]+1, dec[i])


res=[0 for _ in range(N)]
dec=dec[::-1]
for i in range(N):
    res[i]=inc[i]+dec[i]-1
print(max(res))

print(inc)