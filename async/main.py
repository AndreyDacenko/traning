import asyncio

# async def count(counter):
#     print(len(counter))
#
#     while True:
#         await asyncio.sleep(0.01)
#         counter.append(1)
#
#
#
# async def wait_1_sec(counter):
#     while True:
#         await asyncio.sleep(1)
#         print('1 sec')
#         print(f'zapisey: {len(counter)}')
#
# async def wait_5_sec():
#     while True:
#         await asyncio.sleep(5)
#         print('5 sec')
#
# async def wait_10_sec():
#     while True:
#         await asyncio.sleep(10)
#         print('10 sec')
#
#
#
# async def main():
#     counter = []
#     tasks = [
#         count(counter),
#         wait_1_sec(counter),
#         wait_5_sec(),
#         wait_10_sec()
#     ]
#
#     await asyncio.gather(*tasks)
#
#
# asyncio.run(main())

my_counter = 0

async def increase():
    global my_counter
    my_counter += 1

async def count():
    while True:
        await increase()
        print(my_counter)
        await asyncio.sleep(0.1)

asyncio.run(count())











# import threading
#
# def delayed(n):
#     print(f"Вывод через {n} секунд!")
#
# time1 = 5
# time2 = 7
#
# thread = threading.Timer(time1, delayed, [time1])
# thread.start()
#
# thread2 = threading.Timer(time2, delayed, [time2])
# thread2.start()

