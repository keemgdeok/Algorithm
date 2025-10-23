def solution(plans):
    answer = []
    # 진행중인 과제: stack 사용
    # plans 정렬 후 시간이 지남에 따라 stack에 넣고 유후시간에 빼서 진행
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h*60 + m
        plans[i][2] = int(plans[i][2])
        
    plans = sorted(plans, key = lambda x: x[1])
    
    stack=[]
    working = plans[0]
    for i in range(1, len(plans)):
        if sum(working[1:]) <= plans[i][1]: # 현재 시작 시간이 endtime 이상 -> 과제 시작
            answer.append(working[0])
            # 유후 시간 (현재 시작시간 - 이전 끝시간) 활용 
            idle = plans[i][1] - sum(working[1:])
            while stack and idle>0:
                stack[-1][-1], idle = stack[-1][-1]-idle, idle-stack[-1][-1]
                if stack[-1][-1]<=0:
                    answer.append(stack.pop()[0])     
        else: # 현재 시작 시간이 endtime 미만 -> 하던거 stack 옮기고 새 과제 시작 
            working[2] -= plans[i][1] - working[1] 
            stack.append(working)
        working = plans[i]

    answer.append(working[0])
    for _ in range(len(stack)):
        answer.append(stack.pop()[0])
    
    return answer