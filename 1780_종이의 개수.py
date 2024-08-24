N=int(input())

graph=[list(map(int, input().split())) for _ in range(N)]
minus=0; zero=0; plus=0

def dfs(x, y, n):
    global minus, zero, plus

    num=graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j]!=num:
                for k in range(3):
                    for l in range(3):
                        dfs(x+k*n//3, y+l*n//3, n//3)
                return
            
    if num==-1: minus+=1
    elif num==0: zero+=1
    else: plus+=1

dfs(0,0,N)
print(minus)
print(zero)
print(plus)
