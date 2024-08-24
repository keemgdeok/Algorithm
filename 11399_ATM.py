N=int(input())
A=[0]
A+=sorted(list(map(int,input().split())), reverse=True)
ans=0

for i in range(1, len(A)):
    ans+=i*A[i]

print(ans)
