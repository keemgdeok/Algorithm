from collections import deque
import math

def solution(players, m, k):
    ans = 0
    server=deque([0]*k)
    add_server = 0
    time=0

    for player in players:
        # 서버 시간
        add_server-=server.popleft()
        
        # 서버 추가
        if player >= (add_server+1) * m:
            if player % m == 0:
                s = player//m + 1
            else:
                s = math.ceil(player/m)
            s-=add_server+1
            server.append(s)
            add_server+=s
            
        else:
            server.append(0)
        ans+=server[-1]


        
        
        print(f"{time}~{time+1}",add_server , server)
        time+=1
        
    return ans