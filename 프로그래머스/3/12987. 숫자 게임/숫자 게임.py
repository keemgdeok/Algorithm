def solution(A, B):
    ans = 0
    # 매 차례 마다 A보다 크지만 최소가 되는 B를 찾아라
    A.sort(reverse=True)
    B.sort(reverse=True)
    n=len(A)
    for i in range(n):
        a = A.pop()
        for j in range(n):
            if len(B)==0: break
            if a < B.pop():
                ans+=1
                break
    
    return ans