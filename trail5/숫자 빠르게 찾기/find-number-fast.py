from bisect import bisect_left

n , m = map(int, input().split())

arr = list(map(int, input().split()))

for _ in range(m):
    tgt = int(input())
    
    idx = bisect_left(arr, tgt)
    
    if idx >= n: # tgt 가 arr 에 없는 최댓값일 때
        print(-1)
    elif arr[idx] != tgt:
        print(-1)
    else:
        print(idx+1)