n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

# Please write your code here.

a_set = set(a)
for elem_b in b:
    print(0 if elem_b not in a_set else 1)