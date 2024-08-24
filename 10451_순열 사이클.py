T=int(input())


def cycle(i, idx):
    while True:
        if i==A[idx]:
            visited[idx]=True
            return 1
        visited[idx]=True
        idx=A[idx]
        
for _ in range(T):
    N=int(input())
    A=[0]+list(map(int, input().split()))

    visited=[False]*(len(A)+1)

    cnt=0
    for i in range(1, len(A)):
        if not visited[i]:
            cnt+=cycle(i, i)
    
    print(cnt)

    