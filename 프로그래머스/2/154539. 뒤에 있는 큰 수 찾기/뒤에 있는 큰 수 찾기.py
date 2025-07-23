def solution(numbers):
    ans = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            prev = stack.pop()
            ans[prev] = numbers[i]
        
        stack.append(i)
            
    return ans