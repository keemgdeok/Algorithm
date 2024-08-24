N,M=map(int, input().split())
A=sorted(list(map(str, input().split())))
vowel=['a', 'e', 'i', 'o', 'u']
ans=[]

def dfs(dep=0, idx=0):
    if dep==N:
        vc=0; cc=0
        for i in range(N):
            if ans[i] in vowel: vc+=1
            else: cc+=1
        if vc>=1 and cc>=2:
            print("".join(ans))

    for i in range(idx, M):
        ans.append(A[i])
        dfs(dep+1, i+1)
        ans.pop()

dfs()
