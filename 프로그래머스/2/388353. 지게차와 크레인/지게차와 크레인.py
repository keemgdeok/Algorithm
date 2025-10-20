from collections import deque

def solution(storage, requests):
    # 문자열 1개 -> 지게차, 문자열 2개 -> 크레인(모두 빼기)
    n = len(storage)
    m = len(storage[0])
    answer = n*m
    
    storage = [list(row) for row in storage]
    
    # 요청 받기
    for req in requests:
        if len(req) == 1: # 지게차
            storage, count = forklift(storage, req)
            
        elif len(req) == 2: # 크레인
            storage, count = crane(storage, req[0])
        
        answer-=count
            
    return answer 


def forklift(storage, req):
    row = len(storage)
    col = len(storage[0])
    count = 0

    visited = [[False]*(col) for i in range(row)]
    removed = set()
    dq = deque()
    
    for y in range(row):
        for x in range(col):
            if y==0 or y==row-1 or x==0 or x==col-1:
                dq.append((y,x))
                visited[y][x] = True 
        
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    while dq:
        y, x = dq.popleft()
        char = storage[y][x]
        
        # 맞는 경우 
        if char == req:
            removed.add((y, x))
        # 안맞는경우 -> 전파
        elif char is None:
            for i in range(4):
                ny = dy[i] + y; nx = dx[i] + x
                if 0<=ny<row and 0<=nx<col and not visited[ny][nx]:
                    visited[ny][nx] = True
                    dq.append((ny,nx))
        else: pass
    
    for y, x in removed:
        storage[y][x] = None
        count+=1
    
    return storage, count
    
    
    
def crane(storage, req):
    row = len(storage)
    col = len(storage[0])
    count = 0
    
    for i in range(row):
        for j in range(col):
            if storage[i][j] == req:
                storage[i][j] = None
                count+=1
                
                        
    return storage, count
                
    
    
    
    
    
    
    
    