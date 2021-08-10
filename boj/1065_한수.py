n = int(input())

def hansoo(t):
    t = str(t)
    flag = True
    prev = int(t[0])
    d=0
    for i in range(1,len(t)):
        if i == 1:
            d = int(t[i]) - prev
        elif d != int(t[i]) - prev:
            flag = False
            break
        prev = int(t[i])
    return flag

ans = 0
for i in range(1,n+1):
    if hansoo(i):
        ans+=1
print(ans)
