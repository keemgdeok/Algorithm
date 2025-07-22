def solution(n, t, m, p):
    ans = ''
    #1 n진법으로 숫자를 문자열로 t*m만큼 뱉는다
    #2 전체인원 m중 p번째마다 문자열에 추가
    
    number = '0'
    num=1
    mapping = {
        '10' : 'A',
        '11' : 'B',
        '12' : 'C',
        '13' : 'D',
        '14' : 'E',
        '15' : 'F'
    }
    
    while len(number) < t*m:
        tran = num
        addnum=''
        while tran > 0:
            residual = tran % n
            if residual >= 10:    
                residual = mapping[str(residual)]
            addnum += str(residual)
            tran //= n
        
        number+=addnum[::-1]        
        num+=1
        
    ans = number[p-1:t*m:m]
    
    
    return ans