import sys
sys.setrecursionlimit(10**9)

N=int(input())

def star10(n):
    if n==1: return '*'

    stars=star10(n//3)
    draw=[]

    for star in stars:
        draw.append(star*3)
    for star in stars:
        draw.append(star+' '*(n//3)+star)
    for star in stars:
        draw.append(star*3)
        
    return draw

print('\n'.join(star10(N)))

