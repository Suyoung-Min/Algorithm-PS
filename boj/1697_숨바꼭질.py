from collections import deque

n,k=map(int,input().split())
deq = deque()
deq.append((n,0))
visit=[False]*(100001)

while True:
    pos = deq.popleft()
    if pos[0]<0 or pos[0]>100000 or visit[pos[0]] == True:
        continue
    
    visit[pos[0]] = True
    if pos[0] == k:
        print(pos[1])
        break

    deq.append((pos[0]+1,pos[1]+1))
    deq.append((pos[0]-1,pos[1]+1))
    deq.append((pos[0]*2,pos[1]+1))
