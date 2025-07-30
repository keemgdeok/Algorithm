def solution(arr, divisor):
    ans=[]
    for a in arr:
        if a % divisor == 0:
            ans.append(a)
        
    if ans:
        return sorted(ans)
    else:
        return [-1]
    