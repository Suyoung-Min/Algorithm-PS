import heapq
import sys
sys.setrecursionlimit(int(1e8))
input = sys.stdin.readline
INF = int(1e9)

while True:
    N,M = map(int,input().split())

    if N == 0 and M == 0: break

    S,D = map(int,input().split())

    g = [[] for _ in range(N)]
    distance = [[INF,[-1]] for _ in range(N)]

    for _ in range(M):
        U,V,P = map(int,input().split())

        g[U].append([P,V]) # (cost,dest)
    
    distance[S][0] = 0
    q = []
    heapq.heappush(q,(0,S))

    while q:
        dist,now = heapq.heappop(q)

        if dist > distance[now][0]: continue

        for i in g[now]:
            cost = dist + i[0]
            if cost < distance[i[1]][0]:
                distance[i[1]][0] = cost
                distance[i[1]][1] = [now]
                heapq.heappush(q,(cost,i[1]))
            elif cost == distance[i[1]][0]:
                distance[i[1]][1].append(now)
    
    

    def recur(pos):
        if pos == S: return

        for i in distance[pos][1]:
            if i == -1: break

            for j in range(len(g[i])):
                if g[i][j][1] == pos:
                    recur(i)
                    del g[i][j]
                    break

    recur(D)

    distance = [INF]*(N)
    distance[S] = 0
    q = []
    heapq.heappush(q,(0,S))

    while q:
        dist,now = heapq.heappop(q)

        if dist > distance[now]: continue

        for i in g[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q,(cost,i[1]))

    if distance[D] == INF:
        print(-1)
    else:
        print(distance[D])
