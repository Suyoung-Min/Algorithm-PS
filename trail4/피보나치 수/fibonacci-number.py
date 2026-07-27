N = int(input())

# Please write your code here.

fibo_arr = [0] * 46
fibo_arr[1] = 1
fibo_arr[2] = 1

def fibo(num):
    if fibo_arr[num]: return fibo_arr[num]

    fibo_arr[num] = fibo(num - 1) + fibo(num - 2)

    return fibo_arr[num]


print(fibo(N))