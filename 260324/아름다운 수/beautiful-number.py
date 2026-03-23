n = int(input())

ans = 0

def dfs(num_length):
    global ans
    
    if num_length == n:
        ans += 1
        return
    
    
    for i in range(1,5): # 1~4
        if num_length + i > n: continue
        dfs(num_length + i)
    
dfs(0)
print(ans)