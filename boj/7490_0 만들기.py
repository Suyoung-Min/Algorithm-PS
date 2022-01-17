test_case = int(input())

ans = []
n = 0
def recur(x,part,prev):
    global ans,n

    if x == n+1:
        if part == 0:
            for i in range(n-1):
                print(str(i+1)+ans[i],end='')
            print(str(n))
        return

    ans.append(' ')
    if prev < 0:
        recur(x+1,(part-prev)+(prev*10-x),prev*10-x)
    else:
        recur(x+1,(part-prev)+(prev*10+x),prev*10+x)
    ans.pop()

    ans.append('+')
    recur(x+1,part+x,+x)
    ans.pop()

    ans.append('-')
    recur(x+1,part-x,-x)
    ans.pop()

for _ in range(test_case):
    n = int(input())

    recur(2,1,1)

    print()
