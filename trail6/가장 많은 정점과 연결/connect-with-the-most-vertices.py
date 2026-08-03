n, m, k = map(int, input().split())

costs = [0] + list(map(int, input().split()))

edges = [tuple(map(int, input().split())) for _ in range(m)]

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


for s, e in edges:
    union(s, e)

for i in range(1, n+1): find(i)

from collections import defaultdict

part_count = defaultdict(list)

for i in range(1, n+1):
    part_count[parent[i]].append(costs[i])

part_least_costs = sorted([min(parts) for parts in list(part_count.values())])

if len(part_least_costs) == 1: print(0)

ans = min(part_least_costs) * (len(part_least_costs) - 1) + sum(part_least_costs[1:])

print(ans if ans <= k else 'NO')