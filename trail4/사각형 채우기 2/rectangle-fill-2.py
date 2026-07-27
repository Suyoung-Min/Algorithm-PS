N = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3
MOD = int(1e4) + 7

def step(num):
    if dp[num]: return dp[num]

    dp[num] = (step(num - 1) + step(num - 2) * 2) % MOD

    return dp[num]


print(step(N))