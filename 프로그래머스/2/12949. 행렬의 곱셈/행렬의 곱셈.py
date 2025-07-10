def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr2[0])
    ans = [[0]*col for _ in range(row)]
    
    for i in range(len(arr1)): # 행
        for j in range(len(arr2[0])): # 열
            for k in range(len(arr2)):
                ans[i][j] += arr1[i][k] * arr2[k][j]          
    
    return ans