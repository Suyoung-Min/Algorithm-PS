n, m = map(int, input().split())

parent = [i for i in range(n+1)]

# 경로 압축
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
    
all_sum_weight = 0
edges = []

for _ in range(m):
    s, e, w = map(int, input().split())
    
    all_sum_weight += w
    
    edges.append((w, s, e))

edges.sort()

min_weight = 0
edges_num = 0
for w, s, e in edges:
    
    if same(s, e): continue
    
    union(s, e)
    min_weight += w
    edges_num += 1
    
    if edges_num == n-1:
        print(all_sum_weight - min_weight)
        break