n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

x_visited = [False] * n

ans = 0

def backtrack(sy, min_num):
    global ans
    # 종료 조건 
    # 1. 카운트 n개 일 때
    # 2. min_num 이 ans 보다 작을 때
    
    if min_num <= ans:
        return
    
    if sy == n:
        ans = max(ans, min_num)
        return
    
    for x in range(n):
        if not x_visited[x]:
            
            x_visited[x] = True
            
            backtrack(sy+1, min(min_num, A[sy][x]))
            
            x_visited[x] = False
    
backtrack(0, float('inf'))
print(ans)