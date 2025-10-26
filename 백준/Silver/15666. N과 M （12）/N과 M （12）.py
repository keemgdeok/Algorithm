import sys
import itertools

input = sys.stdin.readline

N, M = map(int,input().split()) 

num = sorted(list(map(int, input().split())))

comb_num = sorted(list(set(itertools.combinations_with_replacement(num, M))))

for comp in comb_num:
    print(*comp)