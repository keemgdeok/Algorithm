
def solution(prices):
    ans = []
    
    n = len(prices)
    for i in range(n):
        curr = prices[i]
        time = 0
        for j in range(i+1, n):
            if curr > prices[j]:
                time+=1
                break
            time+=1
        ans.append(time)
    
    return ans