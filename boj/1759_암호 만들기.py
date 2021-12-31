from itertools import combinations
l,c = map(int,input().split())
a = list(map(str,input().split()))
a.sort()
a = list(combinations(a,l))
m = ['a','e','i','o','u']
for s in a:
    flag = False
    countM = 0

    for c in s:
        if c in m:
            countM += 1

    if countM and l-countM >= 2: # 모음 개수 1 이상 and 자음 개수 2 이상
        for c in s:
            print(c,end='')        
        print()
