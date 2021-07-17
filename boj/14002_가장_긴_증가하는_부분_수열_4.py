n = int(input())
a = list(map(int,input().split(' ')))
dp = [1]*(n)
idx = [-1]*(n)
for i in range(n):
    for j in range(i):
        if a[j]<a[i] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1
            idx[i]=j
print(max(dp))
ans = []
s = idx[dp.index(max(dp))]
ans.append(a[dp.index(max(dp))])
while True:
    if s == -1:
        break
    ans.append(a[s])
    s=idx[s]
ans.reverse()
for i in ans:
    print(i,end=' ')
