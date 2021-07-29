a,b = map(int,input().split())
if a > b:
    t=a
    a=b
    b=t
if b-a <= 1:
    print(0)
    exit()
print(b-a-1)

for i in range(a+1,b):
    print(i,end=' ')
