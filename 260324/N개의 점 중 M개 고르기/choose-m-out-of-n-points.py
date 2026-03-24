n, m = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]

def dist(pos1, pos2):
    return (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2

ans = float('inf')

current = []

def backtracking(idx, max_dist):
    global ans
    
    # 종료 조건 1. m 개 뽑았을 때, 2. idx 끝일 때
    
    if len(current) == m:
        ans = min(ans, max_dist)
        return
    
    if idx == len(points):
        return
    
    # 뽑을 때
    
    if not current: # 점이 한개도 없으면 -> max_dist 갱신 없이
        current.append(points[idx])
        
        backtracking(idx+1, max_dist)
        
        current.pop()
    else: # 점이 한개 이상 존재할 때 -> max_dist 갱신
        tmp_dist = max_dist
        for point in current:
            tmp_dist = max(tmp_dist, dist(point, points[idx]))
            
        current.append(points[idx])
        
        backtracking(idx+1, tmp_dist)
        
        current.pop()

    # 안뽑을때
    backtracking(idx+1, max_dist)
    
backtracking(0, 0)

print(ans)