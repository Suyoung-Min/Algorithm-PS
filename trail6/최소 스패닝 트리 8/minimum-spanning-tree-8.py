n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    
    graph[s].append((e, w))
    graph[e].append((s, w))
    
import heapq

visited = [False] * (n+1)

start = 1
q = [(0, start)] # cost, v

weight_sum = 0


while q:
    cost, v = heapq.heappop(q)
    
    if visited[v]: continue
    visited[v] = True
    weight_sum += cost
    
    
    for next_v, next_cost in graph[v]:
        if not visited[next_v]:
            heapq.heappush(q, (next_cost, next_v))
            
print(weight_sum)