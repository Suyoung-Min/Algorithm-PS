n, k = map(int, input().split())
arr = list(map(int, input().split()))

nd = {}

for num in arr:
    if num not in nd:
        nd[num] = 1
    else:
        nd[num] += 1

arr = list(set(arr))

ans = 0

visited = set()

for num in arr:
    target = k - num

    if num in visited or target in visited: continue

    visited.update([target, num])

    if target not in nd: continue
    
    if target == num:
        ans += nd[target] * (nd[target] - 1) // 2

    else:
        ans += nd[num] * nd[target]

print(ans)