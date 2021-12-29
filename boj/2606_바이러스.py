import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
g = [[0]*(n+1) for _ in range(n+1)]
visit = [False]*(n+1)

e = int(input())

for i in range(e):
    a,b = map(int,input().split())
    g[a][b] = g[b][a] = 1

q = deque()
q.append(1)
visit[1] = True
ans = 0

while q:
    pos = q.popleft()

    for i in range(1,n+1):
        if visit[i] == False and g[pos][i] == 1:
            visit[i] = True
            q.append(i)
            ans+=1

print(ans)
