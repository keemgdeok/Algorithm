def solution(order):
    ans = 0
    stack = [0]
    n=1
    i=0
    while n <= len(order):
        stack.append(n)
        while i < len(order) and stack[-1] == order[i]:
            stack.pop()
            ans+=1
            i+=1
        n+=1
            
    
    return ans