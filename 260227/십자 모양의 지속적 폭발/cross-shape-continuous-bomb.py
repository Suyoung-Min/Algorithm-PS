n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input())-1 for _ in range(m)]

# Please write your code here.

def cross_bomb(ty,tx):
    
    t = grid[ty][tx]
    
    for x in range(tx-t+1, tx+t-1+1):
        if x < 0 or x >= n: continue
        
        grid[ty][x] = 0
        
    for y in range(ty-t+1, ty+t-1+1):
        if y < 0 or y >= n: continue
        
        grid[y][tx] = 0
        
def gravity_grid():
    
    for x in range(n):
        ng = [0]*n
        next_row = n-1
        
        for y in range(n-1, -1, -1):
            if grid[y][x]:
                ng[next_row] = grid[y][x]
                next_row -= 1
                
        for y in range(n):
            grid[y][x] = ng[y]
        
def print_grid():
    for line in grid:
        print(*line)

for cmd in commands:
    
    top = -1
    for y in range(n):
        if grid[y][cmd]:
            top = y
            break
        
    if top == -1: continue # 열이 비었으면 다음으로
    
    cross_bomb(top, cmd)
    gravity_grid()
    
    
for line in grid:
    print(*line)