import math

def solution(n, k):
    answer = []
    number = [i for i in range(1, n+1)]
    k-=1
    
    while n>0:
        n-=1
        case = math.factorial(n)
        
        index = k // case
        k %= case
        
        answer.append(number.pop(index))

    return answer