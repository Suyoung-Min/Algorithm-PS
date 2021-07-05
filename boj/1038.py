n = int(input())

if n <= 10:
    print(n)
    quit()

q = []
for i in range(1,10):
    q.append(i)

cur = 9
while True:
    tmp = q.pop(0)
    for i in range(tmp%10):
        cur+=1
        q.append(tmp*10 + i)
        if cur == n:
            print(tmp*10 + i)
            quit()
        if tmp*10 + i == 9876543210:
            print(-1)
            quit()
