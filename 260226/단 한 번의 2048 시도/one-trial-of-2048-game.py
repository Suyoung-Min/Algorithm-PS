# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

# Please write your code here.
if dir == "U":
    for x in range(4):
        tarr = [0]*4
        tidx = 0
        cur = 1
        prev = 0
        
        while cur < 4 and cur > prev:
            
            #breakpoint()
            
            if grid[cur][x] == 0:
                cur += 1
                continue
            elif grid[prev][x] == 0:
                prev = cur
                cur += 1
                continue
                
            if grid[cur][x] == grid[prev][x]:
                tarr[tidx] = grid[cur][x] + grid[prev][x]
                tidx += 1
            
                prev = cur+1
                cur += 2
                
            else:
                
                tarr[tidx] = grid[prev][x]
                prev = cur
                tidx += 1
                cur += 1
                
        if prev < 4:
            tarr[tidx] = grid[prev][x]
                
        for y in range(4):
            grid[y][x] = tarr[y]

elif dir == "D":
    for x in range(4):
        tarr = [0]*4
        tidx = 3
        cur = 2
        prev = 3
        
        while cur >= 0:
            
            #breakpoint()
            
            if grid[cur][x] == 0:
                cur -= 1
                continue
            elif grid[prev][x] == 0:
                prev = cur
                cur -= 1
                continue
                
            if grid[cur][x] == grid[prev][x]:
                tarr[tidx] = grid[cur][x] + grid[prev][x]
                tidx -= 1
            
                prev = cur-1
                cur -= 2
                
            else:
                
                tarr[tidx] = grid[prev][x]
                prev = cur
                tidx -= 1
                cur -= 1
                
        if prev >= 0:
            tarr[tidx] = grid[prev][x]
                
        for y in range(4):
            grid[y][x] = tarr[y]
           
           
elif dir == "L":
    for y in range(4):
        tarr = [0]*4
        tidx = 0
        cur = 1
        prev = 0
        
        while cur < 4:
            
            #breakpoint()
            
            if grid[y][cur] == 0:
                cur += 1
                continue
            elif grid[y][prev] == 0:
                prev = cur
                cur += 1
                continue
                
            if grid[y][cur] == grid[y][prev]:
                tarr[tidx] = grid[y][cur] + grid[y][prev]
                tidx += 1
            
                prev = cur+1
                cur += 2
                
            else:
                
                tarr[tidx] = grid[y][prev]
                prev = cur
                tidx += 1
                cur += 1
                
        if prev < 4:
            tarr[tidx] = grid[y][prev]
                
        for x in range(4):
            grid[y][x] = tarr[x]     
        
elif dir == "R":
    for y in range(4):
        tarr = [0]*4
        tidx = 3
        cur = 2
        prev = 3
        
        while cur >= 0:
            
            #breakpoint()
            
            if grid[y][cur] == 0:
                cur -= 1
                continue
            elif grid[y][prev] == 0:
                prev = cur
                cur -= 1
                continue
                
            if grid[y][cur] == grid[y][prev]:
                tarr[tidx] = grid[y][cur] + grid[y][prev]
                tidx -= 1
            
                prev = cur-1
                cur -= 2
                
            else:
                
                tarr[tidx] = grid[y][prev]
                prev = cur
                tidx -= 1
                cur -= 1
                
        if prev >= 0:
            tarr[tidx] = grid[y][prev]
                
        for x in range(4):
            grid[y][x] = tarr[x]
        
for line in grid:
    print(*line)