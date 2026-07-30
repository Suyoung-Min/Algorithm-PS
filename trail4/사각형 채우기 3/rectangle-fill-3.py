N = int(input())

# Please write your code here.

dp = [0] * 1001
dp[0] = 1
dp[1] = 2
dp[2] = 7

MOD = 1000000007

def step(num):
    if dp[num]: return dp[num]

    dp[num] = step(num - 1) * 2 + step(num - 2) * 3

    for i in range(num-3, -1, -1):
        dp[num] += step(i) * 2

    dp[num] %= MOD

    return dp[num]

print(step(N))