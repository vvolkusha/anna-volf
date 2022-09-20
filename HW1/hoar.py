import random
def hoar(a):
    if len(a)>1:
        x = a[random.randint(0, len(a) - 1)]
        less = [cur for cur in a if cur < x ]
        equal = [cur for cur in a if cur == x ]
        more = [cur for cur in a if cur > x ]
        a = hoar(less) + equal + hoar(more)

    return a
print('Введите числа')
a = input()
a = hoar(a)
a.sort()

print(a)
