import sys
import copy
import itertools
from collections import deque

input=sys.stdin.readline
N, M = map(int, input().split())

lab=[]
for line in sys.stdin.readlines():
    lab.append(list(map(int, line.split())))

# 벽 세우기 가능한 위치 찾기
blocks=[]
for i in range(N):
    for j in range(M):
        if lab[i][j]==0:
            blocks.append((i,j))
# 벽 위치 조합
comb3_blocks = list(itertools.combinations(blocks, 3))

def bfs(lab, visited, i, j):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    dq = deque()
    dq.append((i,j))
    visited[i][j] = True
    
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N and lab[ny][nx]==0 and not visited[ny][nx]:
                lab[ny][nx]=2
                visited[ny][nx]=True
                dq.append((ny, nx))

# gogo
answer=0
for block in comb3_blocks:
    # test deepcopy
    test_lab = copy.deepcopy(lab)
    
    # 벽 세우기
    for b in block:
        test_lab[b[0]][b[1]]=1

    # 바이러스 감염
    visited = [[False]*M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if test_lab[i][j]==2 and not visited[i][j]:
                bfs(test_lab, visited, i, j)

    # 계산
    count = 0
    for i in range(N):
        for j in range(M):
            if test_lab[i][j]==0:
                count+=1
    answer = max(answer, count)

print(answer)






        
