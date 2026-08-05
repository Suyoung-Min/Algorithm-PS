from bisect import bisect_left, bisect_right

n , m = map(int, input().split())

arr = list(map(int, input().split()))

for _ in range(m):
    tgt = int(input())
    
    print(bisect_right(arr, tgt) - bisect_left(arr, tgt))