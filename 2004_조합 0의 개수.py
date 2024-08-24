N, M = map(int, input().split())

def cntNumber(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt

five_cnt = cntNumber(N,5) - cntNumber(M, 5) - cntNumber(N-M, 5)
two_cnt = cntNumber(N,2) - cntNumber(M, 2) - cntNumber(N-M, 2)
print(min(five_cnt, two_cnt))