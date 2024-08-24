import sys
sys.setrecursionlimit(10**9)

N=int(input())

def star11(n):
    if n==3: return ['  *  ', ' * * ', '*****']

    stars=star11(n//2)
    draw=[]

    for star in stars:
        draw.append(' '*(n//2)+star+' '*(n//2))
    for star in stars:
        draw.append(star + ' ' + star)
    
    return draw

print('\n'.join(star11(N)))