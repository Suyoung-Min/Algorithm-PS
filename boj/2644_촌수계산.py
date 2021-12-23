from collections import deque

n = int(input())
start,target = map(int,input().split())
m = int(input())

g = [[] for i in range(n+1)]
visit = [False]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

q = deque()
q.append((start,0))
visit[start] = True
ans = -1

while q:
    pos, l = q.popleft()
    
    if pos == target:
        ans = l
        break

    for i in g[pos]:
        if visit[i] == False:
            visit[i]=True
            q.append((i,l+1))

print(ans)
