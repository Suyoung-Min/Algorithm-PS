n,m=map(int,input().split(' '))
board=[None]*n
for i in range(n):
   board[i]=input()

ans = float('inf')

for i in range(n-7):
    for j in range(m-7):
        
        tmp = 0
        for y in range(i,i+8):
            for x in range(j,j+8):
                if (i+j)%2 == (x+y)%2 and board[y][x] != 'W':
                    tmp += 1
                elif (i+j)%2 != (x+y)%2 and board[y][x] != 'B':
                    tmp +=1
            if tmp > ans:
                break
        if tmp < ans:
            ans = tmp

        tmp = 0
        for y in range(i,i+8):
            for x in range(j,j+8):
                if (i+j)%2 == (x+y)%2 and board[y][x] != 'B':
                    tmp += 1
                elif (i+j)%2 != (x+y)%2 and board[y][x] != 'W':
                    tmp +=1
            if tmp > ans:
                break
        
        if tmp < ans:
            ans = tmp

print(ans)

"""
short version

n,m=map(int,input().split(' '))
board=[None]*n
for i in range(n):
   board[i]=input()

ans = float('inf')

def check(i,j,flag):
    tmp = 0
    if flag == 0:
        color = 'W'
    else:
        color = 'B'
    for y in range(i,i+8):
        for x in range(j,j+8):
            if (i+j)%2 == (x+y)%2 and board[y][x] != color:
                tmp += 1
            elif (i+j)%2 != (x+y)%2 and board[y][x] == color:
                tmp +=1
        if tmp > ans:
            break
    return tmp

for i in range(n-7):
    for j in range(m-7):
        t = check(i,j,0)
        ans = t if t < ans else ans
        t = check(i,j,1)
        ans = t if t < ans else ans

print(ans)
"""
