def solution(data, col, row_begin, row_end):
    answer = 0
    sorted_data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    
    S=[]
    for mod in range(row_begin, row_end+1):
        s = 0
        for num in sorted_data[mod-1]:
            s+= num % mod
        S.append(s)
    
    if len(S)==1:
        return S[0]    
    answer=S[0] ^ S[1]
    for i in range(2, len(S)):
        answer = answer ^ S[i]
    
    return answer