import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

g = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    if g[a][b] > c:
        g[a][b]=c

for m in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            if g[s][e] > g[s][m] + g[m][e]:
                g[s][e] = g[s][m] + g[m][e]

for i in range(1,n+1):
    g[i][i] = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        if g[i][j] == INF:
            g[i][j] = 0

        print(g[i][j],end=' ')
    print()
