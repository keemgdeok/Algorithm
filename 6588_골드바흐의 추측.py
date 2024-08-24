import sys
input=sys.stdin.readline

N = 1000001
P = [True] * N

# 에라토스테네스의 체
for i in range(2, int(N**0.5)+1):
    if P[i]:
        for j in range(i+i, N, i):
            P[j]=False

# 골드바흐의 추측
while True:
    k = int(input())
    if k==0:
        break
    for i in range(3, len(P)):
        if P[i] and P[k-i]:
            print(k,'=',i,'+',k-i)
            break
    else:
        print("Goldbach's conjecture is wrong.")
    