def solve():
    from collections import deque

    n, m = map(int, input().split())
    edges = [[] for _ in range(n + 1)] # 1 ~ n
    indegree = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())

        edges[a].append(b)
        indegree[b] += 1

    q = deque([])
    result = []
    for x in range(1, n + 1):
        if not indegree[x]: q.append(x)

    while q:
        x = q.popleft()

        result.append(x)

        for y in edges[x]:
            indegree[y] -= 1

            if not indegree[y]: q.append(y)

    if len(result) != n: print('Inconsistent')
    else: print('Consistent')

solve()