import itertools

def solution(users, emoticons):
    answer = []
    # 할인율 10, 20, 30, 40% 에 따라 가입자 최대 늘리기, 판매액 늘리기 순
    
    # 모든 할인율 조합을 그대로 계산 후, (가입자, 판매액) 정렬 후 반환
    discounts = list(range(10, 50, 10))
    comb_discounts = list(itertools.product(discounts, repeat=len(emoticons)))
    
    for dct in comb_discounts:
        answer.append(registerCheck(users, emoticons, dct))
    
    answer = sorted(answer, key=lambda x : (-x[0], -x[1]))
    
    return answer[0]

def registerCheck(users, emoticons, discount):
    register = 0
    sales = 0
    for user in users:
        pay = 0
        for i in range(len(emoticons)):
            if user[0] <= discount[i]:
                pay += emoticons[i] * (1 - discount[i]*0.01) 
        if pay >= user[1]:
            register+=1
        else:
            sales+=pay
    
    return (register, sales)
            
    
    
    
    
    
    
    
    
    
    
    
    