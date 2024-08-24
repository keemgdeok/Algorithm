string=str(input())

A=[]
for i in range(len(string)):
    A.append(string[i:])

A=sorted(A)
for i in range(len(string)):
    print(A[i])