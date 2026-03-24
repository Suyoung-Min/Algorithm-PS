n = int(input())
arr = list(map(int, input().split()))

all_sum = sum(arr)

ans = float('inf')

def backtracking(csum, idx, count): # 합, arr 탐색 인덱스, 현재 수열 길이
    
    global ans
    
    # 종료 조건 -> n 개 뽑았을 때, ans 보다 클 때, 인덱스 마지막일 때
    
    if count == n:
        
        ans = min(ans, abs((all_sum - csum) - csum))
        
        return
    
    if idx == 2*n:
        return
    
    # 두 가지 경우 - 해당 숫자를 수열에 포함시킬때, 아닐 때
    
    # 1. 포함
    backtracking(
        csum + arr[idx],
        idx + 1,
        count + 1
    )
    
    # 2. 미포함
    backtracking(
        csum,
        idx + 1,
        count
    )
    
backtracking(0, 0, 0)

print(ans)