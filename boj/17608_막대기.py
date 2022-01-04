n = int(input())
h = [int(input()) for i in range(n)]

t = h[n-1]
ans = 1
for i in range(n-2,-1,-1):
    if h[i] > t:
        ans+=1
        t = h[i]

print(ans)
