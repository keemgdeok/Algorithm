from collections import Counter

def solution(weights):
    counter = Counter(weights)
    answer = 0
    
    # 1. 같은 무게끼리 짝 (1:1 비율)
    for count in counter.values():
        if count > 1:
            answer += count * (count - 1) // 2
            
            
    # 2. 다른 무게끼리 짝 (2:3, 2:4, 3:4 비율)
    ratios = [(2,3), (2,4), (3,4)]
    for w in counter:
        for r1, r2 in ratios:
            if (w * r1) % r2 == 0: 
                partner = (w * r1) // r2
                if partner in counter:
                    answer += counter[w] * counter[partner]
    
    return answer