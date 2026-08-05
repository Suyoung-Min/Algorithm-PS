n = int(input())

stick = [0] + list(map(int, input().split()))

# dp[x] 길이를 x 까지 쓸 때 최대 이익
dp = [0] * (n + 1)

for s in range(1, n+1): # 사용할 길이
    for i in range(s, n+1):
        # if dp[i - s] != -1: 길이 1도 있으니 항상 갱신됨
        dp[i] = max(dp[i], dp[i - s] + stick[s])
            
print(dp[n])