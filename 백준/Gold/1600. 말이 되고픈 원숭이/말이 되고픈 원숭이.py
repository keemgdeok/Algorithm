from collections import deque
import sys
input = sys.stdin.readline

# requirements: 원숭이가 최소한의 동작으로 시작지점에서 도착지점까지 갈 수 있는 방법을 알아내는 프로그램을 작성하시오.
# point: 어떻게 K 번의 말의 움직임을 구현할까

K = int(input())
w, h = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(h)]

hy = [2, 1, -1, -2, -2, -1, 1, 2]
hx = [-1, -2, -2, -1, 1, 2, 2, 1]
my = [0, 0, 1, -1]
mx = [1, -1, 0, 0]
visited = [[[-1]*w for _ in range(h)] for _ in range(K+1)]

dq = deque([(0, 0, K)])
visited[K][0][0] = 0
while dq:
    y, x, k = dq.popleft()
    curr = visited[k][y][x]

    if y == h-1 and x == w-1:
        print(curr)
        exit()

    for i in range(4):
        ny = y + my[i]; nx = x + mx[i]
        if not (0<=ny<h and 0<=nx<w): continue
        if matrix[ny][nx]==0 and visited[k][ny][nx]==-1:
            visited[k][ny][nx] = curr + 1
            dq.append((ny,nx,k))
    if k > 0:
        for i in range(8):
            ny = y + hy[i]; nx = x + hx[i]
            if not (0<=ny<h and 0<=nx<w): continue
            if matrix[ny][nx]==0 and visited[k-1][ny][nx]==-1:
                visited[k-1][ny][nx] = curr + 1
                dq.append((ny, nx, k-1))
print(-1)