import math

def solution(n):
    ans=0
    m=10
    loc=[0]*(m+1)
    loc[1]=1

    while n > m:
        if n%2==1: ans+=1
        n//=2
        
        
    for i in range(2, m+1):
        if i%2==0: # even
            loc[i] = min(loc[i//2], loc[i-1]+1)
        else: #odd
            loc[i] = min(loc[i//2]+1, loc[i-1]+1)
            
    return loc[n] + ans