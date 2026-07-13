n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

dict_arr = {}

for num in arr:
    if num not in dict_arr:
        dict_arr[num] = 1
    else:
        dict_arr[num] += 1

for target in nums:
    if target not in dict_arr: print(0, end=' ')
    else: print(dict_arr[target], end = ' ')