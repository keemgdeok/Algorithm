def solution(n):
    ans = [0]*(n+1)
    #1:1 2:2 3:3 4:5
    ans[1]=1
    ans[2]=2
    for i in range(3, n+1):
        ans[i] = (ans[i-1] + ans[i-2]) % 1000000007
    
    return ans[n]