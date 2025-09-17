def solution(n):
    answer = []
    
    def hanoi(n, start, via, end):
        if n==1: 
            answer.append([start, end])
            return None

        hanoi(n-1, start, end, via)
        answer.append([start, end])

        hanoi(n-1, via, start, end)
    
    hanoi(n, 1, 2, 3)
    
    return answer



    
    
    