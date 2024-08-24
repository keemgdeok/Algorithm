N, M=map(int, input().split())
A=list(map(int, input().split()))

left, right=0,1
cnt=0
while right<=N and left<=right:
    res=A[left:right]
    tot=sum(res)

    if tot==M:
        cnt+=1
        right+=1
    elif tot<M:
        right+=1
    else:
        left+=1
    
print(cnt)