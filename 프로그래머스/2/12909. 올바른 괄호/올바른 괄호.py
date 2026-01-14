def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        elif s[i] == ")":
            if stack:
                stack.pop()
            else:
                return False
    if not stack:
        return True
    return False