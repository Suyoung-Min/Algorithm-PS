n, m = map(int, input().split())

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

    
        
edges  = []

for _ in range(m):
    s, e, v = map(int, input().split())
    
    edges.append((v, s, e))
    
edges.sort()
    
weight_sum = 0
edges_num = 0 


for v, s, e in edges:
    
    if same(s, e): continue
    
    union(s, e)
    weight_sum += v
    edges_num += 1
    
    if edges_num == n-1: # MST 가 완성됐으면
        weight_sum -= v # 마지막 가중치는 다시 빼서 MST 두개로
        print(weight_sum)
        break