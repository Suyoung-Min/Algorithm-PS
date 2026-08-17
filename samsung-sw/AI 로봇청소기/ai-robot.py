def solve():
    from collections import deque
    def pgrid(grid):
        print('#'*10)
        for row in grid:
            print(' '.join(map(str, row)))
        print('#'*10)

    N, K, L = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(N)]
    r_grid = [[-1]*N for _ in range(N)]
    robots = []

    D = ((-1, 0), (0, -1), (1, 0), (0, 1)) # 상 좌 하 우
    for rid in range(K):
        r, c = map(int, input().split())
        robots.append((r-1, c-1))
        r_grid[r-1][c-1] = rid

    # L 턴 동안 반복
    for _ in range(L):

        # 각 로봇 이동
        for rid in range(K):
            ry, rx = robots[rid]
            q = deque([(ry, rx, 0)])
            visited = [[False]*N for _ in range(N)]
            visited[ry][rx] = True

            min_dist = float('inf')
            result = []

            while q:
                y, x, dist = q.popleft()

                if dist > min_dist: continue

                if 1 <= grid[y][x]: # 먼지에 도착했으면

                    if dist <= min_dist:
                        min_dist = dist
                        result.append((y, x))

                    continue

                for dy, dx in D:
                    ny = y + dy
                    nx = x + dx

                    # 맵 밖이면
                    if ny < 0 or ny >= N or nx < 0 or nx >= N: continue
                    # 물건이 있거나 로봇이 있다면
                    if grid[ny][nx] == -1 or r_grid[ny][nx] >= 0: continue
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        q.append((ny, nx, dist + 1))

            result.sort()

            if result:
                nry, nrx = result[0]
                r_grid[ry][rx] = -1
                r_grid[nry][nrx] = rid
                robots[rid] = (nry, nrx)

        # 2. 각 로봇 청소
        for rid in range(K):
            ry, rx = robots[rid]

            max_d = -1
            max_dust = -1

            for i in range(4):
                dust_sum = 0
                
                for d in [i, (i+1) % 4, (i-1) % 4]:
                    ny = ry + D[d][0]
                    nx = rx + D[d][1]
                    
                    # 맵 안이고, 먼지이고, 청소기가 아닐 때
                    if 0 <= nx < N and 0 <= ny < N and 1 <= grid[ny][nx]:
                        # 한번에 먼지 청소 20까지만
                        dust_sum += min(grid[ny][nx], 20)

                if dust_sum >= max_dust:
                    max_dust = dust_sum
                    max_d = i

            # 최대 먼지 청소가능한 방향 정했으니 청소한다


            grid[ry][rx] = max(0, grid[ry][rx] - 20)
            for d in [max_d, (max_d+1) % 4, (max_d-1) % 4]:
                ny = ry + D[d][0]
                nx = rx + D[d][1]

                if 0 <= nx < N and 0 <= ny < N and 1 <= grid[ny][nx]:
                    # 한번에 먼지 청소 20까지만
                    grid[ny][nx] = max(0, grid[ny][nx] - 20)


        # 먼지 축적

        for y in range(N):
            for x in range(N):
                if 1 <= grid[y][x]:
                    grid[y][x] += 5

        # 먼지 확산

        get_dirty = []

        for y in range(N):
            for x in range(N):
                # 깨끗한 격자면
                if grid[y][x] == 0:
                    dust_sum = 0
                    for dy, dx in D:
                        ny = y + dy
                        nx = x + dx

                        # 맵 안에 있는 먼지면
                        if 0 <= ny < N and 0 <= nx < N and 1 <= grid[ny][nx]:
                            dust_sum += grid[ny][nx]
                    get_dirty.append((y, x, dust_sum))

        for y, x, dust_sum in get_dirty:
            grid[y][x] = dust_sum//10


        # 먼지 출력
        dust_sum = 0
        for y in range(N):
            for x in range(N):
                if 1 <= grid[y][x]:
                    dust_sum += grid[y][x]

        print(dust_sum)

solve()