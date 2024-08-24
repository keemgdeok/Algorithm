N=int(input())

member=[]
for i in range(N):
    name, han, eng, math=input().split()
    han,eng,math=int(han), int(eng), int(math)
    member.append([name, han, eng, math])
print(member)
member.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for m in member:
    print(m[0])
