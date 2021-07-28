while True:
    n=input()
    if n == '0':
        break
    flag=True
    for i in range(len(n)//2):
        if n[i] != n[len(n)-1-i]:
            flag = False
            break
    if flag:
        print('yes')
    else:
        print('no')
