
def solution(numbers, target):
    return dfs(numbers, target)

def dfs(numbers, target, depth=0, curr=0):
    if depth == len(numbers):
        if curr == target:
            return 1
        else:
            return 0
    
    add = dfs(numbers, target, depth+1, curr-numbers[depth])
    sub = dfs(numbers, target, depth+1, curr+numbers[depth])
    
    return add + sub