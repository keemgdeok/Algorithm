import math

def solution(n, s):
    if n > s:
        return [-1]
    
    base = s//n
    remainder = s%n
    ans = [base]*n
    
    for i in range(remainder):
        ans[n-i-1]+=1
    
    return ans



    
    
    
    
    
    
    
    