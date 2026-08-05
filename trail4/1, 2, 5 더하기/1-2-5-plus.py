n = int(input())

dp = [0]*(n+1)
dp[0] = 1
MOD = 10007

for i in range(1, n+1):
    for c in (1, 2, 5):
        if i - c >= 0:
            dp[i] += dp[i - c]
            dp[i] %= MOD
    
print(dp[n])