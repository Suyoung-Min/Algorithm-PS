n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

# Please write your code here.
arr1_set = set(arr1)

for elem2 in arr2:
    if elem2 not in arr1_set:
        print(0, end=' ')
    else:
        print(1, end=' ')