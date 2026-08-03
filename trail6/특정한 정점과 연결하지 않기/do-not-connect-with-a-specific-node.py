from collections import defaultdict

def main():
    n,m = map(int, input().split())
    
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    
    a, b, k = map(int, input().split())
    
    parent = [i for i in range(n+1)]
    
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
        
        
    '''
    각 Part 개수 (a, b 포함된 파트는 제외)
    Part 를 연결된 정점의 개수 기준으로 내림차순 정렬한 후,
    sum(Part[:k]) + Part_a
    '''
    
    for s, e in edges:
        union(s, e)
    
    part = [find(i) for i in range(1, n+1)]
    
    part_count = defaultdict(int)
    
    for node in part:
        part_count[node] += 1
        
    part_a = part_count.pop(find(a))
    part_b = part_count.pop(find(b))
    
    part_list = list(part_count.values())
    part_list.sort(reverse=True)
    
    ans = part_a + sum(part_list[:k])
    
    print(ans)


if __name__ == '__main__':
    main()