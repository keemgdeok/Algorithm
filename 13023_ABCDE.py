import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())

relations = [[] for _ in range(N)]
visited = [False] * 2001

for _ in range(M):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

ans = False

def dfs(k, depth):
    global ans
    visited[k] = True
    if depth == 4:
        ans = True
        return

    for i in relations[k]: # k번 노드에 대해 순회
        if visited[i]==False:
           visited[i]=True # k노드의 친구 i에 대해 True
           dfs(i, depth+1)
           visited[i]=False  # 재귀 끝났으면 False
           # 다시 False 하는 이유는 i는 다른 k'의 노드에도
           # 있을수 있으므로 한번 True 하면 다른 k'노드에서도
           # 방문했다고 중복 걸리기 때문
           # 여기가 틀림


for i in range(N):
    dfs(i, 0)
    visited[i] =False # 각 노드마다 순회하므로 다시 False로 초기화
    # 여기도 틀림
    if ans: break

if ans:
    print(1)
else:
    print(0)

