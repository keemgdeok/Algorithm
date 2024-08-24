T=int(input())
A=[]

for i in range(T):
    A.append(int(input()))

dp=[0 for _ in range(max(A)+1)]  
dp[1]=1
dp[2]=2
dp[3]=4
for i in range(4,max(A)+1):
    dp[i]=(dp[i-1]+dp[i-2]+dp[i-3]) % 1000000009

for i in range(T):
    print(dp[A[i]] )

## 메모리 초과 고친 이유
#  %1000000009 를 출력에다가 하면 안되고, 구할때마다 해줘야함