n=int(input())
arr = [int(input()) for _ in range(n)]

ans = 0
idx = n-1
for i in range(n-2,-1,-1):
    if arr[i] >= arr[idx]:
        ans += arr[i] - arr[idx] +1
        arr[i] = arr[idx] -1
    idx -= 1
print(ans)
