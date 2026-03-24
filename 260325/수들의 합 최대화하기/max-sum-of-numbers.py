n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

row_visited = [False] * n
col_visited = [False] * n

ans = 0

def backtrack(area_sum, count): # 정수합, 정수 개수
    global ans
    
    # 종료 조건 n 개 뽑았을 때
    if count == n:
        ans = max(ans, area_sum)
        return
    
    for y in range(n):
        if row_visited[y]: continue
        for x in range(n):
            if col_visited[x]: continue
            
            row_visited[y] = True
            col_visited[x] = True
            
            backtrack(area_sum + grid[y][x], count+1)
            
            row_visited[y] = False
            col_visited[x] = False
            
            
backtrack(0, 0)

print(ans)