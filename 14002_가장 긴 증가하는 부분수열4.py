N = int(input())
A = list(map(int, input().split()))

dp=[1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i]=max(dp[j]+1, dp[i])
print(max(dp))

x=max(dp) # 여기서 거꾸로 가는게 핵심 !

ans=[]
for i in range(N-1, -1, -1):
    if dp[i] == x:
        ans.append(A[i])
        x-=1
ans.reverse()

for an in ans:
    print(an, end=' ')

