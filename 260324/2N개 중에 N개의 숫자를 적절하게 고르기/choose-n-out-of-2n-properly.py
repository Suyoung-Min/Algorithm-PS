n = int(input())
arr = list(map(int, input().split()))
all_sum = sum(arr)
ans = float('inf')
def backtracking(csum, idx, count): # 합, arr 탐색 인덱스, 현재 수열 길이
    global ans
    
    if count == n:
        ans = min(ans, abs((all_sum - csum) - csum))
        return
    
    if idx == 2*n:
        return
    
    backtracking(
        csum + arr[idx],
        idx + 1,
        count + 1
    )
    
    backtracking(
        csum,
        idx + 1,
        count
    )
    
backtracking(0, 0, 0)

print(ans)