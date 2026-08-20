def solve():
    from collections import deque
    n = int(input())

    parent = [0] * (n + 1) # 노드 번호 1 ~ n

    edges = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        s, e = map(int, input().split())
        edges[s].append(e)
        parent[e] = s

    a, b = map(int, input().split())

    # Please write your code here.

    '''
    LCA Lowest Common Ancestor 최소 공통 조상
    1. 트리 노드마다 parent, depth 저장해야 함
    2. 타겟 노드의 depth 같아질 때까지 깊은 depth 의 노드를 parent 를 타고 위로 올린다
    3. 같아질 때까지 depth 둘 다 올린다.
    '''
    root = parent[1:].index(0) + 1
    depth = [0] * (n + 1)

    q = deque([(root, 0)])

    while q:
        x, d = q.popleft()

        for child in edges[x]:
            depth[child] = d + 1
            q.append((child, d + 1))

    if depth[a] > depth[b]:
        a, b = b, a

    while depth[a] != depth[b]:
        b = parent[b]

    while a != b:
        a, b = parent[a], parent[b]

    print(a)

solve()
