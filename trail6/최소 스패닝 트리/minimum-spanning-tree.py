import heapq

n, m = map(int, input().split())
edges = []

# 1~n 부모 자기자신으로 초기화
# parent[x][0] 부모 parent[x][1] 컴포넌트 크기
# 컴포넌트 크기는 항상 부모의 [1] 에 저장됨
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
    
    

edge_num = 0
edge_weight = 0

for _ in range(m):
    s, e, w = map(int, input().split())

    heapq.heappush(edges, (w, s, e))
    
while edges:
    w, s, e = heapq.heappop(edges)
    
    # 연결된 노드면 패스
    if same(s, e): continue
    
    union(s, e)
    
    edge_num += 1
    edge_weight += w
    
    if edge_num == n-1:
        print(edge_weight)
        break