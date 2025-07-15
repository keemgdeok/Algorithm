def solution(bridge_length, weight, truck_weights):
    ans = 0
    # 대기 트럭을 앞에서 하나씩 빼서
    # 다리에 놓는다 - 조건: sum < weight
    # 경과 시간: 한 뭉탱이 * 다리길이 + 객체 수
    n = len(truck_weights)
    b = []
    if sum(truck_weights) <= weight and len(truck_weights) <= bridge_length:
        return len(truck_weights)*(bridge_length+1)
    
    for i in range(n):
        if weight >= sum(b) + truck_weights[i] and len(b) <= bridge_length:
            b.append(truck_weights[i])
        else:
            ans+=len(b)*(bridge_length+1)
            b=[]
            b.append(truck_weights[i])
    
        print(b, ans)
        

        
    return ans