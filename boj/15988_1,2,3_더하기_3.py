t = int(input())

dp = [0]*(1000001)

dp[1]=1
dp[2]=2
dp[3]=4

max = 3

for case in range(t):
    n = int(input())
    
    if n <= max:
        print(dp[n])
    else:
        for i in range(max+1,n+1):
            dp[i] = (dp[i-1] + dp[i-2]+dp[i-3])%1000000009
        max = n
        print(dp[n])
