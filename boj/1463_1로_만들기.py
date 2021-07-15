n = int(input())
    
dp = [0]*(n+3)
dp[2]=1
dp[3]=1
    
for i in range(4,n+1):
    if i%6 == 0:
        dp[i] = min([dp[i-1],dp[int(i/2)],dp[int(i/3)]])+1
    elif i%3 == 0:
        dp[i] = min([dp[i-1],dp[int(i/3)]])+1
    elif i%2 == 0:
        dp[i] = min([dp[i-1],dp[int(i/2)]])+1
    else:
        dp[i]=dp[i-1]+1
        
print(dp[n])
