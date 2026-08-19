def solve():
    from collections import deque
    n = int(input())

    edges = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        s, e, d = map(int, input().split())

        edges[s].append((e, d))
        edges[e].append((s, d))

    start_node = 1

    def bfs(start_node):
        q = deque([start_node])
        distance = [float('inf')] * (n+1)
        distance[start_node] = 0

        while q:
            x = q.popleft()

            for y, next_d in edges[x]:
                if distance[x] + next_d < distance[y]:
                    distance[y] = distance[x] + next_d
                    q.append(y)

        return distance

    distance = bfs(1)
    second_start = distance.index(max(distance[1:]))
    distance = bfs(second_start)
    print(max(distance[1:]))

solve()