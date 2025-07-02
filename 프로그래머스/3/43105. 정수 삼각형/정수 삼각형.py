def solution(triangle):
    answer = 0
    n=len(triangle)
    
    triangle[1][0]+=triangle[0][0]
    triangle[1][1]+=triangle[0][0]
    original = [t[:] for t in triangle]

    for i in range(1,n-1):
        for j in range(i+1):
            triangle[i+1][j] = max(triangle[i][j]+original[i+1][j], triangle[i+1][j])
            triangle[i+1][j+1] = max(triangle[i][j]+original[i+1][j+1], triangle[i+1][j+1])    
    
    return max(triangle[n-1][:])