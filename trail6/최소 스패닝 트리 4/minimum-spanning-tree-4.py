import heapq

n, m = map(int, input().split())
edges = []

node_type = [0] + input().split()

parent = [i for i in range(n+1)] 

def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]

def same(a, b):
    return find(a) == find(b)

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    
    parent[max(root_a, root_b)] = min(root_a, root_b)
    
    
for _ in range(m):
    s, e, w = map(int, input().split())
    heapq.heappush(edges, (w, s, e))
    
edges_num = 0
edges_weight = 0
    
while edges:
    w, s, e = heapq.heappop(edges)
    
    # 같은 종류의 정점이면 패스
    if node_type[s] == node_type[e]: continue
    
    # 이미 연결된 정점이면 패스
    if same(s, e): continue
    
    union(s, e)
    
    edges_num += 1
    edges_weight += w
    
if edges_num == n-1:
    print(edges_weight)    
else:
    print(-1)