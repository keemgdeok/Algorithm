def solution(n):
    answer = 0
    
    #1
    before = len(trans_binary(n).replace("0", ""))
    while True:
        n+=1
        if before == len(trans_binary(n).replace("0", "")):
            return n
    return None
    
def trans_binary(num):
    s = ""
    while num > 0:
        s += str(num % 2)
        num //= 2
    return s[::-1]
        