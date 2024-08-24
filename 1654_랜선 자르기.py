K, N=map(int, input().split())
line=[int(input()) for _ in range(K)]

low=1; high=max(line)
while low<=high:
    mid=(low+high)//2

    res=0
    for l in line:
        res+=l//mid

    if res>=N:
        low=mid+1
    else:
        high=mid-1

print(high)
