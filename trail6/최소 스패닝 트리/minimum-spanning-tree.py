import heapq

n, m = map(int, input().split())
edges = []

# 1~n 부모 자기자신으로 초기화
# parent[x][0] 부모 parent[x][1] 컴포넌트 크기
# 컴포넌트 크기는 항상 부모의 [1] 에 저장됨
parent = [[i, 1] for i in range(n+1)] 

def find(x):
    if x == parent[x][0]: return x
    parent[x][0] = find(parent[x][0])
    return parent[x][0]

def same(a, b):
    return find(a) == find(b)

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    
    if root_a == root_b: return
    
    p = min(root_a, root_b)
    c = max(root_a, root_b)
    
    # 1. 컴포넌트 넓이 새 부모 노드에 갱신
    # 2. 자식 노드의 부모 노드 갱신
    parent[p][1] = parent[p][1] + parent[c][1]
    parent[c][0] = parent[p][0]

ans = 0

for _ in range(m):
    s, e, w = map(int, input().split())

    heapq.heappush(edges, (w, s, e))
    
while edges:
    w, s, e = heapq.heappop(edges)
    
    if same(s, e): continue
    
    union(s, e)
    
    ans += w
    
    if parent[find(s)][1] == n:
        print(ans)
        break