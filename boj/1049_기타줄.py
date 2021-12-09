N,M = map(int,input().split())

package_min=int(1e9)
one_min = int(1e9)

for _ in range(M):
    package_cost, one_cost = map(int,input().split())
    if package_cost > one_cost*6:
        package_cost = one_cost*6

    if package_min > package_cost:
        package_min = package_cost
    
    if one_min > one_cost:
        one_min = one_cost

ans = 0

ans += (N//6)*package_min

if (N%6)*one_min < package_min:
    ans+=(N%6)*one_min
else:
    ans+=package_min

print(ans)
