def solution(n):
    triangle = [[0]*(i+1) for i in range(n)]
    directions = [(1,0), (0,1), (-1,-1)]
    row, col = 0, 0
    direct = 0
    
    for num in range(1, n*(n+1)//2+1):
        triangle[row][col] = num
        
        next_row = row + directions[direct][0]
        next_col = col + directions[direct][1]
        
        if 0>next_row or next_row>=n or \
            0>next_col or next_col>=len(triangle[next_row]) or \
            triangle[next_row][next_col] != 0:
            direct = (direct + 1) % 3
            next_row = row + directions[direct][0]
            next_col = col + directions[direct][1]
            
        row, col = next_row, next_col
    
    res = []
    for t in triangle:
        res.extend(t)
     
    return res