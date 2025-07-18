from collections import Counter
import math

def solution(str1, str2):
    ans = 0
    str1 = str1.lower()
    str2 = str2.lower()
    
    A = Counter(makeMultiSet(str1))
    B = Counter(makeMultiSet(str2))
    
    intersection = A & B
    union = A | B
    
    count_inters = sum(intersection.values())
    count_union = sum(union.values())
    
    try:
        ans = count_inters/count_union
    except ZeroDivisionError:
        ans = 1
    
    return math.floor(ans * 65536)

def makeMultiSet(string):
    multiset = []
    for i in range(len(string)-1):
        if string[i:i+2].isalpha():
            multiset.append(string[i:i+2])
    return multiset