

def solution(sticker):
    ## DP
    answer = 0
    if len(sticker)==1:
        return sticker[0]
    
    # detach sticker[0]    
    dp1 = [0] * len(sticker)
    dp1[0] = sticker[0]
    dp1[1] = max(sticker[0], sticker[1])
    for i in range(2, len(sticker)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])    
    
    # not detach sticker[0]
    dp2 = [0] * len(sticker)
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])

    answer = max(max(dp1), max(dp2))
    
    return answer