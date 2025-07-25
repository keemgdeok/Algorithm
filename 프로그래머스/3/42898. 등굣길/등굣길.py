def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    # puddles
    for p in puddles:
        dp[p[1]][p[0]]=-1
        
    dp[1][1]=1
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp[i][j]==-1:
                dp[i][j]=0
                continue
            
            if i > 1:
                dp[i][j]+=dp[i-1][j]
            if j > 1:
                dp[i][j]+=dp[i][j-1]

            dp[i][j] %= 1000000007

    print(*dp)
    return dp[n][m]