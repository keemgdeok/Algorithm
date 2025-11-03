import sys
from collections import deque
input = sys.stdin.readline

# input
N = int(input())
picture = [[*input().rstrip()] for _ in range(N)]

# requirement: 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하라
# point : BFS를 적록색약X 1번, 적록색약O 1번

def bfs(picture, visited, i, j):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    dq = deque()
    dq.append((i,j))
    visited[i][j] = True

    color = picture[i][j]
    while dq:
        y, x = dq.popleft()

        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[ny][nx] and picture[ny][nx] == color:
                dq.append((ny,nx))
                visited[ny][nx] = True
    
yes, no = 0, 0
# 적록색약 X
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            no+=1
            bfs(picture, visited, i, j)
        if picture[i][j] == "R":
            picture[i][j] = "G"

# 적록색약 O
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            yes+=1
            bfs(picture, visited, i, j)

print(no, yes)