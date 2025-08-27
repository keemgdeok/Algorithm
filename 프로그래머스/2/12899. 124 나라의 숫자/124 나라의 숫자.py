import math

def solution(n):
    ans = ''
    # 3진법으로 계산 + number replace
    while n>0:
        if n%3==0:
            res=4
            n//=3
            n-=1
        else:
            res=n%3
            n//=3
        ans+=str(res)
    
    return ans[::-1]