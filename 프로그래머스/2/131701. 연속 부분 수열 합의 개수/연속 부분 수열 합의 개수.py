def solution(elements):
    answer = 0
    n = len(elements)
    
    res=[]
    for i in range(1, n+1): # 길이
        for j in range(n): # index
            if j+i > n:
                res.append(sum(elements[j:])+sum(elements[:(i+j)%n]))
            else:
                res.append(sum(elements[j:j+i]))  
    
    return len(set(res))