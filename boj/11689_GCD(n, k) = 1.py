n = int(input())
pi = n
prime = 2
while prime*prime <= n:
    if n%prime == 0:
        pi = int(pi/prime*(prime-1))
    while n%prime == 0:
        n = n//prime
    prime+=1
if n != 1:
    pi = int(pi/n*(n-1))
print(pi)

"""
소수 구하는 함수
오일러-파이 함수
 ϕ(n) = n(1-1/p_1)(1-1/p_2)../(1-1/p_k)
"""
