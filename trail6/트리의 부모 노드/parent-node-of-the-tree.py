def solve():
    n = int(input())

    # 인접 리스트 -> 처음엔 방향 없이

    edges = [[] for _ in range(n+1)]
    parent = [0] * (n + 1)
    parent[1] = 1 # 루트 노드의 부모는 자기자신

    for _ in range(n - 1):
        s, e = map(int, input().split())
        edges[s].append(e)
        edges[e].append(s)


    def dfs(x):

        for y in edges[x]:
            if not parent[y]:
                parent[y] = x
                dfs(y)

    dfs(1)

    for i in range(2, n+1):
        print(parent[i])



solve()