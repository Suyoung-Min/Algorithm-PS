import sys
input=sys.stdin.readline
n=int(input())
arr = [0]*(10001)
for i in range(n):
    arr[int(input())] += 1
for i in range(1,10001):
    for j in range(arr[i]):
        print(i)
        
"""
Counting sort => 원소들의 범위가 한정적이고 숫자가 많을 때 유용하다. 
일반적인 sort의 시간복잡도 O(nlogn)에 비해 Counting sort의 시간복잡도는 O(n)이다.
"""
