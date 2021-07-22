import itertools

def f(a):
    r=0
    for i in range(len(a)-1):
        r+=abs(a[i]-a[i+1])
    return r

n=int(input())
a=list(map(int,input().split(' ')))
m=0
for i in itertools.permutations(a):
    t=f(i)
    m = t if t > m else m
print(m)
