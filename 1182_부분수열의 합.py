N,S=map(int, input().split())
A=list(map(int, input().split()))
temp=[]
cnt=0

def solve(idx):
    global cnt
    if sum(temp)==S and len(temp)>0:
        cnt+=1

    for i in range(idx,len(A)):
        temp.append(A[i])
        solve(i+1)
        temp.pop()
solve(0)
print(cnt)