def solve():
    n, m = map(int, input().split())

    grid = [[0] * (n + 1) for _ in range(n + 1)] # 1 ~ n
    block = {}

    def object_gravity(bid):

        by, bx, h, w = block[bid]

        next = by + h

        while next <= n:
            flag = True

            for x in range(bx, bx + w):
                if grid[next][x] != 0: # 다른 블록이랑 겹치면
                    flag = False
                    break

            if not flag: break

            next += 1

        for y in range(by, by + h):
            for x in range(bx, bx + w):
                grid[y][x] = 0

        new_y = next - h

        for y in range(new_y, new_y + h):
            for x in range(bx, bx + w):
                grid[y][x] = bid

        block[bid][0] = new_y

    def possible_left_out(bid):

        by, bx, h, w = block[bid]

        for y in range(by, by + h):
            for x in range(1, bx):
                if grid[y][x] != 0: return False

        return True

    def possible_right_out(bid):

        by, bx, h, w = block[bid]

        for y in range(by, by + h):
            for x in range(bx + w, n + 1):
                if grid[y][x] != 0: return False

        return True

    def _pg(grid):
        print('#'*10)
        for row in grid:
            print(row)


    for _ in range(m):
        k, h, w, c = map(int, input().split())

        block[k] = [1, c, h, w] # y, x, h, w
        object_gravity(k)

    result = []

    while block: # 블록이 남아있을 때
        #1. 왼쪽으로 k 작은 택배 -> k 찾기

        min_k = None

        for bid in sorted(block.keys()):
            if possible_left_out(bid):
                min_k = bid
                break
                    
        # min_k 빼기

        result.append(min_k)
        my, mx, mh, mw = block.pop(min_k)

        for y in range(my, my + mh):
            for x in range(mx, mx + mw):
                grid[y][x] = 0

        # 블록 다 제거됐으면
        if not block: break
        #2. 하나 뺀 중력 처리

        visit = set()
        to_gravity_bids = []
        for y in range(my - 1, 0, -1):
            for x in range(1, n + 1):
                tmp_bid = grid[y][x]
                if tmp_bid != 0 and tmp_bid not in visit:
                    visit.add(tmp_bid)
                    to_gravity_bids.append(tmp_bid)

        for bid in to_gravity_bids:
            object_gravity(bid)

        #3. 오른쪽으로 k 작은 택배

        min_k = None

        for bid in sorted(block.keys()):
            if possible_right_out(bid):
                min_k = bid
                break

        # min_k 빼기

        result.append(min_k)
        my, mx, mh, mw = block.pop(min_k)

        for y in range(my, my + mh):
            for x in range(mx, mx + mw):
                grid[y][x] = 0

        # 블록 다 제거됐으면
        if not block: break
        # 4. 하나 뺀 중력 처리

        visit = set()
        to_gravity_bids = []
        for y in range(my - 1, 0, -1):
            for x in range(1, n + 1):
                tmp_bid = grid[y][x]
                if tmp_bid != 0 and tmp_bid not in visit:
                    visit.add(tmp_bid)
                    to_gravity_bids.append(tmp_bid)

        for bid in to_gravity_bids:
            object_gravity(bid)


    for bid in result:
        print(bid)

solve()