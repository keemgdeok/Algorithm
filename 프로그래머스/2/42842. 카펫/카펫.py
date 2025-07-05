def solution(brown, yellow):
    answer = []
    
    for i in range(1, int(yellow//2)+2):
        if yellow % i == 0:
            j = yellow//i # j>i
            if brown == 2*(i+j+2):
                return [j+2, i+2]
    return 0
        