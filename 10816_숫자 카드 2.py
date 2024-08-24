import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int, input().strip().split())); A=sorted(A)
M=int(input())
F=list(map(int, input().strip().split()))

# 딕셔너리
count={}
for a in A:
    if a in count:
        count[a]+=1
    else:
        count[a]=1

# 이분 탐색
def binarySearch(low, high, target):
    if low > high:
        return 0
    mid = (low+high)//2
    if A[mid]==target: 
        return count.get(target)
    if A[mid]>target:
        return binarySearch(low, mid-1, target)
    elif A[mid]<target:
        return binarySearch(mid+1, high, target)
    
for f in F:
    print(binarySearch(0, len(A)-1, f), end=" ")

