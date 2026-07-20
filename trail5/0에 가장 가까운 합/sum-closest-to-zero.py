n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
ans = int(1e9)

a.sort()
l, r = 0, n-1
ans = int(1e10)
while l < r:
    lr_sum = a[l] + a[r]
    
    ans = min(ans, abs(lr_sum))

    if lr_sum == 0:
        break
    elif lr_sum > 0:
        r -= 1
    else:
        l += 1

print(ans)