from collections import deque

F,S,G,U,D = map(int,input().split())

visit = [False] *(F+1)

q = deque()
visit[S] = True
q.append((S,0))
ans = -1

while q:
    pos, button = q.popleft()

    if pos == G:
        ans = button
        break

    if pos+U <= F and visit[pos+U]== False :
        visit[pos+U]=True
        q.append(((pos+U),button+1))

    if pos-D > 0 and visit[pos-D]==False:
        visit[pos-D]=True
        q.append(((pos-D),button+1))

if ans == -1:
    print('use the stairs')
else:
    print(ans)
