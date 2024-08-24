N,M = map(int, input().split())
q=[i for i in range(1, N+1)]
res=[]

k=0
while len(q)>0:
    k=(k+(M-1))%len(q)
    res.append(str(q.pop(k)))

print("<", ", ".join(res)[:], ">", sep="")