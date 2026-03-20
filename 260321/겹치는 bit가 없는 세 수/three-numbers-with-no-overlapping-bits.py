n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

max_sum = 0

def generate_combinations_and_sum(tarr, r):
    
    
    def backtracking(current, start):
        global max_sum
        
        if len(current) == r:
            
            a, b, c = current
            
            if not ((a&b) or (b&c) or (c&a)): # 겹치는 게 없다면
                max_sum = max(max_sum, a+b+c)
            
            return
        
        for i in range(start, len(tarr)):
            current.append(tarr[i])
            
            backtracking(current, i+1)
            
            current.pop()
            
    backtracking([], 0)
    
    return max_sum


print(generate_combinations_and_sum(arr, 3))