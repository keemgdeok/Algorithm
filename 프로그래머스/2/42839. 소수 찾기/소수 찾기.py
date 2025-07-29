import itertools
import math

def solution(numbers):
    ans = 0
    
    for i in range(1, len(numbers)+1):
        combine = set(itertools.permutations(numbers, i))
        for com in combine:
            if com[0] == '0': continue
            num = ''.join(com)
            if num and isPrime(int(num)):
                ans+=1
    return ans

def isPrime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for n in range(3, math.isqrt(num)+1, 2):
        if num % n == 0:
            return False
    return True