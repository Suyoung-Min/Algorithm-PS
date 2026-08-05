n = int(input())

arr = list(map(int, input().split()))

m = sum(arr)//2

dp = [0] * (m+1)
dp[0] = 1

# dp[x] 합이 x 인 부분수열의 존재여부

# 원소 하나씩 / 내림차순
# 순서 없이 -> 조합 / for a in arr 바깥쪽

for a in arr:
    for i in range(m, a-1, -1):
        dp[i] |= dp[i-a]
        
sub_sum = -1

for i in range(m, 0, -1):
    if dp[i]: 
        sub_sum = i
        break
    
print( abs((sum(arr) - sub_sum) - sub_sum) )