n = int(input())
a = list(map(int,input().split(' ')))
dp = [1]*(n)
for i in range(n):
    for j in range(i):
        if a[j]<a[i] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1
print(max(dp))
