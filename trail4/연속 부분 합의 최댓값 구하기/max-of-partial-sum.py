def solve():
    n = int(input())

    arr = list(map(int, input().split()))
    
    # dp[i] 연속부분수열의 마지막 원소 위치가 i 일 때의 부분수열합의 최댓값
    # dp[i] = max(dp[i-1] + a[i], a[i])

    dp = [0] * n
    dp[0] = arr[0]

    for i in range(1, n):
        dp[i] = max(dp[i - 1] + arr[i], arr[i])

    print(max(dp))

solve()