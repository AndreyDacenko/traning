from datetime import datetime

name2 = 'semen'
""" zamykanie """

def func_1(name):
    def inner_func(property):
        print(f'{name} {property}')
    return inner_func

func_1('andrey')('horoshiy')

v1 = func_1('oleg')
v2 = func_1('anton')
v1('molodec')
v2('ne molodec')
v2('vse taki molodec')


""" decorator """

def resp_time(func):
    def sole_time(*args, **kwargs):
        t0 = datetime.now()
        num = func(*args, **kwargs)
        print(f'Vremya raboty func: {datetime.now() - t0}')
        # print(f'Result: {num}')

    return sole_time


@resp_time
def stepen_2(n):
    result = 2 ** n
    return result

@resp_time
def stepen_3(n):
    result = 3 ** n
    return result


stepen_2(1000000000)
stepen_3(10000000)
