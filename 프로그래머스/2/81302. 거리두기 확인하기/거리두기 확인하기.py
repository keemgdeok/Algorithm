from collections import deque

def solution(places):
    answer = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for place in places:
        # 모든 P 찾기
        p = []
        for i in range(5):
            for j in range(5):
                if place[i][j]=="P":
                    p.append((i,j))
        
        # 각 P마다 manhattan dist 계산 -> bfs
        flag = 0
        for py, px in p:   
            visited = [[0]*5 for _ in range(5)]
            manhattan = []
            dq = deque()
            dq.append((py, px))
            visited[py][px]=1
            while dq:
                y, x = dq.popleft()

                for i in range(4):
                    nx=dx[i]+x; ny=dy[i]+y
                    if 0<=nx<5 and 0<=ny<5 and visited[ny][nx]==0:
                        if place[ny][nx]=="X":
                            continue
                        dq.append((ny,nx))
                        visited[ny][nx]+=visited[y][x]+1
                        
                        if place[ny][nx]=="P":
                            manhattan.append(visited[ny][nx])
                            
            # manthattan dist 2이하 확인
            for mh in manhattan:
                if mh < 4:
                    flag=1
            if flag:
                answer.append(0)
                break
        if not flag:
            answer.append(1)
            
    return answer
