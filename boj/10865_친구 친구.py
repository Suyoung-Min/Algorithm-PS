import sys
input = sys.stdin.readline
n,m= map(int,input().split())
friend = [0]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    friend[a]+=1
    friend[b]+=1
for i in range(1,n+1):
    print(friend[i])
