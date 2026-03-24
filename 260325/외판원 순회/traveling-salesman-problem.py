n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

visited = [False] * n

# 백트래킹 or 다익스트라?
ans = float('inf')

def backtrack(current, count, cost): # 현재 위치, 이동 지점 개수, 방문 비용
    global ans
    
    # 종료 조건
    # 1. count 가 n 이고, current 에서 0(1) 로 가는 경우가 있을 때
    
    if count == n-1: # 마지막에 0으로 돌아가야 하니까 n 이 아니라 n-1
        if grid[current][0]: # visited[0] 은 방문처리 되어 있으니 제외
            ans = min(ans, cost + grid[current][0])
        
        return
    
    for next in range(len(grid[current])):
        if not visited[next]:
            
            visited[next] = True
            
            backtrack(next, count + 1, cost + grid[current][next])
            
            visited[next] = False
    
visited[0] = True # 0에서 시작하니까 방문 표시
backtrack(0, 0, 0)
        
print(ans)