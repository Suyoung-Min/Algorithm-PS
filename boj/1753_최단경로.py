import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v,e = map(int,input().split())

graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)

start = int(input())

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijstra(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijstra(start)

for i in range(1,v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
