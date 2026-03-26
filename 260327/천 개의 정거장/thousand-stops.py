import heapq
import sys

def main():
    # 모든 입력을 한 번에 읽어오기
    input_data = sys.stdin.read().split()
    if not input_data: return
    it = iter(input_data)
    
    start_node = int(next(it))
    end_node = int(next(it))
    n_bus = int(next(it))
    
    # 노선 데이터를 먼저 리스트에 담아 전체 가상 노드 수를 파악
    bus_data = []
    total_stops = 0
    for _ in range(n_bus):
        cost = int(next(it))
        num_stops = int(next(it))
        route = [int(next(it)) for _ in range(num_stops)]
        bus_data.append((cost, route))
        total_stops += num_stops
    
    # 실제 노드 1000개 + 총 정류장 수만큼만 할당
    max_nodes = 1001 + total_stops
    adj = [[] for _ in range(max_nodes)]
    v_node_ptr = 1001
    
    for cost, route in bus_data:
        num_stops = len(route)
        for i in range(num_stops):
            curr_stop = route[i]
            curr_v_node = v_node_ptr + i
            
            # (1) 승차: 실제 정거장 -> 가상 노드 (비용 발생)
            adj[curr_stop].append((curr_v_node, cost, 0))
            # (2) 하차: 가상 노드 -> 실제 정거장 (비용 0)
            adj[curr_v_node].append((curr_stop, 0, 0))
            # (3) 주행: 가상 노드 간 이동 (시간 1 발생)
            if i > 0:
                adj[curr_v_node - 1].append((curr_v_node, 0, 1))
                
        v_node_ptr += num_stops

    # 다익스트라 최적화: 2차원 리스트 대신 1차원 리스트 2개 사용
    inf = float('inf')
    dist_cost = [inf] * max_nodes
    dist_time = [inf] * max_nodes
    
    dist_cost[start_node] = 0
    dist_time[start_node] = 0
    
    # 힙에는 (비용, 시간, 현재노드) 저장
    q = [(0, 0, start_node)]

    while q:
        d_cost, d_time, u = heapq.heappop(q)
        
        # 비용이 더 크면 무시, 비용이 같을 때 시간이 더 길어도 무시
        if d_cost > dist_cost[u]: continue
        if d_cost == dist_cost[u] and d_time > dist_time[u]: continue
        
        for v, w_cost, w_time in adj[u]:
            new_cost = d_cost + w_cost
            new_time = d_time + w_time
            
            if new_cost < dist_cost[v]:
                dist_cost[v] = new_cost
                dist_time[v] = new_time
                heapq.heappush(q, (new_cost, new_time, v))
            elif new_cost == dist_cost[v] and new_time < dist_time[v]:
                dist_time[v] = new_time
                heapq.heappush(q, (new_cost, new_time, v))
                
    # 최종 결과 출력
    if dist_cost[end_node] == inf:
        print("-1 -1")
    else:
        print(f"{dist_cost[end_node]} {dist_time[end_node]}")

if __name__ == "__main__":
    main()