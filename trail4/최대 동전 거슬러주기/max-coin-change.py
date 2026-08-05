n, m = map(int, input().split())

coin = list(map(int, input().split()))

dp = [-1]*(m+1)
dp[0] = 0
MOD = 10007

for c in coin:
    for i in range(m+1):
        if i - c >= 0 and dp[i-c] != -1:
            dp[i] = max(dp[i], dp[i-c] + 1)
            
print(dp[m])