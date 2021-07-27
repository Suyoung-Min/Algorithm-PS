arr = [0] * 7
sum=0
min_odd=int(1e9)
odd_flag = False
for i in range(7):
    arr[i] = int(input())

for i in arr:
    if i%2 == 1:
        odd_flag = True
        sum+=i
        if i < min_odd:
            min_odd = i

if odd_flag:
    print(sum,min_odd,sep='\n')
else:
    print(-1)
