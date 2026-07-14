n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
nd = {}

for num in arr:
    if num not in nd:
        nd[num] = 1
    else:
        nd[num] += 1

nd_arr = sorted([(v, k) for k, v in nd.items()], reverse=True)

for i in range(k):
    print(nd_arr[i][1], end=' ')