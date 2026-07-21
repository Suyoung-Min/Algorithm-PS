n, m, k = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]
path = list(map(int, input().split()))

# Please write your code here.

tree = [[] for _ in range(n+1)]
parent = [i for i in range(n+1)] # 초기 부모 노드는 자기자신

def find(x):
    if parent[x] != x : # 루트 노드 아니면 == 부모가 따로 있으면
        parent[x] = find( parent[x] )
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    parent[ max(root_a, root_b) ] = min(root_a, root_b)

def same(a, b):
    return find(a) == find(b)


for u, v in edges:
    tree[u].append(v)
    tree[v].append(u)

    union(u, v)

root = find(path[0])
ans = 1
for path_vertex in path:
    if find(path_vertex) != root:
        ans = 0
        break

print(ans)