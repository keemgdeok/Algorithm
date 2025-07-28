def solution(x, n):
    if x > 0:
        ans = [i for i in range(x, x*n+1, x)]
    elif x < 0:
        ans = [i for i in range(x, x*n-1, x)]
    else:
        ans = [0] * n
    return ans