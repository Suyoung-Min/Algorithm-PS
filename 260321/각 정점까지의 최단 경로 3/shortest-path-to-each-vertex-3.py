n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [1e9] * (n+1)

for _ in range(m):
    s, e, dist = map(int, input().split())
    graph[s].append((e, dist))

# Please write your code here.

import heapq

def dijstra(start):
    q = []
    visited[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if visited[now] < dist: continue
        
        visited[now] = dist
        
        for edge in graph[now]:
            cost = dist + edge[1]
            
            if cost < visited[edge[0]]:
                visited[edge[0]] = cost
                heapq.heappush(q, (cost, edge[0]))
                
dijstra(1)

for i in range(2, n+1):
    if visited[i] == 1e9:
        print(-1)
    else:
        print(visited[i])