def solution(numbers):
    ans = []
    for x in numbers:
        if x % 2 == 0:
            ans.append(x+1)
        else:
            rbit = '0' + bin(x)[2:]
            idx = rbit.rfind('01')
            
            rbit = rbit[:idx] + '10' + rbit[idx+2:]
            ans.append(int(rbit, 2))
    
    return ans