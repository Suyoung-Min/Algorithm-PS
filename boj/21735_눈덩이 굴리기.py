N , M = map(int,input().split())
dp = list(map(int,input().split()))
dp.insert(0, 0)
ans = [0]*(N+1)

max_snow = 1
def snow(idx, t, prev):
    global max_snow

    if idx + 1 <= N and t <= M:
        max_snow = max([ max_snow, prev + dp[idx+1]])
        snow(idx+1, t+1, prev + dp[idx+1] )  


    if idx+2 <= N and t <= M:
        max_snow = max([ max_snow, prev//2 + dp[idx+2]  ])
        snow(idx+2 , t+1, prev//2 + dp[idx+2])

snow(0,1,1)
print(max_snow)
