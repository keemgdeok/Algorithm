N=int(input())

member=[]
for _ in range(N):
    age, name=input().split()
    age=int(age)
    member.append((age, name))

member.sort(key=lambda x:x[0])

for m in member:
    print(m[0], m[1])