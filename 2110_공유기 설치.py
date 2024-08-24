N, C=map(int, input().split())
home=sorted([int(input()) for _ in range(N)])

low=1; high=home[-1]-home[0]
res=0
while low<=high:
    mid=(low+high)//2
    curr=home[0]
    dist=1

    for i in range(1, len(home)):
        if home[i]>=curr+mid:
            dist+=1
            curr=home[i]

    if dist>=C:
        low=mid+1
    else:
        high=mid-1

print(high)
