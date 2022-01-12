n = int(input())
A = list(map(int,input().split()))
dp1 = [1]*n
dp2 = [1]*n

for i in range(1,n):
    for j in range(i):
        if A[j] < A[i] and dp1[j]+1 > dp1[i]:
            dp1[i] = dp1[j]+1

for i in range(n-2,-1,-1):
    for j in range(n-1,i,-1):
        if A[j] < A[i] and dp2[j]+1 > dp2[i]:
            dp2[i] = dp2[j]+1

dp = [dp1[i]+dp2[i]-1 for i in range(n)]
print(max(dp))
