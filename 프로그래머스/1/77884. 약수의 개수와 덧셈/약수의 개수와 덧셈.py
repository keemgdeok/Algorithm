def solution(left, right):
    answer = 0
    
    for n in range(left, right+1):
        # 1부터 n의 제곱근까지만 반복
        divisors=[]
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                # 제곱근이 아닌 경우, 짝이 되는 약수도 추가
                if i * i != n:
                    divisors.append(n // i)
                    
        count = len(divisors)
        if count%2==0:  answer+=n
        else:   answer-=n
    
    return answer