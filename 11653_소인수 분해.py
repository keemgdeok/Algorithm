N=int(input())

i=2
while N!=1:
    if N%i==0:
        N//=i
        print(i)
    if N%i!=0:
        i+=1

