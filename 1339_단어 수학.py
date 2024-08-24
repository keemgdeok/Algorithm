import sys
input=sys.stdin.readline

N=int(input())
S=[input().strip() for _ in range(N)]
word={}

for s in S:
    x=len(s)-1
    for i in s:
        if i in word:
            word[i]+=10**x 
        else:
            word[i]=10**x
        x-=1

word=sorted(word.values(), reverse=True)
res=0
num=9
for k in word:
    res+=k*num
    num-=1

print(res)
