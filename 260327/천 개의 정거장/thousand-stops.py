import heapq
import sys

def main():
    # 전체 입력을 한 번에 읽어 처리 (매우 빠름)
    input_data = sys.stdin.read().split()
    if not input_data: return
    it = iter(input_data)
    
    start_node = int(next(it))
    end_node = int(next(it))
    n_bus = int(next(it))
    
    # 1. 그래프 구성
    # 1~1000: 실제 정거장
    # 1001~: 가상 정거장 (각 버스 노선의 정류장들)
    adj = [[] for _ in range(1001 + 1000000)] # 넉넉하게 가상 노드 공간 확보
    v_node_ptr = 1001 # 가상 노드 번호 할당용 포인터
    
    for _ in range(n_bus):
        cost = int(next(it))
        num_stops = int(next(it))
        route = [int(next(it)) for _ in range(num_stops)]
        
        for i in range(num_stops):
            curr_stop = route[i]
            curr_v_node = v_node_ptr + i
            
            # (1) 승차: 실제 정거장 -> 가상 노드 (비용 발생, 시간 0)
            adj[curr_stop].append((curr_v_node, cost, 0))
            
            # (2) 하차: 가상 노드 -> 실제 정거장 (비용 0, 시간 0)
            adj[curr_v_node].append((curr_stop, 0, 0))
            
            # (3) 주행: 이전 가상 노드 -> 현재 가상 노드 (비용 0, 시간 1)
            if i > 0:
                prev_v_node = curr_v_node - 1
                adj[prev_v_node].append((curr_v_node, 0, 1))
                
        v_node_ptr += num_stops # 다음 버스를 위해 가상 노드 번호 대역 이동

    # 2. 다익스트라
    inf = float('inf')
    # visited[node] = [min_cost, min_time]
    # 전체 노드 수(v_node_ptr)만큼 초기화
    dist = [[inf, inf] for _ in range(v_node_ptr)]
    
    dist[start_node] = [0, 0]
    q = [(0, 0, start_node)] # (비용, 시간, 노드)

    while q:
        d_cost, d_time, u = heapq.heappop(q)
        
        if d_cost > dist[u][0]: continue
        if d_cost == dist[u][0] and d_time > dist[u][1]: continue
        
        # 가상 노드 설계 덕분에 간선 수가 매우 적어 u에서 연결된 v만 확인하면 됨
        for v, w_cost, w_time in adj[u]:
            next_cost = d_cost + w_cost
            next_time = d_time + w_time
            
            if next_cost < dist[v][0]:
                dist[v][0], dist[v][1] = next_cost, next_time
                heapq.heappush(q, (next_cost, next_time, v))
            elif next_cost == dist[v][0] and next_time < dist[v][1]:
                dist[v][1] = next_time
                heapq.heappush(q, (next_cost, next_time, v))
                
    # 3. 결과 출력
    res_c, res_t = dist[end_node]
    if res_c == inf:
        print("-1 -1")
    else:
        print(f"{res_c} {res_t}")

if __name__ == "__main__":
    main()