import math

def solution(n,a,b):
    ans = 0

    ln = int(math.log(n,2))

    while True:# n>=1:
        # n//=2
        
        if abs(a-b)==1 and (a+b+1)%4==0:
            return ans + 1
        else:
            ans+=1
            a= a//2 if a%2==0 else a//2+1
            b= b//2 if b%2==0 else b//2+1 


    