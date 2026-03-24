n = int(input())

grid = [
    list(input().rstrip()) for _ in range(n)
]


# Please write your code here.

"""
1. 동전 위치 파악
2. 동전마다 각 동전 및 S, E 까지 거리 파악 -> 중복방문 허용 및 동전위치 가능
3. 동전들 중 3개 조합 -> 순서는 오름차순 고정
4. 3개 조합 a, b, c S -> a -> b -> c -> E 거리로 최단거리 갱신
"""
def p2p_dist(ay, ax, by, bx):
    return abs(ay-by)+ abs(ax-bx)


def solve():
    c2c = [[0]*11 for _ in range(11)] # 각 코인별 거리 -> c2c[y][0] = S->y, c2c[y][10] -> y->E
    coins_cord = [None for _ in range(10)] # 코인들 좌표
    coins_list = []
    S_xy = 0
    E_xy = 0
    ans = 1e9

    for y in range(n):
        for x in range(n):
            if grid[y][x] == 'S': # 시작점이면
                S_xy = (y,x)
            elif grid[y][x] == 'E': # 끝점이면
                E_xy = (y,x)

    for y in range(n):
        for x in range(n):
            if grid[y][x].isdigit(): # 동전이면
                coin_num = int(grid[y][x])
                
                coins_list.append(coin_num) # 코인 저장
                coins_cord[coin_num] = (y,x)
                
                c2c[coin_num][0] = p2p_dist(*(y,x), *S_xy) # S -> c 거리저장
                c2c[coin_num][10] = p2p_dist(*(y,x), *E_xy) # c -> E 거리저장
                
    if len(coins_list) < 3:
        return -1
    
    coins_list.sort()
    
    # 각 코인별 이동거리 - 작은 코인에서 큰 코인 거리만 저장
    
    for i in range(len(coins_list)):
        for j in range(i+1, len(coins_list)):
            coin_num_a = coins_list[i]
            coin_num_b = coins_list[j]
            
            c2c[coin_num_a][coin_num_b] = p2p_dist(*coins_cord[coin_num_a], *coins_cord[coin_num_b])
            
            
    # 코인별 조합 뽑기 및 거리 저장
    
    def backtracking(current, start, dist): # 최대 3개
        nonlocal ans
        
        if len(current) == 3: # 마지막 c -> E 넣어주기
            
            dist += c2c[current[-1]][10]
            
            ans = min(ans, dist)
            return
        
        for i in range(start, len(coins_list)): # 코인 리스트는 오름차순 정렬되어 있음
            
            coin_num = coins_list[i]
            
            if not current: # 현재 current 가 비어있으면
                
                current.append(coin_num)
                dist += c2c[coin_num][0] # S -> c
                
                backtracking(current, i+1, dist)
                
                dist -= c2c[coin_num][0]
                current.pop()
                
            else: # 안비어있으면
                
                prev_coin_num = current[-1] # 이전 리스트 마지막 코인
                dist += c2c[prev_coin_num][coin_num]
                current.append(coin_num)
                
                backtracking(current, i+1, dist)
                
                dist -= c2c[prev_coin_num][coin_num]
                current.pop()
            
    backtracking([], 0, 0)
    
    return ans
            
print(solve())