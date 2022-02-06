N,r,c = map(int,input().split())

count,y,x = 0,0,0
while N > 0:
    l = 2**(N-1)

    if r < y+l:
        if c >= x+l:
            count += l*l
            x += l
    else:
        y += l
        if c >= x+l:
            count += l*l*3
            x += l
        else: count += l*l*2

    N-=1

print(count)

# 일일이 재귀는 시간초과 => 사분면으로 나눠서 타겟 분면만 탐색하도록 재귀를 
