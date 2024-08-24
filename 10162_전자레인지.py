N=int(input())

a=300; b=60; c=10
A=0; B=0; C=0
while N!=0:
    if N>=a:
        A+=N//a
        N%=a
    elif N>=b:
        B+=N//b
        N%=b
    else:
        C+=N//c
        N%=c
    
    if N<10 and N>0:
        print(-1)
        exit()

print(A, B, C)