# 플로이드-워셜 응용

import sys
input = sys.stdin.readline
INF = int(1e9)

def printM(M):
    for line in M:
        print(line)

n,m = map(int,input().split())

g = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    g[a][b] = 1

for m in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            if g[s][m] and g[m][e]:
                g[s][e] = 1

ans = 0
for t in range(1,n+1):

    tmp = 0
    for i in range(1,n+1):
        tmp += g[t][i] + g[i][t]

    if tmp == n-1:
        ans+=1

print(ans)
