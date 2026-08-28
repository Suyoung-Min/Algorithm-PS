def solve():
    n, m = map(int, input().split())
    edges = [[] for _ in range(n + 1)] # 1 ~ n

    indegree = [0] * (n + 1)

    for _ in range(m):
        s, e = map(int, input().split())

        edges[s].append(e)
        indegree[e] += 1


    import heapq
    heap = []
    for x in range(1, n + 1):
        if not indegree[x]: heap.append(x)

    heapq.heapify(heap)
    result = []

    while heap:
        x = heapq.heappop(heap)

        result.append(x)
        for y in edges[x]:
            indegree[y] -= 1

            if not indegree[y]: heapq.heappush(heap, y)

    print(' '.join(map(str, result)))

solve()

'''
위상정렬
DAG
indegree 0 인 원소들부터 q 에 넣고 시작
'''