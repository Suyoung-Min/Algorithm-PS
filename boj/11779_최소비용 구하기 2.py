import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

g = [[] for _ in range(n+1)]
distance = [[INF,-1] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())

    g[a].append((b,c)) #dest, cost

s,d = map(int,input().split())

q = []
distance[s][0]=0
heapq.heappush(q,(0,s))

while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now][0]: continue

    for i in g[now]:
        cost = dist + i[1]
        if cost < distance[i[0]][0]:
            distance[i[0]][0] = cost
            distance[i[0]][1] = now
            heapq.heappush(q,(cost,i[0]))

city = []
def recur(pos):
    global city
    city.append(pos)
    if pos == s: return
    
    recur(distance[pos][1])

recur(d)

print(distance[d][0])
print(len(city))
for i in city[::-1]:
    print(i,end=' ')
