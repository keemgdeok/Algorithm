import math

def solution(arr):
    answer = arr[0]
    
    for i in range(1, len(arr)):
        answer = LCM(answer, arr[i])
        
    return answer


def LCM(a, b):
    if a==0 or b==0:
        return 0
    return abs(a*b) // math.gcd(a, b)