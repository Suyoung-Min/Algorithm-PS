from bisect import bisect_left, bisect_right

n, m = map(int, input().split())

point = list(map(int, input().split()))

point.sort()

for _ in range(m):
    l, r = map(int, input().split())

    print(bisect_right(point, r) - bisect_left(point, l))