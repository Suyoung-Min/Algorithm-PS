n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def generate_combinations(tarr, r):
    result = []
    
    def backtracking(current, start):
        
        if len(current) == r:
            result.append(current[:])
            return
        
        for i in range(start, len(tarr)):
            current.append(tarr[i])
            
            backtracking(current, i+1)
            
            current.pop()
            
    backtracking([], 0)
    
    return result

carr = generate_combinations(arr, 3)

max_sum = 0

for targets in carr:
    a, b, c = targets
    
    if a&b or b&c or c&a: # 겹치는 게 있으면
        continue
    
    max_sum = max(max_sum, a+b+c)
    
print(max_sum)