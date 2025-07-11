from collections import deque

def solution(priorities, location):
    ans = 0
    n = len(priorities)
    taskq=deque()
    for i in range(n):
        taskq.append([priorities[i], i])
    
    while True:
        flag=0
        proc = taskq.popleft()
        for i in range(len(taskq)):
            if proc[0] < taskq[i][0]:
                taskq.append(proc)
                flag=1
                break
                
        if flag==1:
            continue
        else:
            ans+=1
        
        if proc[1] == location:
            return ans
        