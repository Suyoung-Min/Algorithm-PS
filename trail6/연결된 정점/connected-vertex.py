import sys

input = sys.stdin.readline

n, m = map(int, input().split())

operations = []
for _ in range(m):
    op, *nums = input().split()
    if op == "x":
        a, b = map(int, nums)
        operations.append((op, a, b))
    else:
        a = int(nums[0])
        operations.append((op, a))

# Please write your code here.

parent = [i for i in range(n+1)]
size   = [1 for i in range(n+1)]

def find(x):
    if parent[x] != x: # 루트 노드가 아니면 - 부모가 따로 있다면
        parent[x] = find( parent[x] )
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    parent[ max(root_a, root_b) ] = min(root_a, root_b) # 숫자 큰 노드가 자식노드, 숫자 작은 노드가 부모 노드

    if root_a != root_b: # 같은 루트면 같은 구역이니 더하면 안됨
        size[ min(root_a, root_b) ] = size[root_a] + size[root_b] # 크기 합치는 건 루트 노드에 저장

def same(a, b):
    return find(a) == find(b)

def component_size(x):
    return size[find(x)]

for operation in operations:
    if len(operation) == 2: # y a 와 연결된 정점 개수 -> 구역 크기
        a = operation[1]
        print(component_size(a))
    else: # x a,b 연결
        a, b = operation[1:]
        
        if a == b: continue

        union(a, b)

