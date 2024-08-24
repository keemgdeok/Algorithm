import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N=int(input())

tree=[[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, w=map(int, input().split())
    tree[a].append((b,w))
    tree[b].append((a,w))

def dfs(p, weight):
    for t, w in tree[p]:
        if visited[t]==-1:
            visited[t]=weight+w
            dfs(t, weight+w)

# 시작 정점에서 임의의 정점까지의 거리를 구하고 그 중 가장 먼거리를 구한다.
visited=[-1]*(N+1)
visited[1]=0
dfs(1,0)  

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
# 가장 먼 노드를 시작점으로하여 다시한번 가장 긴 거리를 찾는다.
idx=visited.index(max(visited))
visited=[-1]*(N+1)
visited[idx]=0
dfs(idx, 0)

print(max(visited))
