n = int(input())

if n <= 10:
    print(n)
    quit()

q = [ i for i in range(10)]

cur = 9
while True:
    tmp = q.pop(0)
    for i in range(tmp%10):
        cur+=1
        ans = tmp*10 + i
        q.append(ans)
        if cur == n:
            print(ans)
            quit()
        if ans == 9876543210:
            print(-1)
            quit()
