import heapq
import math

def solution(picks, minerals):
    answer = 0
    
    if sum(picks) * 5 < len(minerals):
        minerals = minerals[:5 * sum(picks)]
    
    # stone을 기준으로 greedy, 5개씩
    picks_mine_table = {
        "diamond" : [1, 5, 25],
        "iron" :    [1, 1, 5],
        "stone" :   [1, 1, 1]
    }
    cost = []
    for i in range(0, len(minerals), 5):
        bundle = minerals[i:i+5]
        picked_diamond, picked_iron, picked_stone = 0, 0, 0
        for mine in bundle:
            picked_diamond += picks_mine_table[mine][0]
            picked_iron += picks_mine_table[mine][1]
            picked_stone += picks_mine_table[mine][2]
        
        cost.append((picked_stone, picked_iron, picked_diamond))
        
    print(cost)
    # 큰 cost 순으로 dia -> iron -> stone
    cost.sort(key=lambda x: x[0], reverse=True)
    for cost_stone, cost_iron, cost_diamond in cost:
        if picks[0] > 0:
            picks[0]-=1
            answer+=cost_diamond
        elif picks[1] > 0:
            picks[1]-=1
            answer+=cost_iron
        elif picks[2] > 0:
            picks[2]-=1
            answer+=cost_stone
        else:
            break
    
    return answer