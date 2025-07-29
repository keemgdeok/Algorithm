def solution(a, b):
    if a==b:
        return a
    return sum([i for i in range(min(a,b), max(a, b)+1)])