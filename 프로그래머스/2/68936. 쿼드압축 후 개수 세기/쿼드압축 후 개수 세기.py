import sys
sys.setrecursionlimit(10**9)

def solution(arr):      
    return quadcomp(0, 0, len(arr), arr)

def quadcomp(x, y, size, arr):
    standard = arr[x][y]
    flag = True
    
    for i in range(x, x+size):
        for j in range(y, y+size):
            if standard != arr[i][j]:
                half = size // 2
                res1 = quadcomp(x, y, half, arr)
                res2 = quadcomp(x+half, y, half, arr)
                res3 = quadcomp(x, y+half, half, arr)
                res4 = quadcomp(x+half, y+half, half, arr)
                
                return [res1[0]+res2[0]+res3[0]+res4[0],
                       res1[1]+res2[1]+res3[1]+res4[1]]
                
    if standard == 0:
        return [1, 0]
    elif standard == 1:
        return [0, 1]
               