n,k = map(int,input().split())

C = [[1] + [0]*1000 for _ in range(1001)]
for i in range(n+1):
    C[i][i] = 1
C[2][1] = 2

for i in range(3,n+1):
    for j in range(1,n):
        C[i][j] = (C[i-1][j-1] + C[i-1][j])%10007
print(C[n][k])
