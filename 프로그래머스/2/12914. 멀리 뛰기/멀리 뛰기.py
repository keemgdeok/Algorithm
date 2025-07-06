def solution(n):
    answer = 0
    # 1 2 3 4 5 6
    # 1 2 3 5 ..
    step=[0]*2001
    step[1]=1
    step[2]=2
    for i in range(3,n+1):
        step[i] = step[i-1] + step[i-2]
    
    return step[n] % 1234567