import sys
input=sys.stdin.readline

N,M=map(int, input().rstrip().split())

A=list(map(int, input().rstrip().split()))
B=list(map(int, input().rstrip().split()))

ans=[]
i=0; j=0
# 코드 최적화
lenA=len(A); lenB=len(B)

while i!=lenA or j!=lenB:
    if i==lenA:
        ans.append(B[j]); j+=1
    elif j==lenB:
        ans.append(A[i]); i+=1
    else:
        if A[i] < B[j]:
            ans.append(A[i])
            i+=1
        else:
            ans.append(B[j])
            j+=1

print(*ans)