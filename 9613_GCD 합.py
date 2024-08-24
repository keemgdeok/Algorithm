import math
T=int(input())

for _ in range(T):
    A=list(map(int, input().split()))
    ans=0
    for i in range(1,len(A)):
        for j in range(i+1,len(A)):
            ans+=math.gcd(A[i], A[j])
    print(ans)

    