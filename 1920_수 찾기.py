N=int(input())
A=list(map(int, input().split())); A.sort()

M=int(input())
B=list(map(int, input().split()))

for b in B:
    low=0; high=N-1
    flag=0
    while low<=high:
        mid=(low+high)//2

        if b > A[mid]:
            low=mid+1
        elif b < A[mid]:
            high=mid-1
        else:
            flag=1
            break

    print(flag)
        

