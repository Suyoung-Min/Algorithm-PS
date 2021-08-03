s=input()
arr=[]
for i in range(len(s)):
    arr.append(s[i:len(s)])
arr.sort()
print(*arr,sep='\n')
