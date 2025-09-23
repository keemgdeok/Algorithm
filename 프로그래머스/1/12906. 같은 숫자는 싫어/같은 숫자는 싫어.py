def solution(arr):
    answer = [10]
    for a in arr:
        if answer[-1] != a:
            answer.append(a)
        
    return answer[1:]