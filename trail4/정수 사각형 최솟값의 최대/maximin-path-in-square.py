N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = arr[0][0]

def step(y, x):
    if dp[y][x]: return dp[y][x]

    upper_dp, left_dp = 0, 0

    if y-1 >= 0:
        upper_dp = step(y-1, x)

    if x-1 >= 0:
        left_dp = step(y, x-1)

    dp[y][x] = min( max(left_dp, upper_dp), arr[y][x] )

    return dp[y][x]


print(step(N-1, N-1))