import sys
input=sys.stdin.readline

N=int(input())
point=[list(map(int, input().split())) for _ in range(N)]
page=[[0 for _ in range(101)] for _ in range(101)]

for i in range(N):
    for j in range(10):
        for k in range(10):
            if page[point[i][0]+j][point[i][1]+k]==0:
                page[point[i][0]+j][point[i][1]+k]=1

ans=0
for i in range(101):
    for j in range(101):
        if page[i][j]==1: ans+=1

print(ans)
