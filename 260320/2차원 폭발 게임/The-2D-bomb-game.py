n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def bomb(): # 같은 숫자 M 개 이상이면 터뜨리기만
    
    for x in range(n):
        
        last_y = 0
        si = -1 # start_index
        for y in range(n-1, -1, -1):
            #breakpoint()
            
            if grid[y][x] == 0: 
                last_y = y+1
                break
            
            if si == -1:
                si = y
            elif grid[y][x] != grid[si][x]:
                
                if si - y >= m:
                    for i in range(y+1, si+1):
                        grid[i][x] = 0
                        
                si = y

        if si - last_y + 1 >= m: # 마지막 남은 si 가 m 이상일 때
            for i in range(si+1):
                grid[i][x] = 0
                

def gravity_fall():
    ng = [0]*n
    
    for x in range(n):
        ng = [0]*n
        next_row = n-1
        
        for y in range(n-1, -1, -1):
            if grid[y][x]:
                ng[next_row] = grid[y][x]
                next_row -= 1
        
        for y in range(n):
            grid[y][x] = ng[y]

def rotate_cw():
    ng = [[0]*n 
          for _ in range(n)]
    
    for y in range(n):
        for x in range(n):
            ng[y][x] = grid[n-x-1][y]
            
    for y in range(n):
        for x in range(n):
            grid[y][x] = ng[y][x]
            
for _ in range(k):
    bomb()
    gravity_fall()
    rotate_cw()
    gravity_fall()
    
bomb()

bombs_num = 0
for y in range(n):
    for x in range(n):
        if grid[y][x]:
            bombs_num += 1
print(bombs_num)