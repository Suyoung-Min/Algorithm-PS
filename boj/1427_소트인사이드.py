n=input()
ans=[0 for _ in range(len(n))]
for i in range(len(n)):
    ans[i] = int(n[i])
ans.sort(reverse = True)
print(*ans,sep='')
