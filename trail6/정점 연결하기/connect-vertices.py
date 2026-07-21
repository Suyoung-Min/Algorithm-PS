n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 2)]

# Please write your code here.

parent = [i for i in range(n+1)] # 1 ~ n 정점

def find(x):
    if parent[x] != x : # 루트 노드가 아닐 때 / 부모가 있을 때
        parent[x] = find( parent[x] )
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    
    parent[ max(root_a, root_b) ] = min(root_a, root_b)
    
def same(a, b):
    return find(a) == find(b)

for u, v in edges:
    union(u, v)
    
root_node_1, root_node_2 = int(1e10), int(1e10)
for i in range(1, n+1):
    tp = find(i)
    
    if tp < root_node_1 and tp < root_node_2:
        root_node_1 = tp
    elif root_node_1 < tp and tp < root_node_2:
        root_node_2 = tp
        
        
print(root_node_1, root_node_2)