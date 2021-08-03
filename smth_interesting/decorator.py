def decor(func):
    def the_second_func(*args, **kwargs):
        input = func(*args, **kwargs)
        res = 100 - input
        return res
    return the_second_func()

@decor
def first_decorim_func():
    i = 10
    return i


@decor
def second_decorim_func():
    i = 15
    return i

print(first_decorim_func, second_decorim_func)
