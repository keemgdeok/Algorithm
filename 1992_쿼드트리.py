N=int(input())
graph=[list(input()) for _ in range(N)]

ans=[]
def dfs(x, y, n):
    global ans

    num=graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j]!=num:
                ans.append('(')
                for k in range(2):
                    for l in range(2):
                        dfs(x+k*n//2, y+l*n//2, n//2)
                ans.append(')')      
                return
                
    if num=='0': ans.append('0')
    else: ans.append('1')
    
dfs(0,0,N)
print(''.join(ans))
