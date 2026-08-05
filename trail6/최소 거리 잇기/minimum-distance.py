n, m = map(int, input().split())

point = [(0, 0)] + [tuple(map(int ,input().split())) for _ in range(n)]

#edges = [tuple(map(int, input().split())) for _ in range(m)]

parent = [i for i in range(n+1)] # 1 ~ n 부모 자기자신으로 초기화

def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]

def same(a, b):
    return find(a) == find(b)

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    
    parent[ max(root_a, root_b) ] = min(root_a, root_b)

for _ in range(m):
    s, e = map(int, input().split())
    
    union(s, e)
    
edges = []
    
for s in range(1, n): # s < e
    for e in range(s+1, n + 1):
        sy, sx = point[s]
        ey, ex = point[e]
        
        dist = (abs(sy-ey)**2 + abs(sx-ex)**2)**0.5
        
        edges.append((dist, s, e))
        
edges.sort()
    
dist_sum = 0
edges_num = 0    
for dist, s, e in edges:
    
    if edges_num == n-1: break
    
    if same(s, e): continue
    
    union(s, e)
    
    dist_sum += dist
    edges_num += 1
    
print(f'{dist_sum:.2f}')