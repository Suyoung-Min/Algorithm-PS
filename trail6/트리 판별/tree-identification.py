def solve():
    m = int(input())

    edges = dict()
    indegree = dict()

    for _ in range(m):
        s, e = map(int, input().split())

        if s not in edges: edges[s] = []
        edges[s].append(e)

        if s not in indegree: indegree[s] = 0

        if e not in indegree: indegree[e] = 1
        else: indegree[e] += 1

    root = 0
    for k in indegree:
        if indegree[k] == 0:
            if root == 0: 
                root = k
            else:
                root = 0
                break
                
    # 루트가 없거나 중복이면
    if root == 0:
        print(0)
        return

    visited = {k: 0 for k in indegree}
    visited[root] = 1

    def dfs(node):
        if node in edges:
            for next_node in edges[node]:
                if visited[next_node] < 2:
                    visited[next_node] += 1
                    dfs(next_node)


    dfs(root)

    if 2 in visited.values() or 0 in visited.values() :print(0)
    else: print(1)

solve()