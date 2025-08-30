import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    INF = float('inf')
    distance = [INF] * (N+1)
    
    def dijkstra(start):
        hq = []
        distance[1]=0
        heapq.heappush(hq, (0, start))
        
        while hq:
            dist, now = heapq.heappop(hq)
            if distance[now] < dist:
                continue
            
            for neighbor, cost in graph[now]:
                new_cost = dist + cost
                
                if new_cost < distance[neighbor]:
                    distance[neighbor] = new_cost
                    heapq.heappush(hq, (new_cost, neighbor))
                
    dijkstra(1)
    
    
    ans=0
    for d in distance:
        if d<=K: ans+=1

    return ans