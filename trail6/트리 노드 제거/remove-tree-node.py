def solve():
    from collections import deque
    n = int(input())

    parent = list(map(int, input().split()))
    erase_node = int(input())
    edges = [[] for _ in range(n)] # 0 ~ n-1 단방향 엣지

    root = None
    for i in range(len(parent)):
        if parent[i] == -1:
            root = i
            continue
        if i == erase_node or parent[i] == erase_node: continue

        edges[parent[i]].append(i)

    leaf_num = 0
    def dfs(node):
        nonlocal leaf_num

        if len(edges[node]) == 0 and node != root:
            leaf_num += 1
            return

        for next_node in edges[node]:
            dfs(next_node)

    dfs(root)

    print(leaf_num)

solve()