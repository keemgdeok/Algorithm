def solution(clothes):

    # 경우의 수 -> 입는다 + 안입는다
    kind = dict()
    for _, t in clothes:
        kind[t] = kind.get(t, 0) + 1
    
    ans=1
    for i in kind.values():
        ans *= i+1
            
    return ans - 1