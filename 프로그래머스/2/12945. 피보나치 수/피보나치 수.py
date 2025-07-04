def solution(n):
    N=[0]*(n+1)
    N[0]=0
    N[1]=1
    
    for i in range(2, n+1):
        N[i] = N[i-1] + N[i-2]
    
    
    return N[n] % 1234567