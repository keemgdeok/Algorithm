import sys
import itertools
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
homes = []
chicken = []
for i in range(n):
    line = [*map(int, input().split())]
    for j in range(n):
        if line[j] == 1:
            homes.append((i, j))
        elif line[j] == 2:
            chicken.append((i, j))


comb_chicken = list(itertools.combinations(chicken, m))

result = 10**9
for comb in comb_chicken:
    city_dist = 0
    for hy, hx in homes:
        dist = 1e9
        for cy, cx in comb:
            dist = min(dist, abs(cy-hy) + abs(cx-hx))
        city_dist += dist
    result = min(result, city_dist)

print(result)



