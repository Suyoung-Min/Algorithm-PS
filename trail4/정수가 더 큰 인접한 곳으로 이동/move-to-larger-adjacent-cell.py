def solve():
    
    D = ((-1, 0), (1, 0), (0, -1), (0, 1)) # 상 하 좌 우

    n, r, c = map(int, input().split())
    r -= 1
    c -= 1
    grid = [list(map(int, input().split())) for _ in range(n)]
    result = []
    while True:
        result.append(grid[r][c])

        next_d = -1
        for d in range(4):
            nr = r + D[d][0]
            nc = c + D[d][1]

            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] > grid[r][c]:
                    next_d = d
                    break

        if next_d == -1: break

        r += D[next_d][0]
        c += D[next_d][1]

    print(" ".join(map(str, result)))

solve()