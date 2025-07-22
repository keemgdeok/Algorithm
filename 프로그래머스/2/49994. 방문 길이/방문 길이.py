def solution(dirs):
    x, y = 0, 0
    nx, ny = 0, 0
    visited = set()
    
    for step in dirs:  
        if step == "U": 
            ny=y+1
        elif step == "D":
            ny=y-1
        elif step == "L":
            nx=x-1
        elif step == "R":
            nx=x+1
            
        if -5 > ny or ny > 5:
            ny = y
            continue
        if -5 > nx or nx > 5:
            nx = x
            continue
        
        path = tuple(sorted(((y, x), (ny, nx))))
        if path not in visited:
            visited.add(path)
        y=ny
        x=nx
         
    return len(visited)