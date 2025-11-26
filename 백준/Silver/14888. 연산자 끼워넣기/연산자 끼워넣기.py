import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
num = [*map(int, input().split())]
sign = [*map(int, input().split())]


min_answer, max_answer = 10**9, -10**9
def dfs(result, depth):
    global min_answer, max_answer

    if depth == n-1:
        max_answer = max(max_answer, result)
        min_answer = min(min_answer, result)
        return 

    # 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다.
    for i in range(4):
        if sign[i] > 0:
            sign[i] -= 1
            if i == 0:
                dfs(result + num[depth+1], depth+1)
            elif i == 1:
                dfs(result - num[depth+1], depth+1)
            elif i == 2:
                dfs(result * num[depth+1], depth+1)
            elif i == 3:
                dfs(int(result / num[depth+1]), depth+1)
            sign[i] += 1

dfs(num[0], 0)
print(max_answer)
print(min_answer)
            