n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 2)]

# Please write your code here.

parent = [i for i in range(n+1)] # 1~n


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

for s, e in edges:
    union(s, e)
    
roots = sorted({find(i) for i in range(1, n+1)})
print(roots[0], roots[1])