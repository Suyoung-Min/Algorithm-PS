n = int(input())

node_cost = [int(input()) for _ in range(n)]

cost_map = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n # 0 ~ n-1

import heapq

q = []

for i in range(n):
    heapq.heappush(q, (node_cost[i], i)) # (cost, v)
    
cost_sum = 0
    
while q:
    cost, v = heapq.heappop(q)
    
    if visited[v]: continue
    visited[v] = True
    cost_sum += cost
    
    for e in range(len(cost_map[v])):
        if not cost_map[v][e]: continue
        
        if not visited[e]:
            heapq.heappush(q, (cost_map[v][e], e))
            
print(cost_sum)