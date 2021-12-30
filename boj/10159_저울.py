import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

g = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b, = map(int,input().split())
    g[a][b] = 1

for m in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            if g[s][m] and g[m][e]:
                g[s][e] = 1

for t in range(1,n+1):
    ans = 0
    for i in range(1,n+1):
        ans += g[t][i] + g[i][t]
    ans = (n-1) - ans
    print(ans)
