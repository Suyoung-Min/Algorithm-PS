n = int(input())
visited = [False] * (n+1)

def backtracking(current):
    
    if len(current) == n:
        print(*current)
        return
    
    for i in range(n, 0, -1):
        if not visited[i]:
            visited[i] = True
            current.append(i)
            
            backtracking(current)
            
            current.pop()
            visited[i] = False
            
backtracking([])