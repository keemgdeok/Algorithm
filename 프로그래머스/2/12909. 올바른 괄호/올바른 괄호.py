def solution(s):
    ans = True
    stack=[]
    for input in s:
        if input == "(":
            stack.append(input)
        else:
            if len(stack)<1:
                return False
            else:
                stack.pop(-1)
                
    if len(stack) == 0: ans = True
    else: ans = False

    return ans