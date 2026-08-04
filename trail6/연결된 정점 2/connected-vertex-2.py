n = int(input())

parent = [[i, 1] for i in range(100001)] # 1 ~ n
# parent[n][0] 부모 parent[n][1] 소속 넓이

def find(x):
    if x == parent[x][0]: return x
    parent[x][0] = find(parent[x][0])
    return parent[x][0]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b: # 둘이 부모 같으면 == 같은 컴포넌트면
        return

    pnode = min(root_a, root_b)
    cnode = max(root_a, root_b)

    area = parent[pnode][1] + parent[cnode][1]

    parent[ pnode ][1] = area
    parent[ cnode ][1] = area
    parent[ cnode ][0] = pnode

def same(a, b):
    return find(a) == find(b)


for _ in range(n):
    a, b = map(int, input().split())

    union(a, b)

    print(parent[find(a)][1])