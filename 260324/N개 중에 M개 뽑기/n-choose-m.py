N, M = map(int, input().split())

# Please write your code here.

# 1 ~ n 에서 m 개를 중복없이 뽑는 조합

def generate_combinations(n, m):
    
    result = []
    
    def backtracking(current, start):
        
        if len(current) == m:
            result.append(current[:])
            return
        
        
        for i in range(start, n+1):
            
            current.append(i)
            
            backtracking(current, i+1)
            
            current.pop()
            
            
    backtracking([], 1)
    
    return result

ans = generate_combinations(N, M)    

for line in ans:
    print(*line)