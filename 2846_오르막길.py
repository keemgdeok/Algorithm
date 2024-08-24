# 오르막길
size = int(input()) # 수열 size
way = list(map(int, input().split())) # 조건 수열

prev = way[0]
diff = 0
path = []

for N in way:
    if prev < N:
        diff += (N - prev)
        path.append(diff)
    else:
        diff = 0
        path.append(diff)
    prev = N

print(max(path))