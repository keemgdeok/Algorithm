import sys
from collections import deque
input = sys.stdin.readline

# 0. 입력 및 필요한 변수값 정의
n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dist = [[0]*n for _ in range(n)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# 1. 섬마다 영역 정의
def check_island(i, j, number):
    dq = deque()
    dq.append((i, j))
    visited[i][j] = True
    board[i][j] = number
    
    while dq:
        y, x = dq.popleft()
        for k in range(4):
            ny = y + dy[k]; nx = x + dx[k]
            if not (0<=ny<n and 0<=nx<n): continue
            if board[ny][nx] == 1 and not visited[ny][nx]:
                dq.append((ny,nx))
                visited[ny][nx] = True
                board[ny][nx] = number
    
number = 2
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            check_island(i, j, number)
            number+=1

# 2. 섬마다 바다로 진출해서 두개 만나는 영억을 기점으로 dist1 + dist2 을 구하면 bridge
def forward_sea(island):
    answer = sys.maxsize
    dq = deque(island)
    
    while dq:
        y, x = dq.popleft()

        for k in range(4):
            ny = y + dy[k]; nx = x + dx[k]
            if not (0<=ny<n and 0<=nx<n): continue
    
            if board[ny][nx] != 0 and board[ny][nx] != board[y][x]:
                answer = min(answer, dist[ny][nx] + dist[y][x]) 
            
            if board[ny][nx] == 0:
                board[ny][nx] = board[y][x]
                dist[ny][nx] = dist[y][x] + 1
                dq.append((ny, nx)) 
                
    return answer

island = []
for i in range(n):
    for j in range(n):
        if board[i][j] > 1:
            island.append((i, j)) 
            
print(forward_sea(island))
    