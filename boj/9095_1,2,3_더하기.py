t = int(input())

for case in range(t):
    n = int(input())
    
    dp = [0]*(n+3)
    dp[1]=1
    dp[2]=2
    dp[3]=4
    
    for i in range(4,n+1):
        dp[i]= dp[i-3]+dp[i-2]+dp[i-1]
        
    print(dp[n])
