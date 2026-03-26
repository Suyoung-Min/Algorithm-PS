import heapq
import sys

def main():
    input = sys.stdin.readline
    
    # 입력 받기
    line = input().split()
    if not line: return
    a, b, n = map(int, line)
    
    # 1. 메모리 최적화: 리스트 대신 딕셔너리 인접 리스트 사용
    # adj[u] = {v: (cost, time)} 형태로 저장하여 필요한 메모리만 사용합니다.
    adj = [{} for _ in range(1001)]
    
    for _ in range(n):
        cost, _ = map(int, input().split())
        route = list(map(int, input().split()))
        
        # i: 출발 정류장 인덱스, j: 도착 정류장 인덱스
        for i in range(len(route) - 1):
            for j in range(i + 1, len(route)):
                u, v = route[i], route[j]
                time = j - i  # 시간 계산
                
                # u에서 v로 가는 경로가 처음이거나, 더 효율적인(싸거나 빠른) 경로일 때만 저장
                if v not in adj[u]:
                    adj[u][v] = (cost, time)
                else:
                    prev_cost, prev_time = adj[u][v]
                    if cost < prev_cost:
                        adj[u][v] = (cost, time)
                    elif cost == prev_cost and time < prev_time:
                        adj[u][v] = (cost, time)

    # 2. 다익스트라 최적화
    # visited[정점] = [최소비용, 최소시간]
    visited = [[float('inf'), float('inf')] for _ in range(1001)]
    q = []
    
    visited[a] = [0, 0]
    # (비용, 시간, 현재정점) 순으로 push
    heapq.heappush(q, (0, 0, a))

    while q:
        curr_cost, curr_time, u = heapq.heappop(q)
        
        # 이미 더 좋은 경로를 찾았다면 스킵
        if curr_cost > visited[u][0]: continue
        if curr_cost == visited[u][0] and curr_time > visited[u][1]: continue
        
        # u와 연결된 목적지 v들만 확인 (딕셔너리이므로 존재하는 간선만 순회)
        for v, (w_cost, w_time) in adj[u].items():
            new_cost = curr_cost + w_cost
            new_time = curr_time + w_time
            
            # 비용이 더 저렴한 경우
            if new_cost < visited[v][0]:
                visited[v][0] = new_cost
                visited[v][1] = new_time
                heapq.heappush(q, (new_cost, new_time, v))
            # 비용은 같으나 시간이 더 짧은 경우
            elif new_cost == visited[v][0] and new_time < visited[v][1]:
                visited[v][1] = new_time
                heapq.heappush(q, (new_cost, new_time, v))
                
    # 결과 출력
    final_cost, final_time = visited[b]
    if final_cost == float('inf'):
        print("-1 -1")
    else:
        print(f"{final_cost} {final_time}")

if __name__ == "__main__":
    main()