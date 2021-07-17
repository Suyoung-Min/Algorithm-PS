n,k = map(int,input().split(' '))
a = [0]*(n)
for i in range(n):
    a[i] = int(input())
ans = 0
for i in reversed(a):
    ans += k//i
    k %= i
print(ans)
