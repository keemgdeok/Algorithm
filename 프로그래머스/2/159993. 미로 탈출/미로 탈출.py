from collections import deque

def solution(maps):
    col = len(maps[0])
    row = len(maps)
    
    # 시작점, 레버, 출구 위치 찾기
    for r in range(row):
        for c in range(col):
            if maps[r][c] == 'S':
                start = (r, c)
            elif maps[r][c] == 'L':
                lever = (r, c)
            elif maps[r][c] == 'E':
                end = (r, c)

    def bfs(start_pos, end_pos):
        q = deque([(start_pos[0], start_pos[1], 0)]) # (y, x, 비용)
        visited = [[False] * col for _ in range(row)]
        visited[start_pos[0]][start_pos[1]] = True
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while q:
            y, x, cost = q.popleft()

            if (y, x) == end_pos:
                return cost
            
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if 0 <= ny < row and 0 <= nx < col and not visited[ny][nx] and maps[ny][nx] != 'X':
                    visited[ny][nx] = True
                    q.append((ny, nx, cost + 1))
        
        return -1

    # 1. 시작 -> 레버
    start_to_lever = bfs(start, lever)
    
    # 2. 레버 -> 출구
    lever_to_end = bfs(lever, end)
    
    if start_to_lever == -1 or lever_to_end == -1:
        return -1
    
    return start_to_lever + lever_to_end