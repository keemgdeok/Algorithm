exp=input().split('-')
num=[]

for e in exp:
    tmp=sum(map(int, e.split('+')))
    num.append(tmp)

ans=num[0]
for i in range(1, len(num)):
    ans-=num[i]

print(ans)
