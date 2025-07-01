def solution(A,B):
    ans = 0
    A = sorted(A)
    B = sorted(B, reverse=True)
    
    for _ in range(len(A)):
        ans += A.pop() * B.pop()
    

    return ans