from collections import deque

def main():
    n, m = map(int, input().split())
    
    a, b = map(int, input().split())
    
    edges = [] # (satis, s, e)
    
    edges_input = [tuple(map(int, input().split())) for _ in range(m)]
    
    for s, e, satis in edges_input:
        edges.append((satis, s, e))
        
    edges.sort(reverse=True)
    
    parent = [i for i in range(n+1)] # 1~n 부모 설정 - 초기 부모는 자기 자신
    
    def find(x):
        if x == parent[x]: return x
        parent[x] = find(parent[x])
        return parent[x]
    
    def same(a, b):
        return find(a) == find(b)
    
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        
        parent[ max(root_a, root_b) ] = min(root_a, root_b)
        
    deq = deque(edges)
    
    ans = 0
    '''
    1. 높은 satis 순으로 엣지를 선택    
    2. s, e 유니온
    3. 연결 후 a 와 b 가 연결됨 -> 해당 엣지가 a 와 b 를 연결하는 최솟값 중 최대
    '''

    while deq:
        satis, s, e = deq.popleft()
        
        union(s, e)
        
        if same(a, b):
           ans = satis
           break
       
    print(ans) 
    
if __name__ == '__main__':
    main()