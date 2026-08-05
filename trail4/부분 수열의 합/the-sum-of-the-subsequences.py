n, m = map(int, input().split())
A = list(map(int, input().split()))

bits = 1                      # 0번 비트 = 합 0 도달 가능
for a in A:
    bits |= bits << a

print('Yes' if (bits >> m) & 1 else 'No')