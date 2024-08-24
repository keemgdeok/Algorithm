N = int(input())

arr =[0,1,2,4]
ans=0
for _ in range(N):
    k = int(input())
    if k==1:
        ans=1
    elif k==2:
        ans=2
    elif k==3:
        ans=4
    else:
        i=4 
        while i<=k:
            ans=0
            ans =sum(arr[-3:])
            arr.append(ans)
            
            print(arr)
            i+=1
    print(arr[k])
