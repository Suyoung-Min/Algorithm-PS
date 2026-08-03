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
        
    for i in range(m):
        s, e = edges[i]
        
        if same(s, e):
            print(i+1)
            return
        
        union(s, e)
    
    print('happy')    
        
if __name__ == '__main__':
    main()