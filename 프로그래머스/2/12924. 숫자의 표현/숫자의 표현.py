def solution(n):
    answer = 0
    
    for i in range(1, n):
        sum = 0
        for j in range(i, n):
            sum+=j
            if sum==n: 
                answer+=1
                break
            elif sum > n:
                break
        # 1 2 3 4 5 6 7 8 9 10
        # 1 1 2 1 2 2 2 1 2 2 
    
    
    return answer + 1