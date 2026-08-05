n = int(input())

stick = [0] + list(map(int, input().split()))

dp = [-1] * (n + 1)
dp[0] = 0

for s in range(1, n+1): # 길이
    for i in range(s, n+1):
        if dp[i - s] != -1:
            dp[i] = max(dp[i], dp[i - s] + stick[s])
            
print(max(dp))