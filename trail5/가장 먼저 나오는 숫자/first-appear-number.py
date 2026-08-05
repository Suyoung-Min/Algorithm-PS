from bisect import bisect_left, bisect_right

n, m = map(int, input().split())

arr = list(map(int, input().split()))

query = list(map(int, input().split()))

for x in query:
    idx = bisect_left(arr, x)

    if idx == len(arr):
        print(-1)
        continue

    if x != arr[idx]: 
        print(-1)
    else:
        print(idx+1)