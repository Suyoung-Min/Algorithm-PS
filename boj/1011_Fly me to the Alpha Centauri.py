import sys

t=int(input())
for i in range(t):
    b,a = map(int,sys.stdin.readline().split())
    a-=b
    flag = 0 if (a-int(a**0.5)**2)%int(a**0.5) == 0 else 1
    print(2*int(a**0.5)-1+(a-int(a**0.5)**2)//int(a**0.5)+flag)
