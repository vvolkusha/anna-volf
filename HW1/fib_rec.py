def fib_rec(n):
    sum = 0
    b = 0
    a = 1
    if (n == 1) or (n == 2):
        for i in range(n-1):
            sum = a + b
            b = a
            a = sum
        print(sum)
    else:
        print(fib(n-1) + fib(n-2))
print('Введите номер числа')
n = int(input())
fib_rec(n)