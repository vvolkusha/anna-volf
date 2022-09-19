def fib(n):
    sum = 0
    a = 1
    b = 0
    if (n == 1) or (n==2):
        for i in range(n-1):
            sum = a + b
            b = a
            a = sum
        print(sum)
    else:
        for i in range (n-2):
            b, a = a, a + b
        print(a)
print('Введите номер числа')
n = int(input())
fib(n)
