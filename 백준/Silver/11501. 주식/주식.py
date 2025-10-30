import sys
input = sys.stdin.readline

# input
T = int(input())
for t in range(T):
    # requirement : 날 별로 주식의 가격을 알려주었을 때, 최대 이익
    # point : 거꾸로 순회하면서 판다
    N = int(input())
    prices = [*map(int, input().split())]

    max_price = 0
    profit = 0    
    for i in range(N-1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            profit += max_price - prices[i]

    print(profit)