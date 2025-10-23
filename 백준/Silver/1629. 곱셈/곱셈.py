import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def power_mod(a, b, c):
    if b==1:
        return a % c

    half = power_mod(a, b//2, c)
    
    if b%2==0:
        return (half * half) % c
    else:
        return (half * half * a) % c

print(power_mod(A, B, C))