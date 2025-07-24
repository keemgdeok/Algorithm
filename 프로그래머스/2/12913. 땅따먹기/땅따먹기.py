import copy

def solution(land):
    ans = 0
    row = len(land)
    dp = copy.deepcopy(land)
    
    for i in range(row-1):
        for j in range(4):
            if j==0:
                dp[i+1][1] = max(dp[i+1][1], land[i+1][1]+dp[i][0])
                dp[i+1][2] = max(dp[i+1][2], land[i+1][2]+dp[i][0])
                dp[i+1][3] = max(dp[i+1][3], land[i+1][3]+dp[i][0])
            elif j==1:
                dp[i+1][0] = max(dp[i+1][0], land[i+1][0]+dp[i][1])
                dp[i+1][2] = max(dp[i+1][2], land[i+1][2]+dp[i][1])
                dp[i+1][3] = max(dp[i+1][3], land[i+1][3]+dp[i][1])
            elif j==2:
                dp[i+1][0] = max(dp[i+1][0], land[i+1][0]+dp[i][2])
                dp[i+1][1] = max(dp[i+1][1], land[i+1][1]+dp[i][2])
                dp[i+1][3] = max(dp[i+1][3], land[i+1][3]+dp[i][2])
            elif j==3:
                dp[i+1][0] = max(dp[i+1][0], land[i+1][0]+dp[i][3])
                dp[i+1][1] = max(dp[i+1][1], land[i+1][1]+dp[i][3])
                dp[i+1][2] = max(dp[i+1][2], land[i+1][2]+dp[i][3])
        
    
    return max(dp[-1])