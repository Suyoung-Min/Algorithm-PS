def solve():
    N, M, K = map(int, input().split())
    K -= 1

    grid= [list(map(int, input().split())) for _ in range(N)]

    y = 0
    while y < N-1:

        can_install = False

        for x in range(K, K+M):
            if grid[y+1][x]:
                can_install = True
                break

        if can_install:
            for x in range(K, K + M):
                grid[y][x] = 1
            break

        y += 1

    if y == N-1:
        for x in range(K, K + M):
            grid[y][x] = 1

    for row in grid:
        print(' '.join(map(str, row)))



solve()