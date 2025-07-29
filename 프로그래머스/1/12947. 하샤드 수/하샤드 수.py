def solution(x):
    ha = sum([int(i) for i in str(x)])
    if x % ha == 0:
        return True
    return False