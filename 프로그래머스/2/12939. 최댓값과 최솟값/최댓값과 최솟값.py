def solution(s):
    answer = []
    l = list(map(int, s.split()))
    answer.append(str(min(l)))
    answer.append(str(max(l)))
    return (' ').join(answer)