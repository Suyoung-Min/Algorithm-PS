
def main():
    n, m = map(int, input().split())
    a, b, c = map(int, input().split())
    #edges = [tuple(map(int, input().split())) for _ in range(m)]

    # Please write your code here.
    edges = {}
    visited = {}

    for _ in range(m):
        s, e, d = map(int, input().split())
        
        if s not in edges:
            edges[s] = [(e, d)]
        else:
            edges[s].append((e, d))
            
        if e not in edges:
            edges[e] = [(s, d)]
        else:
            edges[e].append((s, d))
            
        if s not in visited:
            visited[s] = [float('inf')] * 3
        
        if e not in visited:
            visited[e] = [float('inf')] * 3
            
            
    import heapq

    start_point = [a, b, c]
    
    for si in range(3):
        
        q = []
        
        sp = start_point[si] # a, b, c
        
        heapq.heappush(q, (0, sp))
        
        visited[sp][si] = 0
        
        while q:
            dist, cur_v = heapq.heappop(q)
            
            if dist > visited[cur_v][si]: continue
            
            for edge in edges[cur_v]:
                next_v, next_dist = edge
                
                new_dist = dist + next_dist
                
                if new_dist < visited[next_v][si]:
                    visited[next_v][si] = new_dist
                    heapq.heappush(q, (new_dist, next_v))
                    
    for key in visited.keys():
        visited[key] = min(visited[key])
        
        
    ans = max(visited.values())
    print(ans)
        
        

if __name__ == '__main__':
    main()