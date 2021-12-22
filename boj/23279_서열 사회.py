n,k = map(int,input().split())

for _ in range(k):
    arr = list(map(int,input().split()))
    index = [i+1 for i in range(arr[0])]
    del arr[0]
    arr.sort()
    arr = [arr[i]+index[i] for i in range(len(arr))]

    for i in arr:
        print(i,end=' ')
    print()
