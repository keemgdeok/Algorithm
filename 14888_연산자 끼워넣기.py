N=int(input())
A=list(map(int, input().split()))
op=list(map(int, input().split()))

maxi=-1e9
mini=1e9

def dfs(depth, tot, add, sub, mul, div):
    global mini, maxi
    if depth==N:
        mini=min(tot, mini); 
        maxi=max(tot, maxi)
        return
    
    if add>0:
        dfs(depth+1, tot+A[depth], add-1, sub, mul, div)
    if sub>0:
        dfs(depth+1, tot-A[depth], add, sub-1, mul, div)
    if mul>0:
        dfs(depth+1, tot*A[depth], add, sub, mul-1, div)
    if div>0:
        dfs(depth+1, int(tot/A[depth]), add, sub, mul, div-1)

    
dfs(1, A[0], op[0], op[1], op[2], op[3])  
print(maxi)
print(mini)