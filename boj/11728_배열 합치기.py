from collections import deque
input()
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = deque()
i=0
j=0
while i<len(a) and j<len(b):
    if a[i] <= b[j]:
        ans.append(a[i])
        i+=1
    else:
        ans.append(b[j])
        j+=1
if i<len(a):
    for t in range(i,len(a)):
        ans.append(a[t])
elif j<len(b):
    for t in range(j,len(b)):
        ans.append(b[t])
print(*ans)

# Merge Sort 의 정렬 부분을 활용 & deque으로 시간 
