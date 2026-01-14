def solution(s):   
    ans = list(map(str, s.split(" ")))

    return " ".join(list(map(str.capitalize, ans)))