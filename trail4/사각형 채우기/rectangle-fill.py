N = int(input())

# Please write your code here.

dp = [0] * 1001
dp[1] = 1
dp[2] = 2
dp[3] = 3

def step(num):

    if dp[num]: return dp[num]

    dp[num] = (step(num - 1) + step(num - 2)) % 10007

    return dp[num] 

print(step(N))