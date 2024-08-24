import sys
input=sys.stdin.readline

N,M=map(int, input().strip().split())
tree=list(map(int, input().strip().split()))

# low는 무조건 1부터 시작해야함
low=1; high=max(tree)
while low<=high:
    mid=(low+high)//2
    
    res=0
    for log in tree:
        if log>mid: res+=log-mid

    if res>=M: low=mid+1
    else: high=mid-1

print(high)