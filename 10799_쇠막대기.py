A=input()
stack=[]

ans=0
for i in range(len(A)):
    if A[i]=='(':
        stack.append('(')
    else:
        if A[i-1]=='(':
            stack.pop()
            ans+=len(stack)
        else:
            stack.pop()
            ans+=1

print(ans)
