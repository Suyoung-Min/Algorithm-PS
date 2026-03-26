
def main():
    
    a, b, n = map(int, input().split()) # 시작점 a 도착점 b 버스 개수 n
    
    bus_route = [[] for _ in range(n+1)] # 버스 노선 저장 1 ~ n 번 버스
    bus_cost = [0] * (n+1)
    
    edges = [[] for _ in range(1001)]
    visited = [[float('inf'), float('inf')] for _ in range(1001)] # [거리, 시간]
    # 경로 1 ~ 1000 s. (e, cost, time)
    # 시작점. (도착점, 비용, 시간)
    
    for i in range(1, n + 1):
        
        bus_cost[i], _ = map(int, input().split())
        bus_route[i] = list(map(int, input().split()))
        
        for j in range(len(bus_route[i])-1):
            tmp_time = 0
            
            for k in range(j+1, len(bus_route[i])):
                tmp_time += 1
                edges[bus_route[i][j]].append((bus_route[i][k], bus_cost[i], tmp_time))

                
    import heapq
    
    q = []
    visited[a][0] = 0 # 비용
    visited[a][1] = 0 # 시간
    heapq.heappush(q, (0, a, 0)) # (비용, 정점, 시간)
    
    # 다익스트라 비용 기준으로 돌린 후, 시간은 같은 거리일 때 비교
    
    while q:
        cost, cur_v, time = heapq.heappop(q)
        
        if cost > visited[cur_v][0]: continue
        
        for next_v, next_cost, next_time in edges[cur_v]:
            
            new_cost = cost + next_cost
            new_time = time + next_time
            
            if new_cost < visited[next_v][0]: # 기존 비용보다 작으면
                visited[next_v][0] = new_cost # 비용 갱신
                visited[next_v][1] = new_time
                
                heapq.heappush(q, (new_cost, next_v, new_time))
            elif new_cost == visited[next_v][0] and new_time < visited[next_v][1]: # 기존 비용과 동일하고, 시간이 짧을 때
                visited[next_v][1] = new_time
                
                heapq.heappush(q, (new_cost, next_v, new_time)) # 시간 갱신해서 다시 큐에
        
        
    final_cost = -1 if visited[b][0] == float('inf') else visited[b][0]
    final_time = -1 if visited[b][1] == float('inf') else visited[b][1]
    
    print(final_cost, final_time)
        
if __name__ == "__main__":
    main()