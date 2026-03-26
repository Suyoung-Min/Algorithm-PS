import heapq
import sys

def main():
    # 입력 속도 최적화
    input = sys.stdin.readline
    
    # a: 시작점, b: 도착점, n: 버스 개수
    try:
        line = input().split()
        if not line: return
        a, b, n = map(int, line)
    except ValueError: return

    # 1. 간선 최적화 (인접 행렬 사용)
    # 1000개 정점 기준, [비용, 시간]의 최솟값만 저장하여 메모리 낭비를 막습니다.
    adj = [[ [float('inf'), float('inf')] for _ in range(1001)] for _ in range(1001)]
    
    for _ in range(n):
        # 버스 비용과 정류장 개수 입력
        cost, _ = map(int, input().split())
        route = list(map(int, input().split()))
        
        # 요청하신 대로 i(출발 인덱스), j(도착 인덱스)로 변경
        for i in range(len(route) - 1):
            for j in range(i + 1, len(route)):
                u, v = route[i], route[j]
                time = j - i # 정거장 간의 시간(간격) 계산
                
                # 동일한 구간(u -> v)에 대해 가장 효율적인 노선만 남김
                if cost < adj[u][v][0]:
                    adj[u][v] = [cost, time]
                elif cost == adj[u][v][0]:
                    if time < adj[u][v][1]:
                        adj[u][v][1] = time

    # 2. 다익스트라 (메모리 및 시간 효율화)
    # visited[정점] = [최소비용, 최소시간]
    visited = [[float('inf'), float('inf')] for _ in range(1001)]
    q = []
    
    visited[a][0] = 0
    visited[a][1] = 0
    # (비용, 시간, 현재정점) 순으로 넣어야 heapq가 비용 우선, 시간 차선으로 정렬해줍니다.
    heapq.heappush(q, (0, 0, a)) 

    while q:
        curr_cost, curr_time, u = heapq.heappop(q)
        
        # 이미 처리된 더 좋은 경로가 있다면 스킵
        if curr_cost > visited[u][0]: continue
        if curr_cost == visited[u][0] and curr_time > visited[u][1]: continue
        
        # 연결된 모든 정점(v)을 확인
        for v in range(1, 1001):
            if adj[u][v][0] == float('inf'): continue
            
            new_cost = curr_cost + adj[u][v][0]
            new_time = curr_time + adj[u][v][1]
            
            # 비용이 더 저렴한 경우
            if new_cost < visited[v][0]:
                visited[v][0] = new_cost
                visited[v][1] = new_time
                heapq.heappush(q, (new_cost, new_time, v))
            # 비용은 같지만 시간이 더 단축되는 경우
            elif new_cost == visited[v][0] and new_time < visited[v][1]:
                visited[v][1] = new_time
                heapq.heappush(q, (new_cost, new_time, v))
                
    # 결과 도출
    final_cost = visited[b][0]
    final_time = visited[b][1]
    
    if final_cost == float('inf'):
        print("-1 -1")
    else:
        print(f"{final_cost} {final_time}")

if __name__ == "__main__":
    main()