n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
nd = {}
ans = 0

for num_i in arr:
    if num_i not in nd:
        nd[num_i] = 1
    else:
        nd[num_i] += 1

nd_items = sorted(nd.items()) 
keys = sorted(nd.keys())
# k:v -> num, total 숫자, 개수
# 정렬을 통해  l <= r 을 보장

for i, a in enumerate(keys):

    count_a = nd[a]
    b = k - a * 2

    if a * 3 == k: # A == A == A
        ans += max(nd[a] * (nd[a] - 1) * (nd[a] - 2) // 6, 0)
    elif b in nd and a < b: # A == A < B
        ans += nd[a] * (nd[a] - 1) // 2 * nd[b]

    for j in range(i+1, len(keys)):

        b = keys[j]
        count_b = nd[b]

        c = k - (a + b)

        if b > c: break

        # A < B == C
        if b == c:
            ans += max(nd[a] * nd[b] * (nd[b] - 1) // 2, 0)
        # A < B < C
        elif c in nd:
            ans += nd[a] * nd[b] * nd[c]

print(ans)