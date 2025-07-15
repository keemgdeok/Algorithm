from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0 
    bridge=deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    current_weights = 0
    
    while truck_weights:
        time+=1
        
        current_weights -= bridge.popleft()
        
        if current_weights + truck_weights[0] <= weight:
            next_truck = truck_weights.popleft()
            bridge.append(next_truck)
            current_weights+=next_truck
        else:
            bridge.append(0)

        
    return time + bridge_length