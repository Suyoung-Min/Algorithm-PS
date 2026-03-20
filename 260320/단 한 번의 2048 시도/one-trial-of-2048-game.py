grid = [list(map(int, input().split())) for _ in range(4)]

dir = input()

dir_to_rotate = {
    'L': 3,
    'R': 1,
    'U': 2,
    'D': 0
}

def rotate_grid_cw():
    ng = [[0]*4 for _ in range(4)]
    
    for y in range(4):
        for x in range(4):
            ng[y][x] = grid[4-x-1][y]
            
    for y in range(4):
        for x in range(4):
            grid[y][x] = ng[y][x]
            
            
for _ in range(dir_to_rotate[dir]):
    rotate_grid_cw()
    
for x in range(4):
    
    tmp = [0]*4
    tidx = 3
    num = -1 # -1 은 비어있는 것
    
    for y in range(3, -1, -1):
        if grid[y][x] == 0: continue
        
        if num == -1: # num 비엇을 때
            num = grid[y][x]
            continue
        elif grid[y][x] == num: # num 과 같을 때
            tmp[tidx] = num*2
            tidx -= 1
            num = -1
        else: # num 과 다를 때
            tmp[tidx] = num
            tidx -= 1
            num = grid[y][x]
            
    if num != -1: # num 이 남아있으면
        tmp[tidx] = num
            
    for y in range(4):
        grid[y][x] = tmp[y]
    
    
for _ in range(4 - dir_to_rotate[dir]):
    rotate_grid_cw()
    
for line in grid:
    print(*line)