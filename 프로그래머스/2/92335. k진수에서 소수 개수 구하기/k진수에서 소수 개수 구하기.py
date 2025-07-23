import math

def solution(n, k):
    ans = 0
    #1 n진수로 변환
    #2 4개의 조건을 만족하는 숫자 반환
    #3 소수인지 확인
    
    base = convertBase(n, k).split('0')
        
    for number in base:
        if not number:
            continue
        if isPrime(int(number)):
            ans+=1
            
    return ans

def convertBase(n, k):
    res = ''
    while n>0:
        res += str(n % k)
        n = n//k
    
    return res[::-1]

def isPrime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    for n in range(3, math.isqrt(number)+1, 2):
        if number % n == 0:
            return False
    return True
    
    
    
    
    