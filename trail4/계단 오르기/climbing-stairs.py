N = int(input())

# Please write your code here.

dp = [0] * 1001
dp[2] = 1
dp[3] = 1

def step(num):

    if num < 0: return 0
    if dp[num]: return dp[num]

    dp[num] = (step(num - 2) + step(num - 3)) % 10007

    return dp[num]

print(step(N))