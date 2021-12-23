n = int(input())
d = list(map(int,input().split()))
d.sort()

left = 0
right = sum(d)
ans = int(1e9)
ans_idx = 0
for i in range(n):
    left += d[i]
    right -= d[i]

    tmp = (d[i]*(i+1) - left) + (right - d[i]*(n-i-1))
    if tmp < ans:
        ans = tmp
        ans_idx = i

print(d[ans_idx])
