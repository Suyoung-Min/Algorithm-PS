def solve():
    n, m, k = map(int, input().split())
    edges = [[] for _ in range(n + 1)] # 1 ~ n
    visit = [False] * (n + 1)

    weight_sum = 0

    for _ in range(m):
        s, e, w = map(int, input().split())
        edges[s].append((w, e))
        edges[e].append((w, s))


    import heapq

    heap = [(0, 1)] # (weight, node)

    while heap:
        w, x = heapq.heappop(heap)

        if visit[x]: continue
        visit[x] = True
        weight_sum += w

        for next_w, y in edges[x]:
            heapq.heappush(heap, (next_w, y))

    weight_sum += ((n - 1) * (n - 2) // 2) * k

    print(weight_sum)

solve()
