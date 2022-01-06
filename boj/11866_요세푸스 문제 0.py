n,k = map(int,input().split())

ans = []
g = [i for i in range(1,n+1)]
idx = 0
while g:
    idx = (idx + k - 1)%(len(g))
    ans.append(g[idx])
    g.pop(idx)
ans = ', '.join(str(_) for _ in ans)
print(f'<{ans}>')
