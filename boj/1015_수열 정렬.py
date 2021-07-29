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
