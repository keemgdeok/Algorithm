def solution(storey):
    ans = 0
    while storey > 0:
        remainder = storey % 10
        next_digit = (storey // 10) % 10
        
        if remainder < 5 or (remainder == 5 and next_digit < 5):
            ans += remainder
            storey //= 10
        else:
            ans += 10 - remainder
            storey = storey // 10 + 1
    
    return ans