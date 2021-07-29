n = int(input())
b = list(map(int,input().split()))
c = sorted(b)
visited = [False] *(n+1)
for i in range(len(b)):
    for j in range(len(b)):
        if b[i] == c[j] and not visited[j]:
            print(j,end=' ')
            visited[j] = True
            break
            
##############################################
n = int(input())
t = list(map(int, input().split()))
s_li = sorted(t)
li = []
for i in range(n):
    idx = s_li.index(t[i])
    li.append(idx)
    s_li[idx] = -1
print(*li)
