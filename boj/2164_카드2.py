from collections import deque # deque 덱 사용하는 경우를 생각하자 앞뒤 추가 & 삭제 O(1) BUT, List는 O(n)

n=int(input())
deq = deque([i+1 for i in range(n)])

while True:
    if len(deq)>=2:
        deq.popleft()
    else:
        print(deq[0])
        break
    deq.append(deq.popleft())
