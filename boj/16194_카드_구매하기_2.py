n = int(input())

p = list(map(int,input().split(' ')))
p.insert(0,0)

dp = [float('inf')]*(n+2)
dp[0]=0
dp[1]=p[1]

for i in range(2,n+1):
    for k in range(i):
        dp[i] = min([ dp[k]+p[i-k] , dp[i] ])
    
print(dp[n])
