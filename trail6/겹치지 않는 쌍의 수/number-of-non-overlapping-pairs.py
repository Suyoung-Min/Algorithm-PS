n = int(input())
m = []
groups = []

for _ in range(n):
    nums = list(map(int, input().split()))
    m.append(nums[0])
    groups.append(nums[1:])

# Please write your code here.
masks = []
for g in groups:
    mask = 0
    for p in g:
        mask |= (1 << p)
    masks.append(mask)

ans = 0
for i in range(n):
    for j in range(i+1, n):
        ans += int(not bool(masks[i] & masks[j]))

print(ans)