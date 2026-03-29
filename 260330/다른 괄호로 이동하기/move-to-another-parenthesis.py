
def main():
    n, a, b = map(int, input().split())
    
    grid = [list(input()) for _ in range(n)]
    
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    visited = [[float('inf')] * n for _ in range(n)]

    
    import heapq

    
    def dijstra(sy, sx):
        nonlocal visited

        for i in range(n):
            for j in range(n):
                visited[i][j] = float('inf')
        
        q = []
        visited[sy][sx] = 0
        heapq.heappush(q, (0, sy, sx))
        
        
        while q:
            dist, y, x = heapq.heappop(q)
            
            
            if dist > visited[y][x]: continue
            
            for dy, dx in dirs:
                ty = y + dy
                tx = x + dx
                
                if ty < 0 or ty >= n or tx < 0 or tx >= n: continue
                
                next_dist = a if grid[y][x] == grid[ty][tx] else b
                
                new_dist = dist + next_dist
                
                if new_dist < visited[ty][tx]:
                    visited[ty][tx] = new_dist
                    heapq.heappush(q, (new_dist, ty, tx))
                    
                    
        return max(map(max, visited))
    
    ans = 0
    
    for i in range(n):
        for j in range(n):
           ans = max(ans, dijstra(i,j)) 
    
    print(ans)
        

if __name__ == '__main__':
    main()