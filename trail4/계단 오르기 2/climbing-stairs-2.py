def solve():
    n = int(input())

    coins = [0] + list(map(int, input().split()))

    dp = [[-float('inf')]*4 for _ in range(n+1)]

    dp[0][0] = 0

    for i in range(1, n+1):
        for j in range(4):

            if j-1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + coins[i])

            if i-2 >= 0:
                dp[i][j] = max(dp[i][j], dp[i-2][j] + coins[i])

    print(max(dp[n]))
solve()