import heapq

n, m = map(int, input().split())

parent = [i for i in range(n*m+1)]

edges = [] # (w, s, e)

for y in range(n):
    w = list(map(int, input().split())) # m-1 개
    
    for x in range(m-1):    
        s = 1 + y * m + x
        e = s + 1
        
        edges.append((w[x], s, e))
        
for y in range(n-1):
    w = list(map(int, input().split())) # m 개
    
    for x in range(m):
        s = 1 + y * m + x
        e = s + m
        
        edges.append((w[x], s, e))

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
    

edges.sort()

edges_num = 0
edges_weight = 0

for w, s, e in edges:
    if same(s, e): continue
    
    union(s, e)
    
    edges_num += 1
    edges_weight += w
    
    if edges_num == n*m - 1:
        print(edges_weight)
        break