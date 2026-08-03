from collections import deque

def main():
    n, m = map(int, input().split())
    
    a, b = map(int, input().split())
    
    edges = [[] for _ in range(n+1)] # 1~n 정점에 붙은 엣지들
    
    visited = [0] * (n+1)

    edges_input = [tuple(map(int, input().split())) for _ in range(m)]
    
    for s, e, satis in edges_input:
        edges[s].append((e, satis))
        edges[e].append((s, satis))
        
    q = deque([(a, float('inf'))]) # 시작점 및 초기 만족도
    
    max_min_satis = 0
    visited[a] = float('inf')
    
    while q:
        cur_v, cur_s = q.popleft() # cur_s 현재 위치에서 지나온 전선 값 중 작은 값
        
        if cur_v == b: # 도착했으면
            max_min_satis = max(max_min_satis, cur_s)
            continue
        
        for next_v, next_s in edges[cur_v]:
            new_s = min(cur_s, next_s)
            if not visited[next_v] or new_s > visited[next_v]:
                visited[next_v] = new_s
                q.append((next_v, new_s))

    print(max_min_satis)

if __name__ == '__main__':
    main()