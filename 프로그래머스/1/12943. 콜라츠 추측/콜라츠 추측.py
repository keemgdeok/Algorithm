def solution(num):
    ans = 0
    while num > 1:
        if num % 2 == 0:
            num//=2
        else:
            num*=3
            num+=1
        ans+=1
        
    if num==1 and ans < 500:
        return ans
    else:
        return -1