import sys
input=sys.stdin.readline

N=int(input())
plus=[]
minus=[]

res=0  
for i in range(N):
    num=int(input())
    if num>1:
        plus.append(num)
    elif num<=0:
        minus.append(num)
    else:
        res+=num
    
plus.sort(reverse=True)
minus.sort()

# 양수 묶기
for i in range(0, len(plus), 2):
    if i+1 >= len(plus):
        res+=plus[i]
    else:
        res+=(plus[i]*plus[i+1])

# 음수 묶기
for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        res+=minus[i]
    else:
        res+=(minus[i] * minus[i+1])

print(res)
