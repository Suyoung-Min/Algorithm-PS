n=int(input())
dp=[i for i in range(n+1)]
for i in range(4,n+1):
    j=1
    while j*j<=i:
        if dp[i-j*j]+1<dp[i]:
            dp[i]=dp[i-j*j]+1
        j+=1
print(dp[n])

"""
dp[i]=min([dp[i-j*j],dp[i]])는 비교 & 할당
if는 조건이 맞지 않으면 할당 작업 없이 pass
작업량 많을 때 시간차이 있음
"""
