from datetime import datetime

old_list = [5, 15, -12, 45, 87, 3, -7, 95, 32]
print(f'Old list: {old_list}')
bubble_sort_list = old_list.copy()
select_sort_list = old_list.copy()
insert_sort_list = old_list.copy()


def my_timer(func):
    def wripper(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        print(f'{args[1]} {datetime.now() - start_time} {args[0]}')

    return wripper


@my_timer
def bubble_sort(my_list, sort_type):
    last_item = len(my_list) - 1
    for i in range(0, last_item):
        for x in range(0, last_item - i):
            if my_list[x] > my_list[x + 1]:
                my_list[x], my_list[x + 1] = my_list[x + 1], my_list[x]

    return my_list, sort_type


@my_timer
def select_sort(my_list, sort_type):
    for i in range(len(my_list) - 1):
        m = my_list[i]  # запоминаем минимальное значение
        p = i  # запоминаем индекс минимального значения
        for j in range(i + 1, len(my_list)):  # поиск миимального среди оставшихся элементов
            if m > my_list[j]:
                m = my_list[j]
                p = j

        if p != i:  # обмен значениями, если был найден минимальный не в i-й позиции
            t = my_list[i]
            my_list[i] = my_list[p]
            my_list[p] = t

    return my_list, sort_type


@my_timer
def insert_sort(my_list, sort_type):
    for i in range(1, len(my_list)):
        for j in range(i, 0, -1):
            if my_list[j] < my_list[j - 1]:
                my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
            else:
                break

    return my_list, sort_type


bubble_sort(bubble_sort_list, 'bubble_sort')
select_sort(select_sort_list, 'select_sort')
insert_sort(insert_sort_list, 'insert_sort')
