n,l = map(int,input().split(' '))
a=list(map(int,input().split(' ')))

a.sort()

front=0
tape=0
for i in a:
    if front <= i - 0.5:
        tape+=1
        front=i-0.5+l
    elif i-0.5 < front and front < i+0.5:
        front+=l
        tape+=1
print(tape)
