n = int(input())

dp = [0]*(n+1)
dp[0] = 1
MOD = 10007

for i in range(1, n+1):
    dp[i] += dp[i-1]
    
    if i >= 2:
        dp[i] += dp[i-2]
        
    if i >= 5:
        dp[i] += dp[i-5]
        
    dp[i] %= MOD
    
print(dp[n])