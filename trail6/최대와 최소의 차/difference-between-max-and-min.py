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

edges_0 = []
edges_1 = []

for _ in range(m):
    s, e, t = map(int, input().split())
    
    if t == 0:
        edges_0.append((s, e))
    elif t == 1:
        edges_1.append((s, e))
        
# 최소 비용
safe_edges_num = 0
for s, e in edges_1:
    
    if same(s, e): continue
    
    union(s, e)
    
    safe_edges_num += 1
 
# remain   
r = (n - 1) - safe_edges_num
min_cost =  r**2
# 이러면 가능한 안전한 선들은 연결 완료

parent = [i for i in range(n+1)]
threat_edges_num = 0
for s, e in edges_0:
    if same(s, e): continue
    
    union(s, e)
    
    threat_edges_num += 1
    
max_cost = threat_edges_num**2
print(max_cost - min_cost)