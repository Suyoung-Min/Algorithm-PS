n,k=map(int,input().split())
arr=[i+1 for i in range(n)]
ans=[]
idx=0
while arr:
    idx=(idx+k-1)%len(arr)
    ans.append(arr.pop(idx))
print(end='<')
print(*ans,sep = ', ',start='<',end='>')
