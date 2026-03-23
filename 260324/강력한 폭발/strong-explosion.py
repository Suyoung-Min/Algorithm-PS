n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def solve():
    
    visited = [[0]*n for _ in range(n)]
    
    bomb_areas = [[(0, 0),(-2, 0), (-1, 0), (1, 0), (2, 0)], # 1
                 [(0, 0),(-1, 0), (0, 1), (0, -1), (1, 0)], # 2
                 [(0, 0),(-1, -1), (-1, 1), (1, -1), (1, 1)]] # 3
    
    ans = 0
    
    bomb_candidates = []
    
    for y in range(n):
        for x in range(n):
            if grid[y][x] == 1: # 폭탄 후보 자리이면
                bomb_candidates.append((y,x))
                
                
    def backtracking(idx, current_bomb):
        nonlocal ans
        
        if idx == len(bomb_candidates):
            ans = max(ans, current_bomb)
            return
        
        y, x = bomb_candidates[idx]
        
        for i in range(3):
            
            bomb_tracking = []
            
            for by, bx in bomb_areas[i]:
                ty, tx = y + by, x + bx
                
                if ty < 0 or ty >= n or tx < 0 or tx >= n: continue
                
                if visited[ty][tx] == 0:
                    #아직 안 터진 곳이면
                    visited[ty][tx] = 1 # 터트리기
                    bomb_tracking.append((ty,tx)) # 터트린 곳 임시저장
                    
            # 다음 폭탄 후보 위치 탐색        
            backtracking(idx + 1, current_bomb + len(bomb_tracking)) 
            
            
            for ry, rx in bomb_tracking:
                visited[ry][rx] = 0 # 복구하기
                
                
    backtracking(0, 0)
    
    return ans
            
print(solve())