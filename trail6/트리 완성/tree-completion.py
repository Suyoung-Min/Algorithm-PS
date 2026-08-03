def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    parent = [i for i in range(n+1)] # 1~n

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
        
    part = 0
    cycle = 0
        
    for i in range(m):
        s, e = edges[i]
        
        if same(s, e):
            cycle += 1
        
        union(s, e)
    
    part = len(set(find(i) for i in range(1, n+1)))  # 그래프 부분 개수 구하기
    
    ans = (part-1) + cycle
    print(ans)
        
if __name__ == '__main__':
    main()