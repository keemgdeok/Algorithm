N = int(input())
p = [0] + list(map(int, input().split()))
dp = [0 for _ in range(N+1)]
dp.insert(1, p[1])

arr=[]
for i in range(1, N+1):
    for j in range(1,i+1):
        card=p[j]+dp[i-j]
        arr.append(card)
        dp[i]=min(arr)
        # print(arr)
    arr=[]
        

#print(dp)
print(dp[N])