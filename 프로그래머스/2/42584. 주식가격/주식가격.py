
def solution(prices):
    ans = []
    
    n = len(prices)
    for i in range(n):
        curr = prices[i]
        time = 0
        for j in range(i+1, n):
            time+=1
            if curr > prices[j]:
                break
        ans.append(time)
    
    return ans