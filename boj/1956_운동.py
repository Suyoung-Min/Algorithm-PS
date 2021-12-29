import sys
from collections import deque
input = sys.stdin.readline

INF = int(1e9)

V,E = map(int,input().split())

g = [[INF]*(V+1) for i in range(V+1)]

for i in range(E):
    a,b,c = map(int,input().split())
    g[a][b] = c

for m in range(1,V+1):
    for s in range(1,V+1):
        for e in range(1,V+1):
            if g[s][e] > g[s][m] + g[m][e]:
                g[s][e] = g[s][m]+g[m][e]

ans = [g[i][i] for i in range(1,V+1)] //i에서 출발, i에 도착 == cycle
ans = min(ans)
if ans == INF:
    ans = -1
print(ans)
