def solution(n, left, right):
    ans=[]
    
    for i in range(left, right+1):
        row = i//n
        col = i%n
        ans.append(max(row, col) + 1)
    
    return ans