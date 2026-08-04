import heapq
from bisect import bisect_left, bisect_right

num_q = int(input())

pinput = list(map(int, input().split()))

perfume = dict()

idx = 1
for sn in pinput[2:]:
    perfume[idx] = sn
    idx += 1
    

for _ in range(num_q-1):
    
    cmd, k = map(int, input().split())

    if cmd == 2: # 향로 추가
        perfume[idx] = k
        idx += 1
        
    elif cmd == 3:
        print(perfume.pop(k, -1))    
        
    elif cmd == 4:
        # k 블렌딩
        parr = list(perfume.values())
        pset = set(parr)
        
        INF = float('inf')
        
        dp = [INF] * (3001)
        dp[0] = 0
        
        for x in pset:
            dp[x] = 1
            
        def solve_dp(v):
            if dp[v] != INF: return dp[v]
            
            for x in pset:
                if v - x >= 0:
                    dp[v] = min(dp[v], solve_dp(v - x) + 1)
                    
            return dp[v]
        
        
        ans = solve_dp(k)
        
        print(ans if ans != INF else -1)
        
    elif cmd == 5:
        # 3개로 향수 구성  탑노트, 미들노트, 베이스노트
        # 합이 k 이상
        # 3개 같은 경우 s1
        # 2개 같은 경우 s2 * 3
        # 3개 다 다른 경우 s3 * 6
        parr = list(perfume.values())
        
        s1 = 0
        for x in parr:
            if x*3 >= k:
                s1 += 1
                
        parr.sort()
        
        s2 = 0
        for i in range(len(parr)):
            tgt = k - parr[i] * 2
            
            j = bisect_left(parr, tgt)
            
            s2 += len(parr) - j
            
            if j <= i: s2 -= 1
            
        s3 = 0
        for l in range(len(parr)-2):
            for m in range(l+1, len(parr)-1):
                tgt = k - parr[l] - parr[m]
                
                r = bisect_left(parr, tgt)
                
                if r <= m:
                    s3 += len(parr) - m - 1
                else: # r > m
                    s3 += len(parr) - r
        
        print(s1 + s2*3 + s3*6)