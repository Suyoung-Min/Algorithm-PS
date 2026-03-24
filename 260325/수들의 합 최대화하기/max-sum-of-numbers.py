n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

x_visited = [False] * n

ans = 0

def backtrack(sy, area_sum, count): # start y, 정수합, 정수 개수 
    global ans
    
    # 종료 조건 n 개 뽑았을 때
    if count == n:
        ans = max(ans, area_sum)
        return
    
    for x in range(n):
        if not x_visited[x]:
        
            x_visited[x] = True
            
            backtrack(sy+1, area_sum + grid[sy][x], count+1)
            
            x_visited[x] = False
            
backtrack(0, 0, 0)

print(ans)