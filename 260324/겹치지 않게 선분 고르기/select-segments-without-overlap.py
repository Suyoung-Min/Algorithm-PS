n = int(input())
segments = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

lines = []
ans = 0

def backtracking(start): # idx 0 ~ n-1
    global ans
    
    # 백트래킹 종료 조건 -> segments 마지막까지 탐색했을 때
    
    if start == n:
        ans = max(ans, len(lines))
        return
    
    for i in range(start, len(segments)):
        
        lines.append(segments[i])
        # 후보 리스트에 넣고 리스트 내 선분들이 겹치는지 아닌지 탐색
        # 겹치면 넘기기
        # 겹치지 않으면 백트래킹 더 진행
        
        overlapped = False
        
        for j in range(len(lines)):
            for k in range(j+1, len(lines)):
                ax1, ax2 = lines[j]
                bx1, bx2 = lines[k]
                
                if max(ax1, bx1) <= min(ax2, bx2): # 겹치면
                    overlapped = True
                    break
                    
        if not overlapped: # 겹치지 않으면 백트래킹 더 진행
            backtracking(i+1)
            
        lines.pop()
        
backtracking(0)    
            
print(ans)