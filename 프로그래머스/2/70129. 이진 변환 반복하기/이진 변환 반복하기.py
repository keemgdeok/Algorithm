def solution(s):
    answer = []
    cnt=0
    zero=0

    while len(s)!=1:
        n, z = deleteZero(s)
        zero+=z
        s = transformBinary(n)
        cnt+=1
        
    answer.append(cnt)
    answer.append(zero)
    
    return answer

# 0 제거
def deleteZero(string):
    res=''
    zero=0
    for s in string:
        if s == '0': 
            zero+=1
            continue
        res+=s
    return len(res), zero

# 이진 변환
def transformBinary(n):
    res=''
    while n>0:
        res+=str(n%2)
        n//=2
    return res[::-1]
        
    


