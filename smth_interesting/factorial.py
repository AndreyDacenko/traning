from functools import reduce

# num = int(input('Введите число: '))

num = 5
n = [i for i in range(1, num + 1)]
res = reduce(lambda x, y: x * y, n)
print(res)

def factor_rec(num):
    if num < 1:
        return ('unknown')
    elif num == 1:
        return 1
    else:
        return factor_rec(num - 1) * num

print(factor_rec(5))

def factor_range(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

print(factor_range(5))