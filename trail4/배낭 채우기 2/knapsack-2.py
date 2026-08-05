n, m = map(int, input().split())

jewel = [tuple(map(int, input().split())) for _ in range(n)] # w v

# 순서 무시, 무제한
# jewel 바깥쪽, 오름차순

# dp[x] 배낭 무게가 x 일 때 최대 가치
dp = [0] * (m+1)

for w, v in jewel:
    for x in range(w, m+1):
        dp[x] = max(dp[x], dp[x - w] + v)
            
print(max(dp))