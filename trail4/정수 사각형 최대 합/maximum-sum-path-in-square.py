N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]

def step(y, x):
    if dp[y][x]: return dp[y][x]

    upper_dp = 0
    left_dp  = 0

    if y-1 >= 0:
        dp[y-1][x] = step(y-1, x)
        upper_dp = dp[y-1][x]

    if x-1 >= 0:
        dp[y][x-1] = step(y, x-1)
        left_dp = dp[y][x-1]


    dp[y][x] = arr[y][x] + max(upper_dp, left_dp)

    return dp[y][x]


print(step(N-1, N-1))