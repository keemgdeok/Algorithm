from collections import deque

def solution(progresses, speeds):
    ans = []
    time = deque()
    for i in range(len(progresses)):
        res = 100-progresses[i]
        t = res // speeds[i]
        if res%speeds[i]!=0:
            t+=1
        time.append(t)

 
    deploy=time.popleft()
    task=1
    while len(time)>0:
        nextprog = time.popleft()
        if deploy >= nextprog:
            task+=1
        else:
            deploy = nextprog
            ans.append(task)
            task=1       
        
        
    ans.append(task)
    return ans