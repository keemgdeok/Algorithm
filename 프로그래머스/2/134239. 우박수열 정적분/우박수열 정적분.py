def solution(k, ranges):
    answer = []
    
    # 우박수열 y구하기
    y=[]
    while k>1:
        y.append(k)
        if k%2==0: k//=2
        else: k=k*3 + 1
    y.append(1)
    
    # 정적분 구간
    n = len(y) - 1
    areas=[]
    for i in range(n):
        areas.append((y[i]+y[i+1])/2)
    
    # 문제 구간 넓이 구하기
    for r in ranges:
        x1 = r[0]; x2 = n + r[1]
        if x1 > x2: 
            answer.append(float(-1))
            continue
        answer.append(sum(areas[x1:x2]))
        
    return answer