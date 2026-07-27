N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]

dp[0][N-1] = arr[0][N-1]

def step(y, x):
    if dp[y][x]: return dp[y][x]

    upper_dp = float('inf')
    right_dp  = float('inf')

    if y-1 >= 0: upper_dp = step(y-1, x)

    if x+1 < N: right_dp = step(y, x+1)

    dp[y][x] = arr[y][x] + min(upper_dp, right_dp)

    return dp[y][x]


print(step(N-1, 0))