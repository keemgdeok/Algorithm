N,M=map(int, input().split())

a=set()
for i in range(N):
    a.add(input())

b=set()
for i in range(M):
    b.add(input())

ans=sorted(list(a&b))

print(len(ans))

for a in ans:
    print(a)