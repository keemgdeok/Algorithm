import sys
input = sys.stdin.readline

N = int(input())

rope = sorted([int(input()) for _ in range(N)], reverse=True)

# require : 로프를 이용하여 들어올릴 수 있는 물체의 최대 중량
# point : 강한 로프부터 약한 로프까지 사용하되 이전값과 비교하며 갱신
max_weight = rope[0]
for i in range(1, N):
    max_weight = max(max_weight, rope[i]*(i+1))

print(max_weight)

