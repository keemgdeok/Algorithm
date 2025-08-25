import math

def solution(arrayA, arrayB):
    ans = 0
    # find 철수&영희의 최대공약수
    A = findGCD(arrayA)
    B = findGCD(arrayB)

    if A>1:
        for b in arrayB:
            if b%A==0:
                A=0
                break
    
    if B>1:
        for a in arrayA:
            if a%B==0:
                B=0
                break
                
    if A==1:
        A=0
    if B==1:
        B=0
    
    return max(A, B)

def findGCD(cards):
    result = cards[0]
    for i in range(1, len(cards)):
        result = math.gcd(result, cards[i])
    
    return result

