n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.

tree = [[] for _ in range(n+1)]

for s, e in edges: # 단방향으로
    tree[s].append(e)
    tree[e].append(s)

parent = [0] * (n + 1) # parent[1] = 0 => 1번 노드의 부모는 없으므로 0으로 초기화

def dfs(node):
    for child in tree[node]:
        if parent[child] == 0: # 아직 방문하지 않은 노드라면
            parent[child] = node # 부모 노드 기록
            dfs(child) # 자식 노드로 이동

dfs(1) # 1번 노드부터 시작하여 DFS 수행

for i in range(2, n + 1):
    print(parent[i]) # 2번 노드부터 n번 노드까지의 부모 노드 출력 