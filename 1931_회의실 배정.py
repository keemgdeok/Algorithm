N=int(input())
time=[list(map(int, input().split())) for _ in range(N)]
time.sort(key=lambda x: (x[1], x[0]))

print(time)
cnt=0; end=0
for s, e in time:
    if s>=end:
        cnt+=1
        end=e

print(cnt)

"""
주어진 시작시간과 끝나는 시간들을 이용해서 가장 많은 회의의 수를 알기 위해서는 빨리 끝나는 회의 순서대로 정렬을 해야 한다. 이유는 간단하다. 빨리 끝날수록 뒤에서 고려해볼 회의가 많기 때문이다. 
빨리 시작하는 순서대로 정렬을 우선 한다면, 오히려 늦게 끝날 수 있기 때문이다.
"""

