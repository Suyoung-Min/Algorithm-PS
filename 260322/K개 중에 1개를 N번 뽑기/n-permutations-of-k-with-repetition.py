def generate_permutations(arr, n):
    result = []
    
    def backtracking(current, start):
        
        if len(current) == n:
            result.append(current[:])
            return
        
        for i in range(len(arr)):
        
            current.append(arr[i])
            
            backtracking(current, i+1)
            
            current.pop()
            
            
    backtracking([], 0)
    
    return result

k, n = map(int, input().split())

result = generate_permutations([i for i in range(1, k+1)], n)

for line in result:
    print(*line)