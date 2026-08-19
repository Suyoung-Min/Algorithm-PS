def solve():
    import heapq

    n, m = map(int, input().split())

    edges = [[] for _ in range(n+1)] # 1 ~ n

    for _ in range(n - 1):
        s, e, d = map(int, input().split())

        edges[s].append((e, d))
        edges[e].append((s, d))

    for _ in range(m):
        s, e = map(int, input().split())

        distance = [float('inf')] * (n + 1)
        distance[s] = 0

        heap = [(0, s)]

        while heap:
            dist, x = heapq.heappop(heap)

            if x == e: break

            for next_node, next_d in edges[x]:
                if dist + next_d < distance[next_node]:
                    distance[next_node] = dist + next_d
                    heapq.heappush(heap, (dist + next_d, next_node))

        print(distance[e])

solve()