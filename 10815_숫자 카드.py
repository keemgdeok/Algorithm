import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int, input().strip().split())); A=sorted(A)
M=int(input())
F=list(map(int, input().strip().split()))

    
for f in F:
    low, high=0, N-1
    flag=0
    while low<=high:
        mid=(low+high)//2
        if A[mid] > f:
            high=mid-1
        elif A[mid] < f:
            low=mid+1
        else:
            flag+=1
            break
    print(flag, end=" ")
    

        
    