def solve():
    n = int(input())

    left = [0] * 26
    right = [0] * 26

    for _ in range(n):
        x, l, r = input().split()

        left[ord(x) - ord('A')] = l
        right[ord(x) - ord('A')] = r

    def preorder(x):
        if x == '.': return
        print(x, end='')
        preorder(left[ord(x) - ord('A')])
        preorder(right[ord(x) - ord('A')])

    def inorder(x):
        if x == '.': return
        inorder(left[ord(x) - ord('A')])
        print(x, end='')
        inorder(right[ord(x) - ord('A')])

    def postorder(x):
        if x == '.': return
        postorder(left[ord(x) - ord('A')])
        postorder(right[ord(x) - ord('A')])
        print(x, end='')

    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')
    print()

solve()