def solve():
    k = int(input())

    inorder_traversal = list(map(int, input().split()))

    node = [0] * (1 << k) # 1 ~ 2**k - 1

    inorder_index = []

    def inorder(x):
        if x >= (1 << k): return
        inorder(2*x)
        inorder_index.append(x)
        inorder(2*x + 1)

    inorder(1)

    for idx, value in zip(inorder_index, inorder_traversal):
        node[idx] = value

    for h in range(1, k+1):
        for i in range((1 << (h-1)), (1 << h)):
            print(node[i], end=' ')
        print()

solve()