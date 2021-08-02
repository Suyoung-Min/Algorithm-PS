n = int(input())

for i in range(n):
    arr = input()
    flag = 0
    ans = 0
    for j in arr:
        if j == 'O':
            flag+=1
            ans+=flag
        else:
            flag=0

    print(ans)
