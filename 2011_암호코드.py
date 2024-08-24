code=[0]
code+=list(input())

if code[1]=='0':
    print(0)
    exit()

n=len(code)
dp=[0]*n
dp[0]=dp[1]=1

for i in range(2, n):
    first=int(code[i])
    tenth=int(code[i-1])*10+int(code[i])

    if first > 0: dp[i]+=dp[i-1]
    if tenth >=10 and tenth<=26: dp[i]+=dp[i-2]


print(dp[n-1]%1000000)