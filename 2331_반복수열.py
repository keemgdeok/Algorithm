N, M=map(int, input().split())
A=[N]

i=0
while True:
    tmp=0  
    for s in str(A[-1]):
        tmp+=int(s)**M

    if tmp in A: break
    
    A.append(tmp)

print(A.index(tmp))