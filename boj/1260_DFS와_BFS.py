def dfs(p):
    if dfsVisit[p]==1:
        return
    dfsVisit[p]=1
    print(p,end=' ')
    for i in range(1,n+1):
        if graph[p][i] == 1:
            dfs(i)

n,m,v=list(map(int,input().split(' ')))
graph=[[0]*(n+1) for i in range(n+1)]
dfsVisit,bfsVisit=[0]*(n+1),[0]*(n+1)
for i in range(m):
    a,b=list(map(int,input().split(' ')))
    graph[a][b]=1
    graph[b][a]=1
dfs(v)
print()
Q=[v]
while Q:
    s=Q.pop(0)
    bfsVisit[s] = 1
    print(s,end=' ')
    for i in range(1,n+1):
        if graph[s][i]==1 and bfsVisit[i]==0:
            bfsVisit[i]=1
            Q.append(i)
