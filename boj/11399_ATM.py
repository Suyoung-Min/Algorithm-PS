n=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
ans=0
for i in range(len(arr)):
    ans += arr[i]*(i+1)
print(ans)
