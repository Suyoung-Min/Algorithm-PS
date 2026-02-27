NONE = -1

n = 4

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

ng = [
    [0]*n
    for _ in range(n)
]

def rotate(): # 시계방향
    for y in range(n):
        for x in range(n):
            ng[y][x] = 0
    
    for y in range(n):
        for x in range(n):
            ng[y][x] = grid[n-x-1][y]
            
    for y in range(n):
        for x in range(n):
            grid[y][x] = ng[y][x]
            
            
def drop(): # D 기준
    for y in range(n):
        for x in range(n):
            ng[y][x] = 0
            
            
    for x in range(n):
        keep_num = -1
        next_row = n-1
        
        for y in range(n-1, -1, -1):
            
            if grid[y][x] == 0:
                continue
            
            if keep_num == -1:
                keep_num = grid[y][x]
            elif keep_num == grid[y][x]:
                ng[next_row][x] = keep_num * 2
                next_row -= 1
                keep_num = -1
            else:
                ng[next_row][x] = keep_num
                next_row -= 1
                keep_num = grid[y][x]
                
                
        if keep_num != -1:
            ng[next_row][x] = keep_num
            
    for y in range(n):
        for x in range(n):
            grid[y][x] = ng[y][x]
            
                
                
        

def tilt(move_dir):
    for _ in range(move_dir):
        rotate()
        
    drop()
    
    for _ in range(4 - move_dir):
        rotate()
    
dir_char = input()

dir_mapper = {
    'D': 0,
    'R': 1,
    'U': 2,
    'L': 3
}

tilt(dir_mapper[dir_char])

for line in grid:
    print(*line)