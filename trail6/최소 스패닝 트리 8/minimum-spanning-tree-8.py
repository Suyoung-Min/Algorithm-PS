n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

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

edges = []

for _ in range(m):
    s, e, w = map(int, input().split())
    
    edges.append((w, s, e))
    
edges.sort()

weight_sum = 0
edges_num = 0

for w, s, e in edges:
    
    if same(s, e): continue
    
    union(s, e)
    weight_sum += w
    edges_num += 1
    
    if edges_num == n-1:
        print(weight_sum)
        break