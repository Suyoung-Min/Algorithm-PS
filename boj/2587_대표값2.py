arr=[0]*5
sum=0
for i in range(5):
    arr[i]=int(input())
    sum+=arr[i]
arr.sort()
print(sum//5,arr[2],sep='\n')
