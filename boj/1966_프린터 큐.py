t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    queue = list(map(int,input().split()))

    order = 0
    while True:
        print_flag = True
        first = queue[0]
        for i in range(len(queue)):
            if first < queue[i]:
                queue.append(queue.pop(0))
                print_flag = False
                m = len(queue)-1 if m == 0 else m-1
                break
        if print_flag:
            queue.pop(0)
            order += 1
            if m == 0:
                print(order)
                break
            m = len(queue)-1 if m == 0 else m-1
