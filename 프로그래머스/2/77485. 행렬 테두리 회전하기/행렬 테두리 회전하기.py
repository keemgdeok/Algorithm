def solution(rows, columns, queries):
    matrix = [[r*columns+c+1 for c in range(columns)] for r in range(rows)]
    ans = []
    
    for y1, x1, y2, x2 in queries:
        x1-=1; y1-=1; x2-=1; y2-=1
        prev = matrix[y1][x1]
        min_val = prev
                
        ## top
        for nx in range(x1+1, x2+1):
            matrix[y1][nx], prev = prev, matrix[y1][nx]
            min_val = min(min_val, matrix[y1][nx])

        ## right
        for ny in range(y1+1, y2+1):
            matrix[ny][x2], prev = prev, matrix[ny][x2]
            min_val = min(min_val, matrix[ny][x2])
        
        ## bottom
        for nx in range(x2-1, x1-1, -1):
            matrix[y2][nx], prev = prev, matrix[y2][nx]
            min_val = min(min_val, matrix[y2][nx])
        
        ## left
        for ny in range(y2-1, y1-1, -1):
            matrix[ny][x1], prev = prev, matrix[ny][x1]
            min_val = min(min_val, matrix[ny][x1])
         
        ans.append(min_val)

    return ans


