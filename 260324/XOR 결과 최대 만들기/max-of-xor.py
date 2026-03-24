N, M = map(int, input().split())

Arr = list(map(int, input().split()))

# Please write your code here.

ans = 0

def generate_xor_comb(arr, m):
    
    def backtracking(current_xor, current_l, start):
        global ans
        
        if current_l == m:
            ans = max(ans, current_xor)
            return
        
        for i in range(start, len(arr)):

            backtracking(current_xor ^ arr[i], current_l+1, i+1)
            
    backtracking(arr[0], 1, 1)
    
generate_xor_comb(Arr, M)
print(ans)            