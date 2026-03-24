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
def manhattan_dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def solve():
    
    coins_pos = {} # 코인들 좌표
    coins_list = []
    ans = 1e9

    for y in range(n):
        for x in range(n):
            if grid[y][x] == 'S': # 시작점이면
                S_xy = (y,x)
            elif grid[y][x] == 'E': # 끝점이면
                E_xy = (y,x)

    for y in range(n):
        for x in range(n):
            if grid[y][x] == 'S': # 시작점이면
                coins_pos['start'] = (y,x)
            elif grid[y][x] == 'E': # 끝점이면
                coins_pos['end'] = (y,x)
            elif grid[y][x].isdigit(): # 동전이면
                coin_num = int(grid[y][x])
                
                coins_list.append(coin_num) # 코인 저장
                coins_pos[coin_num] = (y,x)
                
                
    
    coins_list.sort()
    
    # 코인별 조합 뽑기 및 거리 저장
    
    coin_nums = 0
        
    
    def backtracking(pos, idx, dist): # 최대 3개
        nonlocal ans, coin_nums
        
        # 가지치기 pruning 넣기
        
        if coin_nums == 3: # 종료조건 1. 3개 뽑았을 때
            
            dist += manhattan_dist(pos, coins_pos['end'])
            
            ans = min(ans, dist)
            
            return
        
        if dist >= ans:
            return
        
        if idx == len(coins_list): # 3개 이상으로 코인 못 뽑을 때
            return
        
        
        coin_nums += 1
        # 위치를 동전 위치로 옮기고, 거리 누적, 다음 동전 인덱스로 진행
        backtracking(coins_pos[coins_list[idx]], 
                     idx+1, 
                     dist + manhattan_dist(pos, coins_pos[coins_list[idx]]))
        
        coin_nums -= 1
        
        # 결정 2. 현재 동전(exist[idx])을 그냥 무시하고 지나칠 때
        # 내 위치와 거리는 그대로 둔 채, 다음 동전 인덱스만 확인하러 감
        backtracking(pos, idx + 1, dist)
        
            
    backtracking(coins_pos['start'], 0, 0)
    
    return ans
            
print(solve())
