n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.
from collections import deque

def find_bomb_seq(bombs):

    bombs_deq = deque([])
    start = 0
    i = 0
    while i <= len(bombs)-1:

        if bombs[i] == bombs[start]:
            if i == len(bombs)-1: # 마지막이면
                if i-start+1 >= m: # 
                    bombs_deq.append((start,i))
        else: # 이전 스택과 다른 숫자면
            if (i-1)-start+1 >= m:
                bombs_deq.append((start,i-1))
                start = i
                continue # 혹시라도 m=1 일 수 있으니
            start = i

        i+=1

    return bombs_deq

bombs_deq=find_bomb_seq(numbers)
while bombs_deq:

    visited = [1]*len(numbers)

    for bse in bombs_deq:
        bs, be = bse

        for i in range(bs,be+1):
            visited[i] = 0

    tmp = []

    for i in range(len(numbers)):
        if visited[i]:
            tmp.append(numbers[i])
    
    numbers = tmp

    bombs_deq=find_bomb_seq(numbers)

print(len(numbers))
for i in range(len(numbers)):
    print(numbers[i])