N=int(input())
K=[int(input()) for _ in range(N)]
K.sort()

ans=[]
for k in K:
    ans.append(k*N)
    N-=1

print(max(ans))
