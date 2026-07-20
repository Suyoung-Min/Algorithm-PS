n, m = map(int, input().split())
query = [list(map(int, input().split())) for _ in range(m)]

# Please write your code here.

parent = [i for i in range(n+1)] # 기본 부모는 자기자신

def find(node):
    if parent[node] != node: # 루트노드가 아니면
        parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    parent[ max(root_a, root_b) ] = min(root_a, root_b)

def same(a, b):
    return find(a) == find(b)


for cmd, a, b in query:
    if cmd == 0: # union 이면
        union(a, b)

    elif cmd == 1: # same 이면
        print(int(same(a, b)))