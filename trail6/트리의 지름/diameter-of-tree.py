import sys

sys.setrecursionlimit(10**6)

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.

# 2. 노드가 1개일 경우 지름은 0이므로 바로 종료합니다.
if n == 1:
    print(0)
    sys.exit()

tree = [[] for _ in range(n+1)]
parent = [0] * (n + 1)
dist = [0] * (n + 1)

for u, v, e in edges:
    tree[u].append((e, v))
    tree[v].append((e, u))

def dfs(node):
    for distance, child in tree[node]:
        if parent[child] == 0: # 아직 방문안한 노드라면
            parent[child] = node
            dist[child] = dist[node] + distance
            dfs(child)


parent[1] = 1 # 시작점이니 부모는 없다 -> 자기자신
dfs(1)#

st_pos = dist.index(max(dist)) 
# 1. 거리가 최댓값인 노드를 시작점으로 
# 2. 시작점에서 다시 거리가 최대인 점과의 거리 계산

# tree 는 그대로, parent, dist 다시 초기화
parent = [0] * (n + 1)
dist = [0] * (n + 1)

parent[st_pos] = st_pos # 자기자신을 부모로 초기화
dfs(st_pos)

print(max(dist)) # 이후 최댓값이 트리의 지름