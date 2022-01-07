import sys
from collections import deque
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    s = input().rstrip()

    l = deque()
    r = deque()

    for c in s:
        if c == '<':
            if l:
                r.appendleft(l.pop())
        elif c == '>':
            if r:
                l.append(r.popleft())
        elif c == '-':
            if l:
                l.pop()
        else:
            l.append(c)

    sys.stdout.write(''.join(l)+''.join(r)+'\n')
