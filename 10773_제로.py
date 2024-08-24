N=int(input())

score=[]
for i in range(N):
    num=int(input())
    if num>0:
        score.append(num)
    else:
        score.pop()

print(sum(score))
