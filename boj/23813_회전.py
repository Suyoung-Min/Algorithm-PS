N = input()

t = N
t = t[-1] + t[0:-1]
ans = 0

while True:
    ans += int(t)
    if t == N:
        break

    t = t[-1] + t[0:-1]

print(ans)
