n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
flat ={}
for x,y in points:
    if x not in flat:
        flat[x] = y
    elif y < flat[x]: flat[x] = y

ans = sum(flat.values())
print(ans)