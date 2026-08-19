def solve():
    from collections import deque
    n = int(input())

    edges = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        s, e, d = map(int, input().split())

        edges[s].append((e, d))
        edges[e].append((s, d))

    start_node = 1

    q = deque([1])
    distance = [float('inf')] * (n + 1)
    distance[1] = 0

    while q:
        x = q.popleft()

        for y, next_d in edges[x]:
            if distance[x] + next_d < distance[y]:
                distance[y] = distance[x] + next_d
                q.append(y)

    second_start = distance.index(max(distance[1:]))
    distance = [float('inf')] * (n+1)
    distance[second_start] = 0
    q = deque([second_start])

    while q:
        x = q.popleft()

        for y, next_d in edges[x]:
            if distance[x] + next_d < distance[y]:
                distance[y] = distance[x] + next_d
                q.append(y)

    print(max(distance[1:]))



solve()