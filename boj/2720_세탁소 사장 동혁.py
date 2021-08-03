t=int(input())
arr = [25,10,5,1]
ans = [0]*4
for i in range(t):
    c = int(input())
    idx=0
    for i in arr:
        ans[idx] = c//i
        c%=i
        idx+=1
    print(*ans,sep=' ')
