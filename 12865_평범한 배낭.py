import sys
input=sys.stdin.readline

N, K=map(int, input().split())
knapsack=[[0 for _ in range(K+1)] for _ in range(N+1)]
# knapsack=[[0]*(K+1)]*(N+1) 로 인해 많이 틀렸음, 미묘한 차이가 있다더라 ~
B=[[0,0]]
for _ in range(N):
    B.append(list(map(int, input().split())))


for i in range(1,N+1):
    for j in range(1,K+1):
        weight=B[i][0]; value=B[i][1]
        if j<weight:
            knapsack[i][j]=knapsack[i-1][j]
        else:
            knapsack[i][j]=max(value + knapsack[i-1][j-weight], knapsack[i-1][j])

print(knapsack[N][K])

